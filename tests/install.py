import os
import unittest
from unittest.mock import patch

from johnsnowlabs import nlp, settings
from johnsnowlabs.py_models.jsl_secrets import JslSecrets


class EnforceVersions(unittest.TestCase):
    def setUp(self) -> None:
        nlp.settings.enforce_versions=True

    @patch("johnsnowlabs.py_models.jsl_secrets.JslSecrets.enforce_versions")
    def test_should_try_to_enforce_versions(self, mock_enforce_versions):
        nlp.install(med_license=os.environ.get("TEST_VALID_LICENSE"), only_refresh_credentials=True, refresh_install=True)
        self.assertTrue(mock_enforce_versions.called)

    def test_should_install_compatible_secrets_with_valid_license(self):
        nlp.install(med_license=os.environ.get("TEST_VALID_LICENSE"), only_refresh_credentials=True, refresh_install=True)
        secrets = JslSecrets.from_jsl_home()
        self.assertEqual(secrets.HC_LICENSE, os.environ.get("TEST_VALID_LICENSE"))
        self.assertEqual(secrets.HC_VERSION, settings.raw_version_secret_medical)
        self.assertEqual(secrets.OCR_VERSION, settings.raw_version_secret_ocr)
    
    def test_should_fallback_to_existing_secrets_with_invalid_license(self):
        nlp.install(med_license=os.environ.get("TEST_INVALID_LICENSE"), 
                    ocr_secret="random-ocr-secret",
                    enterprise_nlp_secret="random-medical-secret",
                    only_refresh_credentials=True, refresh_install=True)
        secrets = JslSecrets.from_jsl_home()
        self.assertTrue(secrets.HC_LICENSE, os.environ.get("TEST_INVALID_LICENSE"))
        self.assertEqual(secrets.HC_SECRET, "random-medical-secret")
        self.assertEqual(secrets.OCR_SECRET, "random-ocr-secret")
    

class DonotEnforceVersions(unittest.TestCase):
    def setUp(self) -> None:
        nlp.settings.enforce_versions=False
        self.enterprise_nlp_secret = "nlp_random"
        self.ocr_secret = "ocr_random"

    def test_should_install_incompatible_secrets_from_input(self):
        nlp.install(med_license=os.environ.get("TEST_VALID_LICENSE"),ocr_secret=self.ocr_secret, enterprise_nlp_secret=self.enterprise_nlp_secret, visual=True , only_refresh_credentials=True, refresh_install=True)
        secrets = JslSecrets.from_jsl_home()
        self.assertEqual(secrets.HC_LICENSE, os.environ.get("TEST_VALID_LICENSE"))
        self.assertEqual(secrets.HC_SECRET, self.enterprise_nlp_secret)
        self.assertEqual(secrets.OCR_SECRET, self.ocr_secret)
    
    @patch("johnsnowlabs.py_models.jsl_secrets.JslSecrets.enforce_versions")
    @patch("johnsnowlabs.py_models.jsl_secrets.JslSecrets.is_ocr_secret_correct_version")
    @patch("johnsnowlabs.py_models.jsl_secrets.JslSecrets.is_hc_secret_correct_version")
    def test_should_not_try_to_enforce_versions_if_input_secrets_are_compatible(self, mock_hc_secret_correct, mock_ocr_secret_correct, mock_enforce_versions):
        nlp.install(med_license=os.environ.get("TEST_VALID_LICENSE"), only_refresh_credentials=True, refresh_install=True)
        mock_hc_secret_correct.return_value = True
        mock_ocr_secret_correct.return_value = True
        self.assertFalse(mock_enforce_versions.called)
