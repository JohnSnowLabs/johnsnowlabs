import time

import requests

from johnsnowlabs import settings
from johnsnowlabs.auto_install.docker.work_utils import (
    is_docker_installed,
    build_image,
    serve_container,
    run_container_cmd,
    _destroy_container,
    _destroy_image,
)
from johnsnowlabs.utils.py_process import run_cmd_and_check_succ


# https://github.com/JohnSnowLabs/nlp-server/blob/main/nlp_server/routers/licenses.py

def check_local_endpoint_health(port):


    url = f"http://localhost:{port}/predict_batch"

    params = {
        "text": ["Your text that you want to predict with the model goes here",
                 'It can also be a list of strings'],
    }
    response = requests.post(url, params=params, headers={"accept": "application/json"})
    print('BATCH PREDICTION UNPARAMETERIZED:')
    print(response.json())




    params = {
        "text": "Your text that you want to predict with the model goes here",
    }
    url = f"http://localhost:{port}/predict"
    response = requests.get(url, params=params, headers={"accept": "application/json"})
    print('STRING PREDICTION UNPARAMETERIZED:')
    print(response.json())



    params = {
        "text": "Your text that you want to predict with the model goes here",
        "output_level": "document",
        "positions": "false",
        "metadata": "false",
        "drop_irrelevant_cols": "false",
        "get_embeddings": "false",
        "keep_stranger_features": "true",
    }
    response = requests.get(url, params=params, headers={"accept": "application/json"})
    print('STRING PREDICTION PARAMETERIZED:')
    print(response.json())






def check_build_serve_query(nlu_ref, port, json_license_path=None):
    # build if missing
    container_name = f"{nlu_ref}_container"
    image_name = f"{nlu_ref}_img"

    build_image(
        nlu_ref,
        f"{nlu_ref}_img",
        rebuild=True,
        use_cache=False,
        json_license_path=json_license_path
    )
    # Serve container, destroy if already running
    serve_container(
        destroy_container=True,
        image_name=image_name,
        container_name=container_name,
        host_port=port,
    )

    # Wait for spark session start and model loading
    time.sleep(30)
    check_local_endpoint_health(port)

    # Print container logs


    run_cmd_and_check_succ(
        f"docker logs {container_name}",
        shell=True,
        raise_on_fail=False,
        use_code=True,
        log=True,
    )
    # _destroy_container(container_name)
    # _destroy_image(image_name)
def test_docker():
    print(is_docker_installed())


def test_build_image():
    build_image(rebuild=True, use_cache=False, preloaded_model="tokenize")
    build_image(rebuild=True, use_cache=True, preloaded_model="tokenize")
    _destroy_image()


def test_serve_container_medical():
    nlu_ref = "en.med_ner.cancer_genetics.pipeline"
    port = 8549
    check_build_serve_query(nlu_ref, port)


def test_serve_container_ocr():
    nlu_ref = "img2text"
    port = 8549
    container_name = f"{nlu_ref}_container"
    image_name = f"{nlu_ref}_img"

    build_image(
        nlu_ref,
        f"{nlu_ref}_img",
        rebuild=True,
        use_cache=False,
        browser_login=True,
        visual=True
    )
    # Serve container, destroy if already running
    serve_container(
        destroy_container=True,
        image_name=image_name,
        container_name=container_name,
        host_port=port,
    )
def test_serve_container_open_source():
    nlu_ref = "tokenize"
    port = 8548
    check_build_serve_query(nlu_ref, port)


def test_query_server():
    port = 8548 # tokenizerz
    port = 8549 # en.med_ner.cancer_genetics.pipeline
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

