from dataclasses import dataclass
from enum import Enum
from functools import partial
from pathlib import Path
from typing import Optional, Union, Dict, List
from abc import ABC, abstractmethod
import glob

import requests
import json

from johnsnowlabs.py_models.lib_version import LibVersion
from johnsnowlabs.utils.enums import ProductName

from johnsnowlabs.abstract_base.pydantic_model import WritableBaseModel
from johnsnowlabs.py_models.primitive import LibVersionIdentifier, Secret
import os

from johnsnowlabs.utils.file_utils import json_path_as_dict
from johnsnowlabs.utils.my_jsl_api import get_user_licenses, download_license, get_access_token, \
    get_access_key_from_browser, get_user_lib_secrets
from johnsnowlabs import settings
from pydantic import Field, validator

secret_json_keys = ['JSL_SECRET', 'SECRET', 'SPARK_NLP_LICENSE', 'JSL_LICENSE', 'JSL_VERSION', 'PUBLIC_VERSION',
                    'AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY',
                    'SPARK_OCR_LICENSE', 'SPARK_OCR_SECRET', 'OCR_VERSION',
                    'HC_SECRET', 'HC_LICENSE', 'HC_VERSION', 'OCR_SECRET', 'OCR_LICENSE',
                    'JSL_LEGAL_LICENSE',
                    'JSL_FINANCE_LICENSE',
                    ]

already_logged = False
ocr_validation_logged = False
hc_validation_logged = False


