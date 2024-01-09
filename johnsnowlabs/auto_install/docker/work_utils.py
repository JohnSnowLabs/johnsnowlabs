import os
import subprocess
from typing import Optional

from johnsnowlabs import settings
from johnsnowlabs.py_models.jsl_secrets import JslSecrets
from johnsnowlabs.utils.enums import JvmHardwareTarget
from johnsnowlabs.utils.env_utils import get_folder_of_func
from johnsnowlabs.utils.py_process import run_cmd_and_check_succ


def check_image_exist(image_name: str) -> bool:
    cmd = f"docker image inspect {image_name}"
    return run_cmd_and_check_succ(
        [cmd], shell=True, raise_on_fail=False, use_code=True, log=False
    )


def check_container_exist(container_name: str) -> bool:
    cmd = f"docker container inspect {container_name}"
    return run_cmd_and_check_succ(
        [cmd], shell=True, raise_on_fail=False, use_code=True, log=False
    )


def _destroy_container(container_name: str = None):
    container_name = (
        settings.docker_container_name if container_name is None else container_name
    )

    if check_container_exist(container_name):
        stop_cmd = f"docker container stop {container_name}"
        rm_cmd = f"docker container rm -f {container_name}"
        run_cmd_and_check_succ(
            [stop_cmd], shell=True, raise_on_fail=False, use_code=True
        )
        run_cmd_and_check_succ([rm_cmd], shell=True, raise_on_fail=False, use_code=True)
        print(f"Container '{container_name}' destroyed.")
    else:
        print(f"Container '{container_name}' does not exist.")


def _destroy_image(image_name: str = None):
    image_name = settings.docker_image_name if image_name is None else image_name
    if check_image_exist(image_name):
        rm_cmd = f"docker image rm -f {image_name}"
        run_cmd_and_check_succ([rm_cmd], shell=True, raise_on_fail=False, use_code=True)
        print(f"Image '{image_name}' destroyed.")
    else:
        print(f"Image '{image_name}' does not exist.")


def is_docker_installed():
    try:
        # Command to check Docker version
        command = "asd asd docker dasdasd --version"

        # Execute the command
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        # Decode the output
        output = result.stdout.decode().strip()

        if "Docker" in output:
            return True
        else:
            return False

    except subprocess.CalledProcessError as e:
        return False


def generate_dockerfile(
    # Install parameters
    model: str,  # nlu ref, nlp_ref or lcoally stored model
    json_license_path: Optional[str] = None,
    access_token: Optional[str] = None,
    spark_nlp: bool = True,
    visual: bool = False,
    nlp: bool = True,
    hardware_platform: str = JvmHardwareTarget.cpu.value,
):
    """
    Generate a Dockerfile for a specific model and configuration.

    :param model: Reference to the model to be used.
    :param json_license_path: Path to the JSON license file.
    :param access_token: Access token for authentication.
    :param spark_nlp: Flag to include Spark NLP.
    :param visual: Flag to include visual features.
    :param nlp: Flag to include NLP features.
    :param hardware_platform: Target hardware platform (e.g., 'cpu').
    """
    if not model:
        raise Exception("model may not me None", model)

    build_folder = os.path.join(get_folder_of_func(_destroy_container), "build")
    base_docker_file_path = os.path.join(build_folder, "base_dockerfile")
    generated_docker_file_path = os.path.join(build_folder, "generated_dockerfile")
    secrets: JslSecrets = JslSecrets.build_or_try_find_secrets(
        secrets_file=json_license_path,
        access_token=access_token,
    )

    provided_license = None
    if secrets.OCR_LICENSE:
        provided_license = secrets.OCR_LICENSE

    elif secrets.HC_LICENSE:
        provided_license = secrets.HC_LICENSE

    env_vars = [
        f'ENV HARDWARE_TARGET="{JvmHardwareTarget(hardware_platform).value}"',
        f'ENV MODEL_TO_LOAD="{model}"',
    ]

    if provided_license:
        env_vars.append(f'ENV JOHNSNOWLABS_LICENSE="{provided_license}"')

    if provided_license:
        env_vars.append(f'ENV JOHNSNOWLABS_LICENSE="{provided_license}"')
    if secrets.HC_SECRET and nlp:
        env_vars.append(f'ENV MEDICAL_SECRET="{secrets.HC_SECRET}"')
    if secrets.OCR_SECRET and visual:
        env_vars.append(f'ENV VISUAL_SECRET="{secrets.OCR_SECRET}"')
    if secrets.AWS_ACCESS_KEY_ID:
        env_vars.append(
            f'ENV JOHNSNOWLABS_AWS_ACCESS_KEY_ID="{secrets.AWS_ACCESS_KEY_ID}"'
        )
    if secrets.AWS_SECRET_ACCESS_KEY:
        env_vars.append(
            f'ENV JOHNSNOWLABS_AWS_SECRET_ACCESS_KEY="{secrets.AWS_SECRET_ACCESS_KEY}"'
        )

    with open(base_docker_file_path, "r", encoding="utf-8") as file:
        docker_code = file.read()

    docker_code = insert_strings(3, env_vars, docker_code)

    with open(generated_docker_file_path, "w", encoding="utf-8") as file:
        file.write(docker_code)


