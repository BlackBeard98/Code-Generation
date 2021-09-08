from abc import ABC, abstractmethod

class Using(ABC):
    
    @abstractmethod
    def Using(self, usingSelector):
        pass

class Where(ABC):
    @abstractmethod
    def Where(self, WhereSelector):
        pass



class TargetGet(ABC):
    @abstractmethod
    def Get(self , key , value):
        pass

class SingleTargeter(ABC):
   
    @property
    @abstractmethod
    def Node(self):
        pass
  

    @property
    @abstractmethod
    def DocumentPath(self):
        pass
    
    @abstractmethod
    def Execute(self,comandModifiers):
        pass

class Target(SingleTargeter,Using,Where,TargetGet):
    pass