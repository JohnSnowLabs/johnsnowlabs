import os
import sys
from enum import Enum
from typing import List, Union
import random
import time
import string
from pydantic import BaseModel
import logging
import json

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from johnsnowlabs import nlp

logger = logging.getLogger(__name__)

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

# jars loaded from jsl-home
nlp.start(model_cache_folder="/app/model_cache")
model = nlp.load(path="/app/model/served_model")


class OutputLevel(Enum):
    document = "document"
    relation = "relation"
    chunk = "chunk"
    token = "token"


class InvocationInput(BaseModel):
    text: Union[str, List[str]] = [
        "Your text that you want to predict with the model goes here",
        "More text can go here and will be interpreted as 2nd row",
    ]
    output_level: OutputLevel = OutputLevel.document
    positions: bool = False
    metadata: bool = False
    drop_irrelevant_cols: bool = False
    get_embeddings: bool = False  # true?
    keep_stranger_features: bool = True


app = FastAPI()


@app.middleware("http")
async def log_requests(request: Request, call_next):
    idem = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
    logger.info(f"rid={idem} start request path={request.url.path}")
    logger.debug(f"Headers: {request.headers.items()}")
    start_time = time.time()

    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000
    formatted_process_time = "{0:.2f}".format(process_time)
    logger.info(
        f"rid={idem} completed_in={formatted_process_time}ms status_code={response.status_code}"
    )

    return response


@app.get("/ping")
def endpoint_ping():
    return ""


@app.post("/invocations")
async def invocations(input: InvocationInput):
    prediction = model.predict(
        input.text,
        output_level=input.output_level.value,
        positions=input.positions,
        metadata=input.metadata,
        drop_irrelevant_cols=input.drop_irrelevant_cols,
        get_embeddings=input.get_embeddings,
        keep_stranger_features=input.keep_stranger_features,
    ).to_json()

    return JSONResponse(
        content=json.loads(prediction),
        headers={
            "X-Amzn-Inference-Metering": {
                "Dimension": "inference.count",
                "ConsumedUnits": len(input.text) if type(input.text) is list else 1,
            }
        },
    )


@app.post("/snowflake_invocations")
async def invoke(request: Request):
    data = await request.json()
    text = [i[1] for i in data["data"]]
    prediction = model.predict(
        text,
        output_level="document",
        positions=False,
        metadata=False,
        drop_irrelevant_cols=False,
        get_embeddings=False,
        keep_stranger_features=True,
    ).to_json(orient="table")
    json_content = json.loads(prediction)
    response = [[i["index"], i] for i in json_content["data"]]
    return JSONResponse(content={"data": response})
