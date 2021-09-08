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



if __name__ == '__main__':
    unittest.main()

               

                