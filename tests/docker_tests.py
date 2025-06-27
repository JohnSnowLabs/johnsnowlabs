from johnsnowlabs import medical, nlp
import time
from typing import List

import pytest

from johnsnowlabs import settings, nlp
from johnsnowlabs.auto_install.docker.work_utils import (
    is_docker_installed,
    run_container_cmd,
    _destroy_container,
    _destroy_image,
    check_local_endpoint_health, health_check_ocr_container,

)
from johnsnowlabs.utils.py_process import run_cmd_and_check_succ

import requests
import pandas as pd

license_path = '/home/ckl/Documents/freelance/freelance/johnsnowlabs_MASTER/tests/utilsz/lic_airgap.json'

visual_model_to_data = {
    "pdf2text": "https://raw.githubusercontent.com/JohnSnowLabs/nlu/master/tests/datasets/ocr/pdf/haiku.pdf",
    "doc2text": "https://raw.githubusercontent.com/JohnSnowLabs/nlu/master/tests/datasets/ocr/docx/resume_001.docx",
    "img2text": "https://raw.githubusercontent.com/JohnSnowLabs/nlu/master/tests/datasets/ocr/images/haiku.png",
    "en.classify_image.convnext.tiny": "https://raw.githubusercontent.com/JohnSnowLabs/nlu/master/tests/datasets/ocr/images/teapot.jpg",
    "pdf2table": "https://raw.githubusercontent.com/JohnSnowLabs/nlu/master/tests/datasets/ocr/table_pdf_highlightable_text/data.pdf",
    "doc2table": "https://raw.githubusercontent.com/JohnSnowLabs/nlu/master/tests/datasets/ocr/docx_with_table/doc2.docx",
    "ppt2table": "https://raw.githubusercontent.com/JohnSnowLabs/nlu/master/tests/datasets/ocr/table_PPT/54111.ppt", }


def get_pipe():
    spark = nlp.start()

    # passcode = input('Give new Passcode')
    documentAssembler = nlp.DocumentAssembler() \
        .setInputCol("text") \
        .setOutputCol("document")

    sentenceDetector = nlp.SentenceDetectorDLModel.pretrained("sentence_detector_dl_healthcare", "en",
                                                              "clinical/models") \
        .setInputCols(["document"]) \
        .setOutputCol("sentence")

    tokenizer = nlp.Tokenizer() \
        .setInputCols(["sentence"]) \
        .setOutputCol("token")

    word_embeddings = nlp.WordEmbeddingsModel.pretrained("embeddings_clinical", "en", "clinical/models") \
        .setInputCols(["sentence", "token"]) \
        .setOutputCol("embeddings")

    ner = medical.NerModel.pretrained("ner_jsl", "en", "clinical/models") \
        .setInputCols(["sentence", "token", "embeddings"]) \
        .setOutputCol("ner") \
        .setLabelCasing("upper")

    ner_converter = medical.NerConverter() \
        .setInputCols(["sentence", "token", "ner"]) \
        .setOutputCol("ner_chunk")

    ner_pipeline = nlp.Pipeline(stages=[
        documentAssembler,
        sentenceDetector,
        tokenizer,
        word_embeddings,
        ner,
        ner_converter])

    empty_data = spark.createDataFrame([[""]]).toDF("text")
    ner_model = ner_pipeline.fit(empty_data)
    return ner_model


def check_build_serve_query(pipe_name=None, pipe_lang='en', pipe_bucket=None, port=None, json_license_path=None,
                            destroy_container=True,
                            destroy_image=True,
                            visual=False, file_url=None, custom_pipe=None

                            ):
    # build if missing
    container_name = f"{pipe_name}_container"
    image_name = f"{pipe_name}_img"

    nlp.build_image(
        pipeline_name=pipe_name,
        pipeline_language=pipe_lang,
        pipeline_bucket=pipe_bucket,
        custom_pipeline=custom_pipe,
        image_name=image_name,
        rebuild=True,
        use_cache=False,
        visual=visual,
        json_license_path=json_license_path,
    )
    # Serve container, destroy if already running
    nlp.serve_container(
        destroy_container=True,
        image_name=image_name,
        container_name=container_name,
        host_port=port,
    )

    # Wait for spark session start and model loading
    # Todo need todo exponential backoff because sie models take different time to load
    time.sleep(130)
    if visual:
        if not file_url:
            raise ValueError('file_url not specified but required for visual model')
        health_check_ocr_container(port, file_url)

    else:
        check_local_endpoint_health(port)

    # Print container logs
    run_cmd_and_check_succ(
        f"docker logs {container_name}",
        shell=True,
        raise_on_fail=False,
        use_code=True,
        log=True,
    )
    if destroy_container:
        _destroy_container(container_name)
    if destroy_image:
        _destroy_image(image_name)


