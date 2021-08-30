from abc import ABC, ABCMeta, abstractmethod
from PythonCodeGenerationResolver import PythonGenerationResolver
#from Selector import Selector

class CodeGenEngine(metaclass =ABCMeta):
    
    @abstractmethod
    def From(self, path:str) :
        pass

    # @property
    # @abstractmethod
    # def TProject (self):
    #     pass

    # @TProject.setter
    # @abstractmethod
    # def TProject(self , Project):
    #     pass
        
    @property
    @abstractmethod
    def CodeGenerationResolver(self)->PythonGenerationResolver:
        pass

    # @abstractmethod
    # def SelectNew(path:str):
    #     pass

    # @abstractmethod 
    # def GetAllDocumentsPaths():
    #     pass

    # @abstractmethod
    # def GetRootNode (path:str):
    #     pass

    