class JslSecrets(WritableBaseModel):
    """Representation of a JSL credentials and helper
    methods for reading/storing found_secrets and managing .jslhome folder
    """
    HC_SECRET: Secret = None
    HC_LICENSE: Secret = None
    HC_VERSION: Optional[LibVersionIdentifier] = None
    OCR_SECRET: Secret = None
    OCR_LICENSE: Secret = None
    OCR_VERSION: Optional[LibVersionIdentifier] = None
    AWS_ACCESS_KEY_ID: Secret = None
    AWS_SECRET_ACCESS_KEY: Secret = None
    NLP_VERSION: Optional[LibVersionIdentifier] = None
    JSL_LEGAL_LICENSE: Secret = None
    JSL_FINANCE_LICENSE: Secret = None

    @staticmethod
    def raise_invalid_version():
        print(
            f'To fix invalid license please visit https://my.johnsnowlabs.com/ and download license with the latest secrets. '
            f'This file cannot be used to install any of the licensed libraries ')
        raise ValueError('Invalid secrets')

    @validator('HC_SECRET')
    def hc_version_check(cls, HC_SECRET):
        global hc_validation_logged
        try:
            if not JslSecrets.is_hc_secret_correct_version(HC_SECRET) and not hc_validation_logged:
                hc_validation_logged = True
                print(
                    f"🚨 Outdated Medical Secrets in license file. Version={HC_SECRET.split('-')[0]} but should be Version={settings.raw_version_medical}")
                if settings.enforce_secret_on_version:
                    raise ValueError('Invalid HC Secret')
                else:
                    return HC_SECRET

            else:
                return HC_SECRET
        except ValueError as err:
            cls.raise_invalid_version()
        except Exception as err:
            pass

    @staticmethod
    def is_ocr_secret_correct_version(ocr_secret: Optional[str]) -> bool:
        return ocr_secret and ocr_secret.split('-')[0] == settings.raw_version_ocr

    @staticmethod
    def is_hc_secret_correct_version(hc_secret: Optional[str]) -> bool:
        return hc_secret and hc_secret.split('-')[0] == settings.raw_version_medical

    @validator('OCR_SECRET')
    def ocr_version_check(cls, OCR_SECRET):
        global ocr_validation_logged
        try:
            if not JslSecrets.is_ocr_secret_correct_version(OCR_SECRET) and not ocr_validation_logged:
                ocr_validation_logged = True
                print(
                    f"🚨 Outdated OCR Secrets in license file. Version={OCR_SECRET.split('-')[0]} but should be Version={settings.raw_version_ocr}")
                if settings.enforce_secret_on_version:
                    raise ValueError("Invalid OCR Secret")
                else:
                    return OCR_SECRET
            else:
                return OCR_SECRET
        except ValueError as err:
            cls.raise_invalid_version()
        except Exception as err:
            pass

    @staticmethod
    def is_other_older_secret(first, other: Optional[str]):
        """Compare one secret value to another i.e. first.secret >= other.secret .
         Returns True if first is larger or equal to other
         Returns False if the other is a newer secret"""
        v1 = LibVersion(first.split('-')[0])
        if not other:
            return False
        v2 = LibVersion(other.split('-')[0])
        if v1.equals(v2):
            return False
        # If the other lib is older, then it must not be greater
        return not v1.is_other_greater(v2)

    def equal_credentials(self, other: 'JslSecrets'):
        """
        Compare this secret to another secret, returns True for equal and False otherwise.
        Since library secrets are universally equal across all secrets,
        we just jest the fields,AWS_SECRET_ACCESS_KEY,AWS_ACCESS_KEY_ID,OCR_LICENSE,HC_LICENSE
        for equality and omit secret fields for Lib Version
        :param other: another instance of JslSecrets to compare
        :return: True for equal False otherwise
        """
        if any([
            self.AWS_SECRET_ACCESS_KEY != other.AWS_SECRET_ACCESS_KEY,
            self.AWS_ACCESS_KEY_ID != other.AWS_ACCESS_KEY_ID,
            self.OCR_LICENSE != other.OCR_LICENSE,
            self.HC_LICENSE != other.HC_LICENSE,
            self.JSL_LEGAL_LICENSE != other.JSL_LEGAL_LICENSE,
            self.JSL_FINANCE_LICENSE != other.JSL_FINANCE_LICENSE,
        ]):
            return False
        else:
            return True

    def equal_lib_secrets(self, other: 'JslSecrets'):
        """
        Compare lib secrets to another secret, returns True for equal and False otherwise.
        Anything which is not a lib secret is referred to as a credential
        for equality and omit secret fields for Lib Version
        :param other: another instance of JslSecrets to compare
        :return: True for equal False otherwise
        """
        if any([
            self.OCR_SECRET != other.OCR_SECRET,
            self.HC_SECRET != other.HC_SECRET,
        ]):
            return False
        else:
            return True

    @staticmethod
    def build_or_try_find_secrets(
            browser_login: bool = True,
            force_browser: bool = False,
            access_token: Optional[str] = None,
            local_license_number: int = 0,
            remote_license_number: int = 0,
            secrets_file: Optional[str] = None,
            hc_license: Optional[str] = None,
            hc_secret: Optional[str] = None,
            ocr_secret: Optional[str] = None,
            ocr_license: Optional[str] = None,
            aws_access_key: Optional[str] = None,
            aws_key_id: Optional[str] = None,
            fin_license: Optional[str] = None,
            leg_license: Optional[str] = None,
            return_empty_secrets_if_none_found=False,
            store_in_jsl_home=True
    ) -> Union['JslSecrets', bool]:
        """
        Builds JslSecrets object if any found_secrets supplied or if none supplied,
         tries out every default resolution method defined to find found_secrets
        and build a JSlSecrets object.
        at the end of flow we always check if secrets are new and store to disk if they are, unless

        :return: JslSecrets if any found_secrets found otherwise False
        """
        secrets = None
        try:
            # we wrap this flow with try/except, so that incase we get invalid license data
            # we can still try loading from JSL-Home afterwards

            if any([hc_license, hc_secret, ocr_secret, ocr_license, aws_access_key, aws_key_id]):
                # Some found_secrets are supplied
                secrets = JslSecrets(HC_SECRET=hc_secret, HC_LICENSE=hc_license, OCR_SECRET=ocr_secret,
                                     OCR_LICENSE=ocr_license,
                                     AWS_ACCESS_KEY_ID=aws_key_id, AWS_SECRET_ACCESS_KEY=aws_access_key,
                                     JSL_LEGAL_LICENSE=leg_license, JSL_FINANCE_LICENSE=fin_license)
            elif access_token:
                secrets = JslSecrets.from_access_token(access_token, remote_license_number)

            # elif email and passw:
            #     found_secrets = JslSecrets.from_email_and_pass(email, passw,local_license_number)

            elif secrets_file:
                # Load from JSON file from provided secret file
                secrets = JslSecrets.from_json_file_path(secrets_file)

            if not secrets and not force_browser:
                # Try auto Resolve credentials if none are supplied
                secrets = JslSecrets.search_default_locations(license_number=local_license_number)
            if not secrets and not force_browser:
                # Search Env Vars
                secrets = JslSecrets.search_env_vars()
        except Exception as err:
            print(f'🚨 Failure Trying to read license {err}\n',
                  f'Trying to use license from John Snow Labs home folder if it exists')

        if not secrets and not force_browser:
            # Search Env Vars
            secrets = JslSecrets.from_jsl_home(license_number=local_license_number)

        if browser_login and not secrets or force_browser:
            # TODO more exception handling and pick License from UI?
            access_token = get_access_key_from_browser()
            secrets = JslSecrets.from_access_token(access_token, remote_license_number)

        if not secrets and return_empty_secrets_if_none_found:
            # Return empty found_secrets object
            return JslSecrets()
        if secrets and store_in_jsl_home:
            # We found some found_secrets
            # Store them if this is the first time JSL-Creds are loaded on this machine
            JslSecrets.store_in_jsl_home_if_new(secrets)
            return secrets

        return False

    @staticmethod
    def dict_has_jsl_secrets(secret_dict: Dict[str, str]) -> bool:

        for key in secret_json_keys:
            if key in secret_dict:
                return True
        return False

    @staticmethod
    def search_env_vars() -> Union['JslSecrets', bool]:
        """
        Search env vars for valid JSL-Secret values
        :return: JslSecrets if secret found, False otherwise
        """
        # We define max json size, anything above this will not be checked

        hc_secret = os.environ['JSL_SECRET'] if 'JSL_SECRET' in os.environ else None
        if not hc_secret:
            hc_secret = os.environ['SECRET'] if 'SECRET' in os.environ else None
        if not hc_secret:
            hc_secret = os.environ['HC_SECRET'] if 'HC_SECRET' in os.environ else None

        hc_license = os.environ['SPARK_NLP_LICENSE'] if 'SPARK_NLP_LICENSE' in os.environ else None
        if not hc_license:
            hc_license = os.environ['JSL_LICENSE'] if 'JSL_LICENSE' in os.environ else None
        if not hc_license:
            hc_license = os.environ['HC_LICENSE'] if 'HC_LICENSE' in os.environ else None

        hc_version = os.environ['JSL_VERSION'] if 'JSL_VERSION' in os.environ else None
        if not hc_version:
            hc_version = os.environ['HC_VERSION'] if 'HC_VERSION' in os.environ else None

        nlp_version = os.environ['PUBLIC_VERSION'] if 'PUBLIC_VERSION' in os.environ else None
        aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID'] if 'AWS_ACCESS_KEY_ID' in os.environ else None
        aws_access_key = os.environ['AWS_SECRET_ACCESS_KEY'] if 'AWS_SECRET_ACCESS_KEY' in os.environ else None

        ocr_license = os.environ['SPARK_OCR_LICENSE'] if 'SPARK_OCR_LICENSE' in os.environ else None
        if not ocr_license:
            ocr_license = os.environ['OCR_LICENSE'] if 'OCR_LICENSE' in os.environ else None

        ocr_secret = os.environ['SPARK_OCR_SECRET'] if 'SPARK_OCR_SECRET' in os.environ else None
        if not ocr_secret:
            ocr_secret = os.environ['OCR_SECRET'] if 'OCR_SECRET' in os.environ else None

        ocr_version = os.environ['OCR_VERSION'] if 'OCR_VERSION' in os.environ else None

        leg_license = os.environ['JSL_LEGAL_LICENSE'] if 'JSL_LEGAL_LICENSE' in os.environ else None
        fin_license = os.environ['JSL_FINANCE_LICENSE'] if 'JSL_FINANCE_LICENSE' in os.environ else None

        if any([hc_secret, hc_license, hc_license, hc_version, nlp_version, aws_access_key_id, aws_access_key,
                ocr_license, ocr_secret, ocr_version]):
            print('👌 License detected in Environment Variables')
            return JslSecrets(
                HC_SECRET=hc_secret,
                HC_LICENSE=hc_license,
                HC_VERSION=hc_version,
                OCR_SECRET=ocr_secret,
                OCR_LICENSE=ocr_license,
                OCR_VERSION=ocr_version,
                NLP_VERSION=nlp_version,
                AWS_ACCESS_KEY_ID=aws_access_key_id,
                AWS_SECRET_ACCESS_KEY=aws_access_key,
                JSL_LEGAL_LICENSE=leg_license,
                JSL_FINANCE_LICENSE=fin_license, )
        return False

    @staticmethod
    def search_default_locations(license_number=0) -> Union['JslSecrets', bool]:
        """
        Search default google colab folder and current working dir for
        for JSL Secret json file
        :return: JslSecrets if secret found, False otherwise
        """
        # We define max json size, anything above this will not be checked
        max_json_file_size = 10000

        # 1. Check colab content folder
        if os.path.exists('/content'):
            j_files = glob.glob('/content/*.json')
            for f_path in j_files:
                try:
                    if os.path.getsize(f_path) > max_json_file_size:
                        continue
                    json_dict = JslSecrets.json_path_as_dict(f_path)
                    if JslSecrets.dict_has_jsl_secrets(json_dict):
                        print(f'👌 Detected license file {f_path}')  # ✅
                        return JslSecrets.from_json_file_path(f_path)
                except:
                    continue

        # 2. Check current working dir
        j_files = glob.glob(f'{os.getcwd()}/*.json')
        for f_path in j_files:
            try:
                if os.path.getsize(f_path) > max_json_file_size:
                    continue

                json_dict = JslSecrets.json_path_as_dict(f_path)
                if JslSecrets.dict_has_jsl_secrets(json_dict):
                    print(f'👌 Detected license file {f_path}')  # ✅
                    return JslSecrets.from_json_file_path(f_path)
            except:
                continue
        # 3. Check JSL home
        return JslSecrets.from_jsl_home(license_number=license_number)

    @staticmethod
    def json_path_as_dict(path):
        with open(path) as f:
            return json.load(f)

    @staticmethod
    def from_json_file_path(secrets_path):
        if not os.path.exists(secrets_path):
            raise FileNotFoundError(f'No file found for secrets_path={secrets_path}')
        f = open(secrets_path)
        creds = JslSecrets.from_json_dict(json.load(f))
        f.close()
        return creds

    @staticmethod
    def from_access_token(access_token, license_number=0):
        licenses = get_user_licenses(access_token)
        secrets = get_user_lib_secrets(access_token)
        # 1. Oct Secret
        if license_number >= len(licenses) or license_number < 0:
            raise ValueError(
                f'You have {len(licenses)} in total. Input License Number {license_number} is invalid, up to {len(licenses) - 1} accepted.')
        data = download_license(licenses[license_number], access_token)

        # Fix lib secrets in license data to correct version
        ocr_candidates = list(
            filter(lambda x: x.version_secret == settings.raw_version_secret_ocr and x.product == ProductName.ocr,
                   secrets))
        hc_handidates = list(
            filter(lambda x: x.version_secret == settings.raw_version_secret_medical and x.product == ProductName.hc,
                   secrets))
        if hc_handidates:
            data['SECRET'] = hc_handidates[0].secret
            data['JSL_VERSION'] = hc_handidates[0].version
        if ocr_candidates:
            data['SPARK_OCR_SECRET'] = ocr_candidates[0].secret
            data['OCR_VERSION'] = ocr_candidates[0].version
        return JslSecrets.from_json_dict(data, licenses[license_number])

    @staticmethod
    def from_email_and_pass(email, passw, license_number=0):
        # TODO test and wait for PR !
        access_token = get_access_token(email, passw)
        licenses = get_user_licenses(access_token)
        data = download_license(licenses[license_number], access_token)
        secrets = JslSecrets.from_json_dict(data, licenses[license_number], )
        return secrets

    @staticmethod
    def from_json_dict(secrets, secrets_metadata: Optional = None) -> 'JslSecrets':
        hc_secret = secrets['JSL_SECRET'] if 'JSL_SECRET' in secrets else None
        if not hc_secret:
            hc_secret = secrets['SECRET'] if 'SECRET' in secrets else None
        if not hc_secret:
            hc_secret = secrets['HC_SECRET'] if 'HC_SECRET' in secrets else None

        hc_license = secrets['SPARK_NLP_LICENSE'] if 'SPARK_NLP_LICENSE' in secrets else None
        if not hc_license:
            hc_license = secrets['JSL_LICENSE'] if 'JSL_LICENSE' in secrets else None
        if not hc_license:
            hc_license = secrets['HC_LICENSE'] if 'HC_LICENSE' in secrets else None

        hc_version = secrets['JSL_VERSION'] if 'JSL_VERSION' in secrets else None
        if not hc_version:
            hc_version = secrets['HC_VERSION'] if 'HC_VERSION' in secrets else None

        nlp_version = secrets['PUBLIC_VERSION'] if 'PUBLIC_VERSION' in secrets else None
        aws_access_key_id = secrets['AWS_ACCESS_KEY_ID'] if 'AWS_ACCESS_KEY_ID' in secrets else None
        aws_access_key = secrets['AWS_SECRET_ACCESS_KEY'] if 'AWS_SECRET_ACCESS_KEY' in secrets else None

        ocr_license = secrets['SPARK_OCR_LICENSE'] if 'SPARK_OCR_LICENSE' in secrets else None
        if not ocr_license:
            ocr_license = secrets['OCR_LICENSE'] if 'OCR_LICENSE' in secrets else None

        ocr_secret = secrets['SPARK_OCR_SECRET'] if 'SPARK_OCR_SECRET' in secrets else None
        if not ocr_secret:
            ocr_secret = secrets['OCR_SECRET'] if 'OCR_SECRET' in secrets else None

        ocr_version = secrets['OCR_VERSION'] if 'OCR_VERSION' in secrets else None

        leg_license = secrets['JSL_LEGAL_LICENSE'] if 'JSL_LEGAL_LICENSE' in secrets else None
        fin_license = secrets['JSL_FINANCE_LICENSE'] if 'JSL_FINANCE_LICENSE' in secrets else None

        return JslSecrets(
            HC_SECRET=hc_secret,
            HC_LICENSE=hc_license,
            HC_VERSION=hc_version,
            OCR_SECRET=ocr_secret,
            OCR_LICENSE=ocr_license,
            OCR_VERSION=ocr_version,
            NLP_VERSION=nlp_version,
            AWS_ACCESS_KEY_ID=aws_access_key_id,
            AWS_SECRET_ACCESS_KEY=aws_access_key,
            JSL_LEGAL_LICENSE=leg_license,
            JSL_FINANCE_LICENSE=fin_license,

            # id=secrets_metadata['id'],
            # license_type=secrets_metadata['type'],
            # end_date=secrets_metadata['endDate'],
            # platform=secrets_metadata['platform'],
            # products=secrets_metadata['products'],

        )

    @staticmethod
    def from_jsl_home(license_number=0, log=True, raise_error=False) -> Union['JslSecrets', bool]:
        global already_logged
        if not os.path.exists(settings.creds_info_file):
            return False

        try:
            # Try/Catch incase we get validation errors from outdated files
            license_infos = LicenseInfos.parse_file(settings.creds_info_file)
            if log and not already_logged:
                already_logged = True
                print(
                    f'📋 Loading license number {license_number} from {settings.license_dir}/{list(license_infos.infos.keys())[license_number]}')
        except:
            license_infos = JslSecrets.update_outdated_lib_secrets()
        if license_number >= len(license_infos.infos) or license_number < 0:
            if raise_error:
                raise ValueError(
                    f'You have {len(license_infos.infos)} different credentials in total '
                    f'but specified license_number={license_number}.'
                    f'Please specify a number smaller than {len(license_infos.infos)}')
            else:
                return False
        return license_infos.infos[list(license_infos.infos.keys())[license_number]].jsl_secrets

    @staticmethod
    def update_outdated_lib_secrets(new_secrets: 'JslSecrets') -> Optional['LicenseInfos']:
        print('Trying to fix outdated licenses')
        hc_secrets = new_secrets.HC_SECRET
        ocr_secret = new_secrets.OCR_SECRET
        invalid_licenses = []
        for license in os.listdir(settings.license_dir):
            if license == 'info.json':
                continue
            secrets = JslSecrets.parse_file(f'{settings.license_dir}/{license}')
            if secrets.HC_SECRET and hc_secrets and \
                    JslSecrets.is_other_older_secret(hc_secrets, secrets.HC_SECRET):
                invalid_licenses.append(f'{settings.license_dir}/{license}')
            elif secrets.OCR_SECRET and ocr_secret \
                    and JslSecrets.is_other_older_secret(ocr_secret, secrets.OCR_SECRET):
                invalid_licenses.append(f'{settings.license_dir}/{license}')

        for license_path in invalid_licenses:
            print(f'Updating license file {license_path}')
            license_dict = json_path_as_dict(license_path)
            if license_dict['HC_LICENSE'] and hc_secrets \
                    and JslSecrets.is_other_older_secret(hc_secrets, license_dict['HC_SECRET']):
                print(
                    f'🤓 Upgraded Medical Secrets to {hc_secrets.split("-")[0]} in credentials file {license_path} ')
                license_dict['HC_SECRET'] = hc_secrets
            if license_dict['OCR_LICENSE'] and ocr_secret \
                    and JslSecrets.is_other_older_secret(ocr_secret, license_dict['OCR_SECRET']):
                print(
                    f'🤓 Upgraded OCR Secrets to {ocr_secret.split("-")[0]} in credentials file {license_path} ')
                license_dict['OCR_SECRET'] = ocr_secret
            JslSecrets(**license_dict).write(license_path)

        # we need to update info dict as well
        info_dict = json_path_as_dict(settings.creds_info_file)
        for license_file, license_metadata in info_dict['infos'].items():
            license_dict = license_metadata['jsl_secrets']
            if license_dict['HC_LICENSE'] and hc_secrets \
                    and JslSecrets.is_other_older_secret(hc_secrets, license_dict['HC_SECRET']):
                license_dict['HC_SECRET'] = hc_secrets
            if license_dict['OCR_LICENSE'] and ocr_secret \
                    and JslSecrets.is_other_older_secret(ocr_secret, license_dict['OCR_SECRET']):
                license_dict['OCR_SECRET'] = ocr_secret
        LicenseInfos(**info_dict).write(settings.creds_info_file)

        try:
            return LicenseInfos.from_home()
        except:
            print(
                '🚨 Looks like all your Credentials are outdated, please visist https://my.johnsnowlabs.com/ to get updated ones or contact John Snow Labs support')
            raise ValueError('Outdated John Snow Labs Credentials Directory')

    @staticmethod
    def are_credentials_known(found_secrets: 'JslSecrets') -> bool:
        # Return True, if secrets are already stored in JSL-Home, otherwise False
        Path(settings.py_dir).mkdir(parents=True, exist_ok=True)
        if os.path.exists(settings.creds_info_file):
            license_infos = LicenseInfos.parse_file(settings.creds_info_file)
        else:
            # If license dir did not exist yet, secrets are certainly new
            return False

        # if any stored secrets equal to found_secrets, then we already know then
        return any(map(lambda x: found_secrets.equal_credentials(x.jsl_secrets), license_infos.infos.values()))

    @staticmethod
    def are_lib_secrets_an_upgrade(found_secrets: 'JslSecrets') -> bool:
        # Return True, if lib are newer than existing ones, if yes upgrade locally stored secrets
        Path(settings.py_dir).mkdir(parents=True, exist_ok=True)
        if os.path.exists(settings.creds_info_file):
            license_infos = LicenseInfos.parse_file(settings.creds_info_file)
        else:
            # If license dir did not exist yet, secrets are certainly new
            return False

        # if any stored secrets equal to found_secrets, then we already know them
        # check OCR secrets
        if found_secrets.HC_SECRET:
            if any(map(lambda x: JslSecrets.is_other_older_secret(found_secrets.HC_SECRET, x.jsl_secrets.HC_SECRET),
                       license_infos.infos.values())):
                return True
        if found_secrets.OCR_SECRET:
            if any(map(lambda x: JslSecrets.is_other_older_secret(found_secrets.OCR_SECRET, x.jsl_secrets.OCR_SECRET),
                       license_infos.infos.values())):
                return True
        return False

    @staticmethod
    def store_in_jsl_home_if_new(secrets: 'JslSecrets') -> None:
        global already_logged
        # Store secrets in JSL home and update info file if secrets are new
        if JslSecrets.are_lib_secrets_an_upgrade(secrets):
            # Update all secret files in JSL home, since this one has an upgrade
            JslSecrets.update_outdated_lib_secrets(secrets)
        if JslSecrets.are_credentials_known(secrets):
            return

        # Store the secret, since it's new
        Path(settings.license_dir).mkdir(parents=True, exist_ok=True)
        products = []
        file_name = 'license_number_{number}_for_'
        if secrets.HC_LICENSE:
            products.append(ProductName.hc.value)
        if secrets.OCR_LICENSE:
            products.append(ProductName.ocr.value)

        file_name = file_name + '_'.join(products) + f'.json'

        if os.path.exists(settings.creds_info_file):
            license_infos = LicenseInfos.parse_file(settings.creds_info_file)
            file_name = file_name.format(number=str(len(license_infos.infos)))
            license_info = LicenseInfo(jsl_secrets=secrets, products=products, id=str(len(license_infos.infos)))
            license_infos.infos[file_name] = license_info
            license_infos.write(settings.creds_info_file)
            out_dir = f'{settings.license_dir}/{file_name}'
            secrets.write(out_dir)
            print(f'📋 Stored new John Snow Labs License in {out_dir}')
        else:
            file_name = file_name.format(number='0')
            license_info = LicenseInfo(jsl_secrets=secrets, products=products, id='0')
            LicenseInfos(infos={file_name: license_info}).write(settings.creds_info_file)
            out_dir = f'{settings.license_dir}/{file_name}'
            secrets.write(out_dir)
            print(f'📋 Stored John Snow Labs License in {out_dir}')
            # We might load again JSL-Secrets from local
            already_logged = True


class MyJslLicenseDataResponse(WritableBaseModel):
    """Representation of MyJSL API Response"""
    id: str
    license_type: str
    end_date: str
    platform: Optional[str]
    products: List[ProductName]
    product_name: ProductName


class LicenseInfo(WritableBaseModel):
    id: str
    jsl_secrets: JslSecrets
    products: List[ProductName]


class LicenseInfos(WritableBaseModel):
    """Representation of a LicenseInfo in ~/.johnsnowlabs/licenses/info.json
    Maps file_name to LicenseInfo
    """
    infos: Dict[str, LicenseInfo]

    @staticmethod
    def from_home() -> Optional['LicenseInfos']:
        if os.path.exists(settings.creds_info_file):
            return LicenseInfos.parse_file(settings.creds_info_file)
        return None
