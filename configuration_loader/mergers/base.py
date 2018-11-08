from abc import abstractmethod


class Base(object):

    @abstractmethod
    def merge(self, dict_a, dict_b, path=None):
        """"
            Merges b into a
        """
        pass