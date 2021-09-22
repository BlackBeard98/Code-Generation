import sys
import unittest
from ast import *
import astor
import os
from CGPython import PythonCodeGenEngine , PythonGenerationResolver
from CGPython.Commands import *


class TestSum(unittest.TestCase):

    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.Engine = PythonCodeGenEngine(PythonGenerationResolver())


    def test_ModifyClass(self):
        def func(cmd:ModifyClassCommand,name):
            return (cmd.DecoratedBy("suma", "5")
                       .DecoratedBy("casa")
                       .InheritsFrom("A")
                       .Append("import ast")
                    )

        (self.Engine.From("src/testcases/ModifyClass/in.py")
                    .Select(ClassDef())
                    .Select(ClassDef())
                    .Using(lambda x: (x.node.name,"name"))
                    .Where(lambda x:x.node.name != "soy")
                    .Execute(func)
        )
        
        a = self.Engine.mapper[os.path.abspath("src/testcases/ModifyClass/in.py").replace("\\","/")]
        s = ""
        with open(os.path.abspath("src/testcases/ModifyClass/out.py"),"r") as f:
            s = f.read()
        self.assertEqual(astor.to_source(a), s, "Should be the same")
    
    def test_ModifyMethod(self):
        def func(cmd:ModifyMethodCommand,name):
            return (cmd.DecoratedBy("Memoize")
                       .WithName(name+"_modified"))

        (self.Engine.From("src/testcases/ModifyMethod/in.py")
                    .Select(ClassDef()).Select(FunctionDef())
                    .Where(lambda x: x.node.name == "fib")
                    .Using(lambda x:(x.node.name,"name"))
                    .Execute(func))
        
        a = self.Engine.mapper[os.path.abspath("src/testcases/ModifyMethod/in.py").replace("\\","/")]
        s = ""
        with open(os.path.abspath("src/testcases/ModifyMethod/out.py"),"r") as f:
            s = f.read()
        self.assertEqual(astor.to_source(a), s, "Should be the same")

    
    def test_CreateClass(self):
        def func(cmd:CreateClassCommand, name:str):
            return (cmd.WithName(name.split("_")[0] + "_generated")
                       .WithBody(
'''
def __init__(self):
    pass
'''
            )
                      .InheritsFrom("NodeVisitor"))

        (self.Engine.From("src/testcases/CreateClass/in.py")
                    .Select(ClassDef()).Select(FunctionDef())
                    .Where(lambda x:"A" in x.node.name)
                    .Using(lambda x: (x.node.name,"name"))
                    .Execute(func))
        
        a = self.Engine.mapper[os.path.abspath("src/testcases/CreateClass/in.py").replace("\\","/")]
        s = ""
        e = astor.to_source(a)
        with open(os.path.abspath("src/testcases/CreateClass/out.py"),"r") as f:
            s = f.read()
        self.assertEqual(astor.to_source(a), s, "Should be the same")



    def test_CreateMethod(self):
        def func(cmd:CreateMethodCommand, name):
            return(cmd.WithArgs("self")
                      .WithArgs("name",'"test"')
                      .WithName(name+"_generated")
                      .WithBody(
'''
print(f"{name}")
'''
            ))
        (self.Engine.From("src/testcases/CreateMethod/in.py")
             .Select(ClassDef())
             .Using(lambda x: (x.node.name,"name"))
             .Execute(func))
        
        a = self.Engine.mapper[os.path.abspath("src/testcases/CreateMethod/in.py").replace("\\","/")]
        s = ""
        e = astor.to_source(a)
        with open(os.path.abspath("src/testcases/CreateMethod/out.py"),"r") as f:
            s = f.read()
        self.assertEqual(astor.to_source(a), s, "Should be the same")

    def test_ReplaceWith(self):
        def func(cmd:ReplaceWithCommand,name):
            cmd.WithBody(
f'''
class A_{name}:
    pass
'''
            )
        (self.Engine.From("src/testcases/ReplaceWith/in.py")
                    .Select(ClassDef())
                    .Select(FunctionDef())
                    .Using(lambda x: (x.node.name,"name"))
                    .Execute(func))
        a = self.Engine.mapper[os.path.abspath("src/testcases/ReplaceWith/in.py").replace("\\","/")]
        s = ""
if __name__ == '__main__':
    unittest.main()