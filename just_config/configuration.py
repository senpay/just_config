import os


class Configuration:

    def __getitem__(self, key):
        if os.getenv(key):
            return os.getenv(key)
