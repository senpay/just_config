import os
import pathlib
from configparser import ConfigParser


class Configuration:

    CONFIGURATION_FILE_NAME = os.path.join(pathlib.Path().absolute(), 'default.ini')

    def __init__(self):
        self._cfg_parser = None

    def __getitem__(self, key: str) -> str:
        if os.getenv(key):
            return os.getenv(key)
        elif self._local_configuration_file():
            return self._get_configuration(key)

    def _local_configuration_file(self) -> ConfigParser:
        if self._cfg_parser:
            return self._cfg_parser

        self._cfg_parser = ConfigParser()
        self._cfg_parser.read(Configuration.CONFIGURATION_FILE_NAME)
        return self._cfg_parser

    def _get_configuration(self, key: str):
        return self._cfg_parser['DEFAULT'].get(key, None)






