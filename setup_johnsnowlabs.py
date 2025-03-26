from codecs import open
from os import path

from setuptools import find_packages, setup

import johnsnowlabs.settings

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

REQUIRED_PKGS = [
    f"pyspark=={johnsnowlabs.settings.raw_version_pyspark}",
    f"spark-nlp=={johnsnowlabs.settings.raw_version_nlp}",
    f"nlu=={johnsnowlabs.settings.raw_version_nlu}",
    f"spark-nlp-display=={johnsnowlabs.settings.raw_version_nlp_display}",
    "numpy",
    "dataclasses",
    "requests",
    "databricks-api",
    f"pydantic>={johnsnowlabs.settings.raw_version_pydantic}",
    "colorama",
    "boto3",
]

setup(
    version=johnsnowlabs.settings.raw_version_jsl_lib,
    name="johnsnowlabs",
    description="The John Snow Labs Library gives you access to all of John Snow Labs Enterprise And Open Source products in an easy and simple manner. Access 10000+ state-of-the-art NLP and OCR models for "
                "Finance, Legal and Medical domains. Easily scalable to Spark Cluster ",
    long_description=long_description,
    install_requires=REQUIRED_PKGS,
    long_description_content_type="text/markdown",
    url="https://www.johnsnowlabs.com/",
    author="John Snow Labs",
    author_email="christian@johnsnowlabs.com",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: Apache Software License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="Spark NLP OCR Finance Legal Medical John Snow Labs  ",
    packages=find_packages(exclude=["test*", "tmp*"]),  # exclude=['test']
    include_package_data=True,
    data_files=[
        ("/johnsnowlabs/auto_install/docker/build",
         ["./johnsnowlabs/auto_install/docker/build/app.py",
          "./johnsnowlabs/auto_install/docker/build/base_dockerfile",
          "./johnsnowlabs/auto_install/docker/build/installer.py"]),
    ],

)
