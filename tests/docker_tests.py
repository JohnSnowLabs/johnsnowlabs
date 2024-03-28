import base64
import time

import requests

from johnsnowlabs import settings, nlp
from johnsnowlabs.auto_install.docker.work_utils import (
    is_docker_installed,
    run_container_cmd,
    _destroy_container,
    _destroy_image,
    check_local_endpoint_health,

)
from johnsnowlabs.utils.py_process import run_cmd_and_check_succ

def serialize(file_path):
    try:
        with open(file_path, 'rb') as file:
            binary_content = file.read()
        base64_encoded_content = base64.b64encode(binary_content)
        return base64_encoded_content.decode()  # Convert bytes to string for easy handling
    except Exception as e:
        print(f"Error serializing file: {e}")
        return None

from pathlib import Path

def send_file_to_server(file_path, url):
    """Send a file to the server using multipart/form-data."""
    try:
        files = {'file': (Path(file_path).name, open(file_path, 'rb'), 'image/png')}
        response = requests.post(url, files=files)
        return response.json()  # Assuming your server responds with JSON
    except Exception as e:
        print(f"Error sending file to server: {e}")
        return None

# https://github.com/JohnSnowLabs/nlp-server/blob/main/nlp_server/routers/licenses.py

def test_quick():
    port = 8548
    params = {
        "text": ["Your text that you want to predict with the model goes here",
                 'It can also be a list of strings'],
    }
    url = f"http://localhost:{port}/invoke"
    response = requests.post(url, params=params, headers={"accept": "application/json"})
    print('INVOKE:')
    print(response.json())




def check_build_serve_query(nlu_ref, port, json_license_path=None, destroy_container=True, destroy_image=True):
    # build if missing
    container_name = f"{nlu_ref}_container"
    image_name = f"{nlu_ref}_img"

    nlp.build_image(
        nlu_ref,
        f"{nlu_ref}_img",
        rebuild=True,
        use_cache=False,
        json_license_path=json_license_path
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


def test_serve_container_ocr():
    nlu_ref = "img2text"
    port = 8541
    container_name = f"{nlu_ref}_container"
    image_name = f"{nlu_ref}_img"

    nlp.build_image(
        nlu_ref,
        f"{nlu_ref}_img",
        rebuild=True,
        use_cache=False,
        visual=True
    )
    # Serve container, destroy if already running
    nlp.serve_container(
        destroy_container=True,
        image_name=image_name,
        container_name=container_name,
        host_port=port,
    )



def test_ocr_container():
    nlu_ref = "img2text"
    port = 8541

    # b = serialize()
    file = '/media/ckl/dump1/Documents/freelance/MOST_RECENT/jsl/nlu/nlu4realgit3/tests/datasets/ocr/images/haiku.png'
    container_name = f"{nlu_ref}_container"
    url = f"http://localhost:{port}/predict_file"
    response = send_file_to_server(file,url)
    # response = requests.post(url, params=params, headers={"accept": "application/json"})
    print(response)



def test_serve_container_open_source():
    nlu_ref = "tokenize"
    port = 8548
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
