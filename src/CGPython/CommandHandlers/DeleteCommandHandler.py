import ast
from ast import AST
from os import name
import sys
sys.path.append("..")
from CodeGenerationCore import CommandHandler , Command , Target 
from CodeGenerationCore import Target
from CodeGenerationCore import CodeGenEngine
from ..Commands.DeleteCommand import DeleteCommand
from ast import NodeTransformer
from .utils import Handles , iter_fields
import copy

@Handles(DeleteCommand)
class DeleteCommandHandler(CommandHandler[DeleteCommand], NodeTransformer):


    def ProcessTarget(self, target:Target, engine:CodeGenEngine):
        tree = engine.mapper[target.path]
        self.current_target = target
        self.visit(tree)

    def generic_visit(self, node):
        if node == self.current_target.node:
           return None
        return NodeTransformer.generic_visit(self,node)
    
    def Command(self) :
        pass
        ##return super().Command

