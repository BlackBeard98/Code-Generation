import ast
import sys
sys.path.append("..")
from ast import AST
from CodeGenerationCore import CommandHandler , Command , Target 
from CodeGenerationCore import Target
from CodeGenerationCore import CodeGenEngine
from ..Commands.AfterNodeCommand import AfterNodeCommand
from ast import NodeTransformer, ClassDef
from .utils import Handles


@Handles(AfterNodeCommand)
class AfterNodeCommandHandler(CommandHandler[AfterNodeCommand], NodeTransformer):


    def ProcessTarget(self, target:Target, engine:CodeGenEngine):
        tree = engine.mapper[target.path]
        self.current_target = target
        self.visit(tree)
        


    def generic_visit(self, node):
            for field, old_value in ast.iter_fields(node):
                if isinstance(old_value, list):
                    new_values = []
                    if self.current_target.node in old_value:
                        old_value.insert(old_value.index(self.current_target.node)+1,self.Command.Node)
                    for value in old_value:
                        if isinstance(value, AST):
                            value = self.visit(value)
                            if value is None:
                                continue
                            elif not isinstance(value, AST):
                                new_values.extend(value)
                                continue
                        new_values.append(value)
                    old_value[:] = new_values
                elif isinstance(old_value, AST):
                    new_node = self.visit(old_value)
                    if new_node is None:
                        delattr(node, field)
                    else:
                        setattr(node, field, new_node)
            return node
   
    def Command(self) :
        pass
        ##return super().Command

   
