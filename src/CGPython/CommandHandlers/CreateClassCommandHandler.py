import ast
import sys
sys.path.append("..")
from ast import AST
from os import name
from CodeGenerationCore import CommandHandler , Command , Target 
from CodeGenerationCore import Target
from CodeGenerationCore import CodeGenEngine
from ..Commands.CreateClassCommand import CreateClassCommand
from ast import NodeTransformer, ClassDef
from .utils import Handles


@Handles(CreateClassCommand)
class ModifyMethodCommandHandler(CommandHandler[CreateClassCommand], NodeTransformer):


    def ProcessTarget(self, target:Target, engine:CodeGenEngine):
        tree = engine.mapper[target.path]
        self.current_target = target
        self.visit(tree)
        self

    def create(self ,node:ClassDef):
        try:
            node.name = self.Command.Name
        except:
            pass
        try:
            node.body = self.Command.Body
        except:
            pass
        node.bases = []
        try:
            node.bases.extend([ast.Name(base,ast.Load()) for base in self.Command.InheritsTypes])
        except:
            pass
        node.decorator_list = []
        for dec in self.Command.Decorators:
            if dec[1] == ():
                node.decorator_list.append(ast.Name(dec[0],ast.Load()))
            else:
                arg = [ast.parse(x,mode='eval') for x in dec[1]]
                node.decorator_list.append(ast.Call(ast.Name(dec[0],ast.Load()),arg,[]))
        try:
            node.body.extend(self.Command.Tail)
        except:
            pass

    def generic_visit (self, node):
        if node == self.current_target.node:
            new_Class = ClassDef()
            self.create(new_Class)
            node.body.append(new_Class)
        return NodeTransformer.generic_visit(self,node)
    
    def Command(self) :
        pass
        ##return super().Command

   
