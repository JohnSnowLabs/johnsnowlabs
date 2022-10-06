from typing import Union

from colorama import Fore
from johnsnowlabs.auto_install.softwares import AbstractSoftwareProduct


def log_outdated_lib(product: AbstractSoftwareProduct, installed_version):
    print(Fore.LIGHTRED_EX +
          f'🚨 Your {product.name} is outdated, installed=={installed_version} but latest version=={product.latest_version.as_str()}')

    print(f'You can run {Fore.LIGHTGREEN_EX} jsl.install() {Fore.RESET}to update {product.name}')


def log_broken_lib(product: Union[AbstractSoftwareProduct, str]):
    if hasattr(product, 'name'):
        product = product.name
    print(Fore.LIGHTRED_EX +
          f'🚨 {product} installation seems broken{Fore.RESET}, there was an exception while importing it. It will not be available on the jsl.xx module')
    print(
        f'You can run {Fore.LIGHTGREEN_EX} jsl.install(refresh_install=True, force_browser=True) {Fore.RESET} to re-install latest version. ')
