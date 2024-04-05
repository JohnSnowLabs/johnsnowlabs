import json
import os
import sys
from enum import Enum
from typing import List

from fastapi import FastAPI, Request
from fastapi import UploadFile, File
from starlette.responses import JSONResponse

from johnsnowlabs import *

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable
visual_enabled = 'VISUAL_SECRET' in os.environ
aws_access_key_id = os.environ.get("JOHNSNOWLABS_AWS_ACCESS_KEY_ID", None)
aws_secret_access_key = os.environ.get("JOHNSNOWLABS_AWS_SECRET_ACCESS_KEY", None)
hardware_target = os.environ.get("HARDWARE_TARGET", "cpu")
model_ref = os.environ.get("MODEL_TO_LOAD", None)

nlp_secret = os.environ.get("MEDICAL_SECRET", None)
nlp_license = os.environ.get("JOHNSNOWLABS_LICENSE", None)
visual_secret = os.environ.get("VISUAL_SECRET", None)

# jars loaded from jsl-home
nlp.start(model_cache_folder="/app/model_cache", aws_access_key=aws_secret_access_key, aws_key_id=aws_access_key_id,
          hc_license=nlp_license, enterprise_nlp_secret=nlp_secret, visual_secret=visual_secret,
          visual=True if visual_secret else False, )

model = nlp.load(path="/app/model/served_model", verbose=True)
if visual_enabled:
    # TODO this needs to be set by NLU
    model.contains_ocr_components = True




class OutputLevel(Enum):
    document = "document"
    sentence = "sentence"
    relation = "relation"
    chunk = "chunk"
    token = "token"


app = FastAPI()


@app.get("/predict")
async def predict(
        text: str = "Your text that you want to predict with the model goes here",
        output_level: OutputLevel = OutputLevel.document,
        positions: bool = False,
        metadata: bool = False,
        drop_irrelevant_cols: bool = False,
        get_embeddings: bool = False,  # true?
        keep_stranger_features: bool = True,
):
    return model.predict(
        text,
        output_level=output_level.value,
        positions=positions,
        metadata=metadata,
        drop_irrelevant_cols=drop_irrelevant_cols,
        get_embeddings=get_embeddings,
        keep_stranger_features=keep_stranger_features,
    ).to_json()


@app.post("/predict_batch")
async def predict_batch(
        text: List[str] = [
            "Your text that you want to predict with the model goes here",
            "More text can go here and will be interpreted as 2nd row",
        ],
        output_level: OutputLevel = OutputLevel.document,
        positions: bool = False,
        metadata: bool = False,
        drop_irrelevant_cols: bool = False,
        get_embeddings: bool = False,  # true?
        keep_stranger_features: bool = True,
):
    return model.predict(
        text,
        output_level=output_level.value,
        positions=positions,
        metadata=metadata,
        drop_irrelevant_cols=drop_irrelevant_cols,
        get_embeddings=get_embeddings,
        keep_stranger_features=keep_stranger_features,
    ).to_json()


@app.post("/predict_file")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    file_path = f"/tmp/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(contents)
    res = model.predict(file_path)
    if isinstance(res, List):
        return [df.to_json() for df in res]
    return res.to_json()


@app.post("/invoke")
async def invoke(request: Request):
    data = await request.json()
    text = [i[1] for i in data["data"]]
    if len(data['data']) > 0 and len(data['data']) > 1:
        output_level = data["data"][0][2]
    else:
        output_level = 'document'

    prediction = model.predict(
        text,
        output_level=output_level,
        positions=False,
        metadata=False,
        drop_irrelevant_cols=False,
        get_embeddings=False,
        keep_stranger_features=True,
    ).to_json(orient="table")
    json_content = json.loads(prediction)
    response = [[i["index"], i] for i in json_content["data"]]
    return JSONResponse(content={"data": response})


@app.get("/healthcheck")
def readiness_probe():
    return "I'm ready!"


@app.get("/ping")
def ping():
    return "I'm ready!"
