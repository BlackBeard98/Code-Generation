from abc import ABCMeta, abstractmethod

class Selector(metaclass =ABCMeta):

    @abstractmethod
    def Select(self,*args):
        pass