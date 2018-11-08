import json

from configuration_loader.loaders.base import Base


class JsonLoader(Base):

    def __init__(self, json_files):
        self.__json_files = json_files

    def load(self):
        jsons = []
        for json_file in self.__json_files:
            with open(json_file) as f:
                jsons.append(json.load(f))
        return jsons
