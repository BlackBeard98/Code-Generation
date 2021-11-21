from abc import ABCMeta, abstractclassmethod, abstractmethod
#from .CommandHandler import CommandHandler
class CodeGenResolver(metaclass =ABCMeta):
    @abstractmethod
    def Build():
        pass
    @abstractmethod
    def RegisterEngine(engine):
        pass
    @abstractmethod
    def ResolveCommand():
        pass
    @abstractmethod
    def ResolveCommandHandler(commandBuilder): #->CommandHandler:
        pass