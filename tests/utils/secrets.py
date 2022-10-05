import json
import os
secret_path=''
license_dict = json.load(open(secret_path))
AWS_ACCESS_KEY_ID = license_dict.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = license_dict.get("AWS_SECRET_ACCESS_KEY")
JSL_SECRET = license_dict.get("SECRET")
SPARK_NLP_LICENSE = license_dict.get("SPARK_NLP_LICENSE")
OCR_SECRET = license_dict.get("SPARK_OCR_SECRET")
OCR_LICENSE = license_dict.get("SPARK_OCR_LICENSE")
