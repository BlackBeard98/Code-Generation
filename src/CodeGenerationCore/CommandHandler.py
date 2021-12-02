from typing import Generic, TypeVar,Type
from .CodeGenerationEngine import CodeGenEngine
from .Command import Command as C
from abc import ABCMeta , abstractclassmethod, abstractmethod

T = TypeVar("T")

class CommandHandler(Generic[T]  , metaclass=ABCMeta):


    @property
    @abstractmethod
    def Command(self)->T:
        pass

    @classmethod
    def CommandType(cls)->Type[C]:
        return cls.__type
    
    @classmethod
    def SetCommandType(cls,__type):
        cls.__type = __type

    @abstractmethod
    def ProcessTarget(self, target,engine):
        pass