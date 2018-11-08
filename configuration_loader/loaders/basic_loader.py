from functools import reduce

from configuration_loader.loaders.base_loader import BaseLoader


class BasicLoader(BaseLoader):
    def __init__(self, property_name_parsers, merger, loaders):
        self.__property_name_parsers = property_name_parsers
        self.__merger = merger
        self.__loaders = loaders
        self.configs = {}

    def load(self):
        configs = []
        for loader in self.__loaders:
            configs += self.__rename_properties(loader.load())

        self.configs = self.__merge(configs)

    def re_load(self):
        self.load()

    def __rename_properties(self, dictionary):
        if isinstance(dictionary, dict):
            return {self.__rename_property(k): self.__rename_properties(v) for k, v in dictionary.items()}
        elif isinstance(dictionary, (list, set, tuple)):
            t = type(dictionary)
            return t(self.__rename_properties(o) for o in dictionary)
        else:
            return dictionary

    def __merge(self, dictionaries):
        return reduce(self.__merger.merge, dictionaries)

    def __rename_property(self, property_name):
        parsed_property_name = property_name
        for parser in self.__property_name_parsers:
            parsed_property_name = parser.parse(parsed_property_name)
        return parsed_property_name

    def __rename_configs_properties(self, configs):
        return [self.__rename_properties(config) for config in configs]

