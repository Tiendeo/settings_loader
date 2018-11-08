import inflection

from configuration_loader.parsers.base import Base


class DefaultParser(Base):
    """SnakeCase"""
    def parse(self, key):
        return inflection.underscore(key)
