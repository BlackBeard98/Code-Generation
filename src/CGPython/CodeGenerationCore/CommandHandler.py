from typing import Generic, TypeVar
#from .CodeGenerationEngine import CodeGenEngine
from abc import ABCMeta , abstractclassmethod, abstractmethod

T = TypeVar("T")

class CommandHandler(Generic[T]): 
# metaclass=ABCMeta):

    @property
    #@abstractmethod
    def Command(self)->T:
        pass

    @classmethod
    #@abstractmethod
    def CommandType(cls):
        pass

    #@abstractmethod
    def ProcessTarget(self, target,engine):
        pass