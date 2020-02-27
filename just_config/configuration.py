import os
import pathlib
from configparser import ConfigParser


class Configuration:

    LOCAL_CFG_FNAME = os.path.join(pathlib.Path().absolute(), 'default.ini')

    def __init__(self, app_name=None):
        self._cfg_local_parser = None
        self._cfg_home_dir_parser = None
        self._app_name = app_name

    def __getitem__(self, key: str) -> str:
        if os.getenv(key) and os.getenv(key):
            return os.getenv(key)
        elif self._local_configuration_file() and self._local_configuration_file()['DEFAULT'].get(key, None):
            return self._local_configuration_file()['DEFAULT'][key]
        elif self._home_dir_configuration_file() and self._home_dir_configuration_file()['DEFAULT'].get(key, None):
            return self._home_dir_configuration_file()['DEFAULT'][key]

    def _local_configuration_file(self) -> ConfigParser:
        if self._cfg_local_parser:
            return self._cfg_local_parser

        self._cfg_local_parser = _build_cfg_parser(Configuration.LOCAL_CFG_FNAME)
        return self._cfg_local_parser

    def _home_dir_configuration_file(self) -> ConfigParser:
        if self._cfg_home_dir_parser:
            return self._cfg_home_dir_parser

        if not self._app_name:
            return None

        cfg_file_name = os.path.join(pathlib.Path.home(), '.' + self._app_name, 'default.ini')
        self._cfg_home_dir_parser = _build_cfg_parser(cfg_file_name)
        return self._cfg_home_dir_parser


def _build_cfg_parser(file_name: str):
    cfg_parser = ConfigParser()
    cfg_parser.read(file_name)
    return cfg_parser






