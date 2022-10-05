from colorama import Fore
from johnsnowlabs.auto_install.softwares import AbstractSoftwareProduct


def log_outdated_lib(product: AbstractSoftwareProduct, installed_version):
    print(Fore.LIGHTRED_EX +
          f'🚨 Your {product.name} is outdated, installed=={installed_version} but latest version=={product.latest_version.as_str()}')

    print(f'You can run {Fore.LIGHTGREEN_EX} jsl.install() {Fore.RESET}to update {product.name}')
