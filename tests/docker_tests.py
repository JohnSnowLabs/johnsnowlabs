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

visual_model_to_data = {
    "pdf2text": "https://raw.githubusercontent.com/JohnSnowLabs/nlu/master/tests/datasets/ocr/pdf/haiku.pdf",
    "doc2text": "https://raw.githubusercontent.com/JohnSnowLabs/nlu/master/tests/datasets/ocr/docx/resume_001.docx",
    "img2text": "https://raw.githubusercontent.com/JohnSnowLabs/nlu/master/tests/datasets/ocr/images/haiku.png",
    "en.classify_image.convnext.tiny": "https://raw.githubusercontent.com/JohnSnowLabs/nlu/master/tests/datasets/ocr/images/teapot.jpg",
    "pdf2table": "https://raw.githubusercontent.com/JohnSnowLabs/nlu/master/tests/datasets/ocr/table_pdf_highlightable_text/data.pdf",
    "doc2table": "https://raw.githubusercontent.com/JohnSnowLabs/nlu/master/tests/datasets/ocr/docx_with_table/doc2.docx",
    "ppt2table": "https://raw.githubusercontent.com/JohnSnowLabs/nlu/master/tests/datasets/ocr/table_PPT/54111.ppt", }

def check_build_serve_query(nlu_ref, port, json_license_path=None, destroy_container=True, destroy_image=True,
                            visual=False, file_url=None):
    # build if missing
    container_name = f"{nlu_ref}_container"
    image_name = f"{nlu_ref}_img"

    nlp.build_image(
        nlu_ref,
        f"{nlu_ref}_img",
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


def test_docker():
    print(is_docker_installed())


def test_build_image():
    nlp.build_image(rebuild=True, use_cache=False, preloaded_model="tokenize")
    nlp.build_image(rebuild=True, use_cache=True, preloaded_model="tokenize")
    _destroy_image()


def test_serve_container_open_source():
    nlu_ref = "tokenize"
    port = 8541
    check_build_serve_query(nlu_ref, port, json_license_path=None)


def test_serve_container_medical():
    nlu_ref = "en.med_ner.cancer_genetics.pipeline"
    port = 8549
    p = '/home/ckl/Documents/freelance/jsl/endpoints/endpoints/creds/license_airgap.json'
    check_build_serve_query(nlu_ref, port, json_license_path=p)


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


def test_invoke():
    data = ['First piece of text', 'second piece of text. With two sentences']
    print(send_invoke(8000, data, 'document'))
    print(send_invoke(8000, data, 'sentence'))
    print(send_invoke(8000, data, 'token'))


@pytest.mark.parametrize("model,url", list(visual_model_to_data.items()))
def test_serve_and_query_container_ocr(model, url):
    # pdf2text, iamg2 text ok! doc2text wierd output?
    #x2table crash. classifyimage crash!
    port = 8541
    p = '/home/ckl/Documents/freelance/jsl/endpoints/endpoints/creds/license_airgap.json'
    print(f'{"#" * 50} Testing Model={model} for data={url} {"#" * 50}')
    check_build_serve_query(
        model,
        port,
        file_url=url,
        json_license_path=p,
        visual=True, )


def test_serve_container_open_source():
    nlu_ref = "tokenize"
    port = 8513
    check_build_serve_query(nlu_ref, port, None, False, False)


def test_query_server():
    port = 8548  # tokenizerz
    port = 8549  # en.med_ner.cancer_genetics.pipeline
    # Send request to the container
    check_local_endpoint_health(port)


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
