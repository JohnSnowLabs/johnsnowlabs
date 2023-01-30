from typing import Dict, Tuple

from colorama import Fore

from johnsnowlabs import settings
from johnsnowlabs.abstract_base.software_product import AbstractSoftwareProduct
from johnsnowlabs.auto_install.softwares import Software
from johnsnowlabs.py_models.jsl_secrets import LicenseInfos
from johnsnowlabs.utils.enums import ProductName
from johnsnowlabs.utils.my_jsl_api import get_access_key_from_browser, get_user_licenses


def check_health(check_install=True):
    # Print status of installations and licenses
    install_status: Dict[AbstractSoftwareProduct:bool] = {}
    health_check: Dict[AbstractSoftwareProduct:bool] = {}
    license_check: Dict[str, Tuple[bool, bool]] = {}
    print(f'{"_" * 10}Installation check results{"_" * 10}')
    for product in ProductName:
        if check_install:
            product = Software.for_name(product)
            if not product or not product.pypi_name:
                continue
            install_status[product] = (
                product.check_installed() and product.check_installed_correct_version()
            )
            if not product.check_installed():
                print(f"{product.logo + product.name} is not installed 🚨")
            elif not product.check_installed_correct_version():
                print(
                    f"{product.logo + product.pypi_name + Fore.LIGHTRED_EX}=={product.get_installed_version() + Fore.RESET} "
                    f"is installed but should be {product.pypi_name}=={Fore.LIGHTGREEN_EX + product.latest_version.as_str() + Fore.RESET} 🚨 To fix run:"
                )

                if product.licensed:
                    print(
                        f"{Fore.LIGHTGREEN_EX}nlp.install(){Fore.RESET} while authorizing to upgrade {product.logo + product.pypi_name}"
                    )
                else:
                    print(
                        f"{Fore.LIGHTGREEN_EX}python -m pip install {product.pypi_name}=={product.latest_version.as_str()} --upgrade{Fore.RESET}"
                    )
            else:
                print(
                    f"{product.logo + product.pypi_name}=={product.get_installed_version()} "
                    f"{Fore.LIGHTGREEN_EX}is correctly installed! ✅{Fore.RESET}"
                )

        if health_check:
            health_check[product] = product.health_check()


def list_remote_licenses():
    access_token = get_access_key_from_browser()
    licenses = get_user_licenses(access_token)

    print("Your Remote licenses in https://my.johnsnowlabs.com:")
    for i, lic in enumerate(licenses):
        softwares = [Software.for_name(p.value) for p in lic.products]
        print(
            f'Remote License Number {i} Has access to: {", ".join([s.logo + s.name for s in softwares])}.\n'
            f"Extra info for License {i}: EndDate={lic.endDate}, Type={lic.type}, Platform={lic.platform}, Id={lic.id} "
        )

        print("_" * 50)


def list_local_licenses():
    print(f"Your licenses in {settings.license_dir}")
    licenses = LicenseInfos.from_home()
    if not licenses:
        raise Exception("You have no local licenses")
    i = 0
    for file, lic in licenses.infos.items():
        softwares = [Software.for_name(p.value) for p in lic.products]
        print(
            f'Your local license in {i} Has access to: {", ".join([s.logo + s.name for s in softwares])}.\n'
            f"Extra info for License {i}: File={file} Id={lic.id}"
        )
        i += 1
        print("_" * 50)
