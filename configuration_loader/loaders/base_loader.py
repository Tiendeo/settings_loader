from abc import abstractmethod


class BaseLoader:
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def re_load(self):
        pass
