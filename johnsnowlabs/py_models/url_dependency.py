import shutil
import urllib.request
from typing import Union, Any
from urllib.request import urlopen

import requests

from johnsnowlabs.utils.enums import JvmHardwareTarget, PyInstallTypes, ProductName
from johnsnowlabs.abstract_base.pydantic_model import WritableBaseModel
from johnsnowlabs.utils.enums import SparkVersion
from johnsnowlabs.py_models.lib_version import LibVersion


class UrlDependency(WritableBaseModel):
    """Representation of a URL"""
    url: str
    dependency_type: Union[JvmHardwareTarget, PyInstallTypes]
    spark_version: SparkVersion
    dependency_version: LibVersion
    file_name: str
    product_name: ProductName

    def __init__(self, **data: Any):
        super().__init__(**data)
        self.file_name = self.url.split('/')[-1]
    def update_url(self, new_url):
        self.url = new_url

    def validate(self):
        # Try GET on the URL and see if its valid/reachable
        return requests.head(self.url).status_code == 200

    @staticmethod
    def internet_on():
        try:
            return True if urlopen('https://www.google.com/', timeout=10) else False
        except:
            return False

    def download_url(self, save_path, name_print_prefix: str = '', keep_default_file_name=True):
        if not UrlDependency.internet_on():
            print(f'Warning! It looks like there is no active internet connection on this machine')
            print(f'Trying to continue but might run into problems...')

        if not self.validate():
            raise ValueError(f"Trying to download Invalid URL! {self.url}")
        if keep_default_file_name:
            self.file_name = self.url.split('/')[-1]
        save_path = save_path + '/' + self.file_name

        print(f'Downloading {name_print_prefix} {self.file_name}')
        # Download the file from `url` and save it locally under `file_name`:
        with urllib.request.urlopen(self.url) as response, open(save_path, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
