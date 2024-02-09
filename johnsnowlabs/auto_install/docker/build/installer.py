import os

from johnsnowlabs import nlp


HARDWARE_TARGET = os.environ.get("HARDWARE_TARGET", "cpu")
model_ref = os.environ.get("MODEL_TO_LOAD", None)


nlp.install(
    json_license_path="/run/secrets/license",
    browser_login=False,
    force_browser=False,
    hardware_platform=HARDWARE_TARGET,
)
nlp.start(model_cache_folder="/app/model_cache")
if model_ref:
    # Cache model, if not specified user must
    # mount a folder to /app/model_cache/ which has a folder named `served_model`
    pipe = nlp.load(model_ref)
    pipe.predict("init")
    pipe.save("/app/model/served_model")
