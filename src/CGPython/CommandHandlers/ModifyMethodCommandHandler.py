import ast
import sys
sys.path.append("..")
from ast import AST
from os import name
from CodeGenerationCore import CommandHandler , Command , Target 
from CodeGenerationCore import Target
from CodeGenerationCore import CodeGenEngine
from ..Commands.ModifyMethodCommand import ModifyMethodCommand
from ast import NodeTransformer
from .utils import Handles


@Handles(ModifyMethodCommand)
class ModifyMethodCommandHandler(CommandHandler[ModifyMethodCommand], NodeTransformer):


    def ProcessTarget(self, target:Target, engine:CodeGenEngine):
        tree = engine.mapper[target.path]
        self.current_target = target
        self.visit(tree)
        self



    def visit_FunctionDef (self, node:ast.FunctionDef):
        if node == self.current_target.node:
            try:
                node.name = self.Command.Name
            except:
                pass
            try:
                node.body = [self.Command.Body]
            except:
                pass
            for dec in self.Command.Decorators:
                if dec[1] == ():
                    node.decorator_list.append(ast.Name(dec[0],ast.Load()))
                else:
                    arg = [ast.parse(x,mode='eval') for x in dec[1]]
                    node.decorator_list.append(ast.Call(ast.Name(dec[0],ast.Load()),arg,[]))
                    
        return NodeTransformer.generic_visit(self,node)
    
    def Command(self) :
        return super().Command

   
