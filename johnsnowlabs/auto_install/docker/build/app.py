import os
import sys
from enum import Enum
from typing import List

from fastapi import FastAPI

from johnsnowlabs import *

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