def send_invoke(port, data, output_level='document'):
    url = f"http://localhost:{port}/invoke"
    data_to_send = {'data': []}
    if isinstance(data, List):
        for i, text in enumerate(data):
            data_to_send['data'].append([i, text, output_level])
    elif isinstance(data, str):
        data_to_send['data'].append([0, data, output_level])
    else:
        raise ValueError(f'Invalid data type {type(data)} must be string or list of strings')
    response = requests.post(url, json=data_to_send)
    if response.status_code == 200:
        data_list = [item[1] for item in response.json()["data"]]
        df = pd.DataFrame(data_list)

        return df
    else:
        ValueError(f"Failed to get a successful response, status code: {response.status_code}")


def test_docker():
    print(is_docker_installed())


def test_build_image():
    nlp.build_image(rebuild=True, use_cache=False, pipeline_name="movies_sentiment_analysis")
    nlp.build_image(rebuild=True, use_cache=True, pipeline_name="movies_sentiment_analysis")
    _destroy_image()


def test_serve_container_open_source():
    check_build_serve_query(
        pipe_name='lora_ner_pipeline',
        pipe_lang='en',
        pipe_bucket=None,
        port=8513,
        json_license_path=None,
        destroy_container=True,
        visual=False)


def test_serve_container_medical():
    check_build_serve_query(pipe_name='ner_bionlp_pipeline',
                            pipe_lang='en',
                            pipe_bucket='clinical/models',
                            port=8549,
                            json_license_path=license_path)
def test_ocr_pipe():
    check_build_serve_query(pipe_name='pdf_printed_transformer_extraction',
                            pipe_bucket='clinical/ocr',
                            visual=True,
                            file_url = 'https://raw.githubusercontent.com/JohnSnowLabs/nlu/master/tests/datasets/ocr/pdf/haiku.pdf',
                            port=8599,
                            destroy_image=False,
                            json_license_path=license_path)


def test_dicom_deid_pipe():


    check_build_serve_query(pipe_name='dicom_deid_generic_augmented_minimal',
                            pipe_bucket='clinical/ocr',
                            visual=True,
                            file_url = 'https://github.com/JohnSnowLabs/visual-nlp-workshop/raw/refs/heads/master/jupyter/data/dicom/deidentify-medical-1.dcm',
                            port=8599,
                            json_license_path=license_path)

def test_nlu_ocr_pipe():
    nlp.start(visual=True)
    pipe = nlp.load('pdf2text')
    try:
        pipe.predict('')
    except:
        pass
    pipe = pipe.vanilla_transformer_pipe

    check_build_serve_query(pipe_name='ocr_pipe',
                            custom_pipe = pipe,
                            visual=True,
                            file_url = 'https://raw.githubusercontent.com/JohnSnowLabs/nlu/master/tests/datasets/ocr/pdf/haiku.pdf',
                            port=8589,
                            json_license_path=license_path)



def test_invoke():
    data = ["The patient has no cancer in the left leg. Administrating morphium caused a 2 day rash on the neck"]
    print(send_invoke(6645, data, 'document'))
    # print(send_invoke(8000, data, 'sentence'))
    # print(send_invoke(8000, data, 'token'))


@pytest.mark.parametrize("model_nlu_ref,url", list(visual_model_to_data.items()))
def test_serve_and_query_container_ocr(model_nlu_ref, url):
    # pdf2text, iamg2 text ok! doc2text wierd output?
    # x2table crash. classifyimage crash!
    print(f'{"#" * 50} Testing Model={model_nlu_ref} for data={url} {"#" * 50}')
    nlp.start(visual=True)
    pipe = nlp.load(model_nlu_ref)
    try:
        # init pipe, it may fail which is fine but we need it so vanilla_transformer_pipe is set
        # it is the fitted pipe which we deploy as a custom pipe
        pipe.predict('')
    except:
        pass

    pipe = pipe.vanilla_transformer_pipe

    check_build_serve_query(
        # We re-use nlu ref as name so we have unique container names
        pipe_name=model_nlu_ref,
        custom_pipe=pipe,
        port=8541,
        file_url=url,
        json_license_path=license_path,
        visual=True, )


def test_serve_custom_nlp_pipe():
    check_build_serve_query(
        pipe_name='custom_pipe',
        custom_pipe=get_pipe(),
        port=8423,
        json_license_path=None,
        visual=False)


def test_run_container():
    run_container_cmd(destroy_container=True)
    # Command to execute the test script inside the container
    script = """from johnsnowlabs import nlp; nlp.start(); print(nlp.load('med_ner').predict('Hello World'))"""
    test_script_cmd = (
        f'docker exec {settings.docker_container_name} python3 -c "{script}"'
    )
    run_cmd_and_check_succ(
        [test_script_cmd], shell=True, raise_on_fail=True, use_code=True
    )
    _destroy_container()
