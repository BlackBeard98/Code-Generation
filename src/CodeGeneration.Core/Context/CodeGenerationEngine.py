from abc import ABC, abstractmethod

class CodeGenResolver(ABC):
    
    @property
    @abstractmethod
    def TProject (self):
        pass

    @TProject.setter
    @abstractmethod
    def TProject(self , Project):
        pass
        
    @property
    @abstractmethod
    def CodeGenerationResolver(self):
        return self._CodeGenerationResolver

    @abstractmethod
    def SelectNew(path:str):
        pass

    @abstractmethod 
    def GetAllDocumentsPaths():
        pass

    @abstractmethod
    def GetRootNode (path:str):
        pass

   