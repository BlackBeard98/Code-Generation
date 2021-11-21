from ..CGPython import CodeGenerationTransformer
from ..CGPython.Commands import ModifyMethodCommand
from ast import ClassDef, FunctionDef, Name


class TrueStaticTransformer(CodeGenerationTransformer):
    def Transform(self):
        def func(cmd:ModifyMethodCommand, name:str):
            return cmd.DecoratedBy("staticmethod").RemoveArg(name)
        (self.Engine.Select(ClassDef())
                    .Select(FunctionDef())
                    .Using(lambda x: (x.node.args.args[0].arg,"name"))
                    .Where(lambda x:x.node.name[:2]!="__")
                    .Where(lambda x:not "staticmethod" in x.node.decorator_list)
                    .Where(lambda x:not "classmethod" in x.node.decorator_list)
                    .Where(lambda x: len(x.Select(Name())
                                          .Where(lambda x: x.parent.Get('name') == x.node.id).targets)==0)
                    .Execute(func)
                                      )
                          