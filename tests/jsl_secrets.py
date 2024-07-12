import unittest
from unittest.mock import patch

from johnsnowlabs import settings
from johnsnowlabs.py_models.jsl_secrets import JslSecrets
from johnsnowlabs.utils.my_jsl_api import LibSecretResponse


class JslSecretsTestCase(unittest.TestCase):
    def setUp(self):
        self.license = "license"
        self.valid_healthcare_secret =  settings.raw_version_secret_medical+ "-healthcare-secret"
        self.valid_ocr_secret = settings.raw_version_secret_ocr +  "-ocr-secret"

    @patch("johnsnowlabs.py_models.jsl_secrets.get_secrets")
    def test_enforce_versions_should_retrieve_matching_secrets(self, mock_get_secrets):
        mock_get_secrets.return_value = [
            LibSecretResponse(
                product="Healthcare NLP",
                version=settings.raw_version_secret_medical,
                secret=self.valid_healthcare_secret,
                isLatest=True,
            ),
            LibSecretResponse(
                product="Visual NLP",
                version=settings.raw_version_secret_ocr,
                secret=self.valid_ocr_secret,
                isLatest=True,
            ),
            LibSecretResponse(
                product="Healthcare NLP",
                version="x.x",
                secret="healthcare-invalid-secret",
                isLatest=False,
            ),
            LibSecretResponse(
                product="Visual NLP",
                version="x.x",
                secret="ocr-invalid-secret",
                isLatest=False,
            ),
        ]
        secrets = JslSecrets.enforce_versions(JslSecrets(OCR_LICENSE=self.license))
        self.assertEqual(secrets.OCR_LICENSE, self.license)
        self.assertEqual(secrets.HC_VERSION, settings.raw_version_secret_medical)
        self.assertEqual(secrets.OCR_VERSION, settings.raw_version_secret_ocr)
        self.assertEqual(secrets.HC_SECRET, self.valid_healthcare_secret)
        self.assertEqual(secrets.OCR_SECRET, self.valid_ocr_secret)


    @patch("johnsnowlabs.py_models.jsl_secrets.get_secrets")
    def test_should_return_existing_secret_if_no_matching_secret_found(self, mock_get_secrets):
        existing_secrets = JslSecrets(HC_LICENSE=self.license, OCR_SECRET="ocr-invalid-secret", HC_SECRET="healthcare-invalid-secret")
        mock_get_secrets.return_value = [
            LibSecretResponse(
                product="Healthcare NLP",
                version="x.x",
                secret="healthcare-invalid-secret",
                isLatest=False,
            ),
            LibSecretResponse(
                product="Visual NLP",
                version="x.x",
                secret="ocr-invalid-secret",
                isLatest=False,
            ),
        ]
        secrets = JslSecrets.enforce_versions(existing_secrets)
        self.assertEqual(secrets.HC_LICENSE, self.license)
        self.assertEqual(secrets.HC_SECRET, existing_secrets.HC_SECRET)
        self.assertEqual(secrets.OCR_SECRET,existing_secrets.OCR_SECRET)
 