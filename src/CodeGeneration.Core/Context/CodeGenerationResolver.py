from abc import ABC, abstractclassmethod, abstractmethod

class CodeGenResolver(ABC):
    @abstractmethod
    def BuildContainer():
        pass
    @abstractmethod
    def RegisterEngine(engine):
        pass
    @abstractmethod
    def ResolveCommand():
        pass
    @abstractmethod
    def ResolveCommandHandler(commandBuilder):
        pass