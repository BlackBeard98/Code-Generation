from abc import ABC, abstractmethod

class Using(ABC):
    
    @abstractmethod
    def Using(self, usingSelector, key):
        pass

class Where(ABC):
    @abstractmethod
    def Where(self, WhereSelector):
        pass

class AsMultiple(ABC):
    @abstractmethod
    def ASMultiple(self):
        pass

class TargetGet(ABC):
    @abstractmethod
    def Get(self , key , value):
        pass

class SingleTargeter(ABC):
   
    @property
    @abstractmethod
    def Id(self):
        pass
   
    @property
    @abstractmethod
    def Node(self):
        pass
    
    @property
    @abstractmethod
    def SemanticSymbol(self):
        pass

    @property
    @abstractmethod
    def DocumentPath(self):
        pass
    
    @abstractmethod
    def Execute(comandModifiers):
        pass