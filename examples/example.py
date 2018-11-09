from pprint import pprint

from configuration_loader.loaders.basic_loader import BasicLoader
from configuration_loader.loaders.environment import EnvironmentLoader
from configuration_loader.loaders.json import JsonLoader
from configuration_loader.parsers.default import DefaultParser
from configuration_loader.mergers.default import DefaultMerger


def main():
    json_loader = JsonLoader(["configs.json"])
    env_loader = EnvironmentLoader()

    merger = DefaultMerger()

    parsers = [DefaultParser()]
    pprint(json_loader.load())
    loader = BasicLoader(parsers, merger, [env_loader, json_loader])
    loader.load()
    pprint(loader.configs)


if __name__ == '__main__':
    main()
