from abc import abstractmethod


class Base(object):

    @abstractmethod
    def parse(self, key):
        pass
