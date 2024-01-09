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

from johnsnowlabs import nlp

# https://github.com/JohnSnowLabs/nlp-server/blob/main/nlp_server/routers/licenses.py


def test_docker():
    print(is_docker_installed())


def test_build_image():
    nlp.build_image(destroy_image=True, use_cache=False)
    build_image(destroy_image=True, use_cache=True)
    _destroy_image()


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


def test_deploy_ecr():
    build_image("tokenize", destroy_image=False, use_cache=True)


def test_serve_container():
    # build if missing
    nlu_ref = "tokenize"
    container_name = f"{nlu_ref}_container"
    image_name = f"{nlu_ref}_img"
    port = 8548

    build_image(
        nlu_ref,
        f"{nlu_ref}_img",
        destroy_image=True,
        use_cache=False,
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

    # Send request to the container
    url = f"http://localhost:{port}/predict"
    params = {
        "text": "Your text that you want to predict with the model goes here",
        "output_level": "document",
        "positions": "false",
        "metadata": "false",
        "drop_irrelevant_cols": "false",
        "get_embeddings": "false",
        "keep_stranger_features": "true",
    }
    headers = {"accept": "application/json"}

    response = requests.get(url, params=params, headers=headers)
    print(response.json())

    # Print container logs
    run_cmd_and_check_succ(
        f"docker logs {container_name}",
        shell=True,
        raise_on_fail=False,
        use_code=True,
        log=True,
    )
    # _destroy_container(container_name)
    _destroy_image(image_name)
