import json
import os

from configuration_loader.loaders.base import Base


class JsonLoader(Base):

    def __init__(self, json_files, optional=True):
        self.__json_files = json_files
        self.__optional = optional

    def load(self):
        jsons = []
        for json_file in self.__json_files:
            if os.path.isfile(json_file) and not self.__optional:
                with open(json_file) as f:
                    jsons.append(json.load(f))
        return jsons
