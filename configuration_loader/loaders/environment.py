import os
from functools import reduce

from configuration_loader.loaders.base import Base


class EnvironmentLoader(Base):

    __SPLIT_STRING_KEY = '__'

    def __init__(self, split_string_key=None):
        if split_string_key:
            self.__split_string_key = split_string_key
        else:
            self.__split_string_key = self.__SPLIT_STRING_KEY

    def load(self):
        configs = {}
        for key, value in os.environ.items():
                configs[key] = value
        return self.__split_keys(configs)

    def __split_keys(self, config):
        configs = []
        for key, value in config.items():
            configs.append(reduce(lambda res, cur: {cur: res}, reversed(key.split(self.__split_string_key)), value))
        return configs
