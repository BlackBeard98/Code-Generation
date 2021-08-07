from abc import ABC, abstractmethod

class CommandHandler(ABC):

    @property
    @abstractmethod
    def Command(self):
        pass

    @abstractmethod
    def ProcessTarget(self, target,engine):
        pass