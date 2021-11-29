import sys
sys.path.append("..")
from CGPython import CodeGenerationTransformer
from CGPython.Commands import ModifyMethodCommand
from ast import ClassDef, FunctionDef, Name

class TrueStaticTransformer(CodeGenerationTransformer):
	def Transform(self):
		def func(cmd:ModifyMethodCommand, name:str):
			return cmd.DecoratedBy("staticmethod").RemoveArg(name)
			
		(self.Engine.Select(ClassDef())
				    .Select(FunctionDef())
			        .Using(lambda x: ([dec.id for dec in x.node.decorator_list if isinstance(dec,Name)],"decorators"))
		            .Where(lambda x:x.node.name[:2]!="__")
		            .Where(lambda x:not "staticmethod" in x.Get("decorators"))
                    .Where(lambda x:not "classmethod" in  x.Get("decorators"))
					.Where(lambda x:len(x.node.args.args)>0)
					.Using(lambda x: (x.node.args.args[0].arg,"name"))
                    .Where(lambda x: len(x.Select(Name())
				                          .Where(lambda x: x.parent.Get('name') == x.node.id).targets)==0)
		            .Execute(func)
		)