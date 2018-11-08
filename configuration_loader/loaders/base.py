from abc import abstractmethod


class Base(object):

    @abstractmethod
    def load(self):
        """Return list of dictionaries"""
        pass

