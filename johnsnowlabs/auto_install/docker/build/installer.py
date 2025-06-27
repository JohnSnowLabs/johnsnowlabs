import os
from johnsnowlabs import settings, nlp

settings.enforce_versions = False

nlp_license = os.environ.get("JOHNSNOWLABS_LICENSE", None)
nlp_secret = os.environ.get("MEDICAL_SECRET", None)
visual_secret = os.environ.get("VISUAL_SECRET", None)
aws_access_key_id = os.environ.get("JOHNSNOWLABS_AWS_ACCESS_KEY_ID", None)
aws_secret_access_key = os.environ.get("JOHNSNOWLABS_AWS_SECRET_ACCESS_KEY", None)
HARDWARE_TARGET = os.environ.get("HARDWARE_TARGET", "cpu")
model_ref = os.environ.get("MODEL_TO_LOAD", None)
model_bucket = os.environ.get("MODEL_BUCKET", None)
model_lang = os.environ.get("MODEL_LANGUAGE", 'en')

nlp.install(
    browser_login=False,
    force_browser=False,
    med_license=nlp_license,
    enterprise_nlp_secret=nlp_secret,
    ocr_secret=visual_secret,
    visual=True if visual_secret else False,
    aws_key_id=aws_access_key_id,
    aws_access_key=aws_secret_access_key,
    hardware_platform=HARDWARE_TARGET,
)
nlp.start(model_cache_folder="/app/model_cache", aws_access_key=aws_secret_access_key, aws_key_id=aws_access_key_id,
          hc_license=nlp_license, enterprise_nlp_secret=nlp_secret, visual_secret=visual_secret,
          visual=True if visual_secret else False, )
if model_ref:
    print(f'Downloading model {model_ref} from bucket {model_bucket} with language {model_lang}')
    # Cache model, if not specified user must
    # mount a folder to /app/model_cache/ which has a folder named `served_model`
    if model_bucket == 'clinical/ocr':
        from sparkocr.pretrained import PretrainedPipeline
        PretrainedPipeline(model_ref, model_lang, model_bucket).model.save("/app/model")
    else:
        nlp.PretrainedPipeline(model_ref, model_lang, model_bucket).model.save("/app/model")
else:
    print("No model reference provided, skipping model download and validating provided model on disk")
    # Validate Model should be stored in /opt/ml/model
    nlp.PretrainedPipeline.from_disk("/app/model")
