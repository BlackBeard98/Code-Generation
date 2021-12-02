import sys
sys.path.append("..")
from CGPython import CodeGenerationTransformer
from CGPython.Commands import ModifyMethodCommand
from ast import ClassDef, FunctionDef


class LogTransformer(CodeGenerationTransformer):
    def Transform(self):
        def func(cmd:ModifyMethodCommand):
            cmd.DecoratedBy("excepcion",None)
        self.Engine.Select(ClassDef()).Select(FunctionDef()).Execute(func)