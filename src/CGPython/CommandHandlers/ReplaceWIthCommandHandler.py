import ast
import sys
sys.path.append("..")
from ast import AST
from CodeGenerationCore import CommandHandler , Command , Target 
from CodeGenerationCore import Target
from CodeGenerationCore import CodeGenEngine
from ..Commands.ReplaceWithCommand import ReplaceWithCommand
from ast import NodeTransformer, ClassDef
from .utils import Handles


@Handles(ReplaceWithCommand)
class ReplaceWithCommandHandler(CommandHandler[ReplaceWithCommand], NodeTransformer):


    def ProcessTarget(self, target:Target, engine:CodeGenEngine):
        tree = engine.mapper[target.path]
        self.current_target = target
        self.visit(tree)
        


    def generic_visit (self, node):
        if node == self.current_target.node:
            return self.Command.Node
           #return NodeTransformer.generic_visit(self,ast.parse(self.Command.Body,mode="eval"))
        return NodeTransformer.generic_visit(self,node)
   
    def Command(self) :
        pass
        ##return super().Command

   
