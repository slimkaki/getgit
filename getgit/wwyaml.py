"""wwyaml - work with yaml"""

from yaml import load, FullLoader, dump
from pathlib import Path
from os import makedirs
import os.path
from sys import exit

from .constants import CONFIG_DIR


def create_file(path: Path = CONFIG_DIR, filename: str = 'config.yaml'):
    """Create file in define path"""
    if not os.path.isdir(path):
        makedirs(path)
    with open(path / filename, "w") as f:
        f.write('service:\nnickname:')


def load_data(path: Path = CONFIG_DIR, filename: str = 'config.yaml') -> dict | None:
    """Return data from config.yaml"""
    try:
        with open(path / filename) as f:
            return load(f, Loader=FullLoader)
    except FileNotFoundError:
        create_file()


#NOTE: use union data for service, nickname and port
def put_data(service, nickname, path: Path = CONFIG_DIR, port: str = '',
        filename: str = 'config.yaml'):
    """Put service(github, gitlab, ...) and nickname in config.yaml"""
    with open(path / filename, "w") as f:
        dump({'service': service, 'nickname': nickname, 'port': port}, f)


def check_filling_of_data(path: Path = CONFIG_DIR, filename: str = 'config.yaml'):
    """
    Return 1 if service and nickname in config.yaml exist.  
    Otherwise return 0.
    """
    data = load_data(path)
    try:
        fields = ('service', 'nickname')
        return all(map(lambda x: x in data.keys(), fields)) and None not in (data[field] for field in fields)
    except TypeError:
        print(f"Config file was add in {CONFIG_DIR / filename}")
        exit()
