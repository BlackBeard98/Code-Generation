import abc
from .PythonCodeGenerationEngine import PythonCodeGenEngine
class   CodeGenerationTransformer(metaclass = abc.ABCMeta):
    @property
    def Engine(self) -> PythonCodeGenEngine:
        pass

    @abc.abstractmethod
    def Transform(self):
        pass