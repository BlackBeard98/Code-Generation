from CGPython import PythonCodeGenEngine , PythonGenerationResolver
from CGPython.Commands import *
from ast import ClassDef, FunctionDef
import os
import astor

eng = PythonCodeGenEngine(PythonGenerationResolver([("C:/Users/carlos/Desktop/Tesis/Codigo/Code-Generation/src", "example")]))
def func(cmd:ReplaceWithCommand,name):
            class B:
                def __init__(self) -> None:
                    pass
            
            cmd.WithNode(B)
        
            
(eng.From("src/testcases/ReplaceWith/in.py")
                    .Select(ClassDef())
                    .Select(FunctionDef())
                    .Using(lambda x: (x.node.name,"name"))
                    .Execute(func)
                    )
       
a = eng.mapper[os.path.abspath("src/testcases/ReplaceWith/in.py").replace("\\","/")]
print(astor.to_source(a))