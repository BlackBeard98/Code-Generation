import ast
from ast import AST
from os import name
import sys
sys.path.append("..")
from CodeGenerationCore import CommandHandler , Command , Target 
from CodeGenerationCore import Target
from CodeGenerationCore import CodeGenEngine
from ..Commands.ModifyClassCommand import ModifyClassCommand
from ast import NodeTransformer
from .utils import Handles

@Handles(ModifyClassCommand)
class ModifyClassCommandHandler(CommandHandler[ModifyClassCommand], NodeTransformer):


    def ProcessTarget(self, target:Target, engine:CodeGenEngine):
        tree = engine.mapper[target.path]
        self.current_target = target
        self.visit(tree)



    def visit_ClassDef (self, node:ast.ClassDef):
        if node == self.current_target.node:
            try:
                node.name = self.Command.Name
            except:
                pass
            try:
                node.bases.extend([ast.Name(base,ast.Load()) for base in self.Command.InheritsTypes])
            except:
                pass
            try:
                node.body = [self.Command.Body]
            except: 
                pass
            try:
                node.body.append(self.Command.Tail)
            except:
                pass
            try:
                for dec in self.Command.Decorators:
                    if dec[1] == ():
                        node.decorator_list.append(ast.Name(dec[0],ast.Load()))
                    else:
                        arg = [ast.parse(x,mode='eval') for x in dec[1]]
                        node.decorator_list.append(ast.Call(ast.Name(dec[0],ast.Load()),arg,[]))
            except:
                pass
            #node.decorator_list.extend([ast.Name(dec,ast.Load()) for dec in self.Command.Decorators])
        return NodeTransformer.generic_visit(self,node)
    
    def Command(self) :
        return super().Command

