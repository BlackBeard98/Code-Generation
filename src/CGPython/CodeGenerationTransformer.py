import abc
from .PythonCodeGenerationEngine import PythonCodeGenEngine
class   CodeGenerationTransformer(metaclass = abc.ABCMeta):
    @property
    def Engine(self) -> PythonCodeGenEngine:
        return self._engine
    @Engine.setter
    def Engine(self,engine:PythonCodeGenEngine) :
        self._engine = engine
    @abc.abstractmethod
    def Transform(self):
        pass