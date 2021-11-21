import ast
import sys
sys.path.append("..")
from ast import AST
from CodeGenerationCore import CommandHandler , Command , Target 
from CodeGenerationCore import Target
from CodeGenerationCore import CodeGenEngine
from CGPython.Commands.ReplaceWithCommand import ReplaceWithCommand
from ast import NodeTransformer, ClassDef, Constant , Expr
from CGPython.CommandHandlers.utils import Handles


@Handles(ReplaceWithCommand)
class ModifyMethodCommandHandler(CommandHandler[ReplaceWithCommand], NodeTransformer):


    def ProcessTarget(self, target:Target, engine:CodeGenEngine):
        tree = engine.mapper[target.path]
        self.current_target = target
        self.visit(tree)
        


    def generic_visit (self, node):
        if node == self.current_target.node:
            return Expr(value=Constant(value=5))
           #return NodeTransformer.generic_visit(self,ast.parse(self.Command.Body,mode="eval"))
        return NodeTransformer.generic_visit(self,node)
   
    def Command(self) :
        pass
        ##return super().Command

   
