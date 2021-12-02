from ast import *
import os
import sys 
from CodeGenerationCore import CodeGenEngine
from CodeGenerationCore import CodeGenResolver
from .PythonTarget import PythonMultipleTargets , PythonSingleTarget
from .PythonCodeGenerationResolver import PythonGenerationResolver
from .Commands import *
from typing import Generic , TypeVar

T = TypeVar("T")

class Selector(NodeVisitor):
    def __init__(self,tree,i_type):
        self.tree = tree
        self.i_type = i_type
        self.results = []

    def generic_visit(self, node):
        if isinstance(node,self.i_type):
           self.results.append(node)
           return
        return NodeVisitor.generic_visit(self,node)

    def run(self):
        self.visit(self.tree)
        return self.results
    
    def run_descendants(self) :
        for field, value in iter_fields(self.tree):
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, AST):
                        self.visit(item)
            elif isinstance(value, AST):
                self.visit(value)
        return self.results

class PythonCodeGenEngine(CodeGenEngine):
    def __init__(self , resolver:CodeGenResolver) -> None:
        self.project = None
        self.__resolver = resolver
        self.mapper = {}

    @property
    def CodeGenerationResolver(self)-> CodeGenResolver:
        return self.__resolver

    def From(self ,path: str) -> 'PythonCodeGenEngine':
        path = os.path.abspath(path).replace("\\","/")
        if os.path.isfile(path):
            self.project =  [path]
        elif os.path.isdir(path):
            ld = os.listdir(path)
            self.project = [path+"/"+f for f in ld if os.path.isfile(path+"/"+f) and f.split(".")[-1] =="py"]

        return self

    def Select(self,i_type:T)-> PythonMultipleTargets[T]:
        targets = []
        for py in self.project :   
            with open(py,"r") as r:
                tree = None
                if not py in self.mapper:
                    tree = parse(r.read(),type_comments=True)
                    self.mapper[py] = tree
                else:
                    tree = self.mapper[py]
                targets.extend([PythonSingleTarget(node, self, py) for node in Selector(tree,type(i_type)).run()])
        return PythonMultipleTargets(targets, self)


if __name__ == '__main__':
    def func(cmd:ModifyClassCommand,name):
        return (cmd
                   .DecoratedBy("singleton","'casa' + 'carr'" , "5")
                   .DecoratedBy("casa")
                   .InheritsFrom("A")
                   .WithBody(
"""
def __init__(self, a:int):
    self.a = a
""")                

                )
    def func2(cmd:ModifyMethodCommand,name):
        return cmd.DecoratedBy("si").WithName(name+"_soy").WithBody("pass")

           
    temp = PythonCodeGenEngine(PythonGenerationResolver())
    x = (temp.From("src/mod1.py")
             .Select(ClassDef())
             .Select(FunctionDef())
             .Using(lambda x: (x.node.name,"name"))
             .Where(lambda x:x.node.name != "soy")
             .Execute(func2)
        )


    import astor
    a = temp.mapper[os.path.abspath("src/mod1.py").replace("\\","/")]
    
    print(astor.to_source(a))
   
    