from abc import ABCMeta, abstractmethod

class Using(metaclass =ABCMeta):
    
    @abstractmethod
    def Using(self, usingSelector):
        pass

class Where(metaclass =ABCMeta):
    @abstractmethod
    def Where(self, WhereSelector):
        pass

class Get(metaclass =ABCMeta):
    @abstractmethod
    def Get(self, arg):
        pass

class SingleTargeter(metaclass =ABCMeta):
   
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

class SingleTarget(SingleTargeter,Using,Get):
    pass

class MultipleTargeters():
    @abstractmethod
    def Execute(self,comandModifiers):
        pass
class MultipleTargets(MultipleTargeters,Using,Where):
    pass