def insert_strings(index, inserts, start_string):
    """
    Insert multiple strings into a starting string at a specified index.

    :param index: Position in the starting string where the inserts begin.
    :param inserts: List of strings to insert.
    :param start_string: The initial string into which the inserts are made.
    :return: Modified string with inserts.
    """

    lines = start_string.split("\n")
    for string in inserts:
        lines.insert(index + 1, string)
        index += 1
    return "\n".join(lines)


def build_image(
    preloaded_model: str,  # nlu ref, nlp_ref or lcoally stored model
    image_name=None,
    destroy_image=False,
    use_cache=True,
    # Install parameters
    json_license_path: Optional[str] = None,
    access_token: Optional[str] = None,
    spark_nlp: bool = True,
    visual: bool = False,
    nlp: bool = True,
    hardware_platform: str = JvmHardwareTarget.cpu.value,
):
    """
    Build a Docker image with specified parameters.

    :param preloaded_model: Reference to the preloaded model.
    :param image_name: Name of the Docker image. If None, uses default from settings.
    :param destroy_image: Flag to destroy the existing image before building a new one.
    :param use_cache: Flag to use cache during the build.
    :param json_license_path: Path to the JSON license file.
    :param access_token: Access token for authentication.
    :param spark_nlp: Flag to include Spark NLP.
    :param visual: Flag to include visual features.
    :param nlp: Flag to include NLP features.
    :param hardware_platform: Target hardware platform (e.g., 'cpu').
    """
    image_name = settings.docker_image_name if image_name is None else image_name
    if destroy_image:
        _destroy_image(image_name)

    build_folder = os.path.join(get_folder_of_func(_destroy_container), "build")
    cmd = f"cd {build_folder} && docker build -f generated_dockerfile . -t {image_name}"
    if not use_cache:
        cmd += " --no-cache"

    generate_dockerfile(
        model=preloaded_model,
        json_license_path=json_license_path,
        access_token=access_token,
        spark_nlp=spark_nlp,
        visual=visual,
        nlp=nlp,
        hardware_platform=hardware_platform,
    )
    run_cmd_and_check_succ([cmd], shell=True, raise_on_fail=True, use_code=True)


def run_container_cmd(container_name=None, image_name=None, destroy_container=False):
    """
    Run a command in a Docker container.

    :param container_name: Name of the Docker container. If None, uses default from settings.
    :param image_name: Name of the Docker image. If None, uses default from settings.
    :param destroy_container: Flag to destroy the container before running the command.
    """

    image_name = settings.docker_image_name if image_name is None else image_name
    container_name = (
        settings.docker_container_name if container_name is None else container_name
    )
    if destroy_container:
        _destroy_container(container_name)

    # Command to run the container, add tail -f /dev/null to keep the container running
    cmd = f"docker run --name {container_name} -d {image_name} tail -f /dev/null"

    run_cmd_and_check_succ([cmd], shell=True, raise_on_fail=True, use_code=True)


def serve_container(
    container_name=None, image_name=None, destroy_container=False, host_port=8000
):
    """
    Serve a Docker container on a specified host port.

    :param container_name: Name of the Docker container. If None, uses default from settings.
    :param image_name: Name of the Docker image. If None, uses default from settings.
    :param destroy_container: Flag to destroy the container before serving.
    :param host_port: Host port to bind the container's service port.
    """
    image_name = settings.docker_image_name if image_name is None else image_name
    container_name = (
        settings.docker_container_name if container_name is None else container_name
    )

    if destroy_container:
        _destroy_container(container_name)

    # Command to run the container
    # Map the container's port 80 to the host's specified port
    cmd = f"docker run --name {container_name} -p {host_port}:80 -d {image_name}"

    run_cmd_and_check_succ([cmd], shell=True, raise_on_fail=True, use_code=True)
