import ast
from os import name
from CodeGenerationCore import CommandHandler , Command , Target 
from CodeGenerationCore import Target
from CodeGenerationCore import CodeGenEngine
from Commands.CloneClassCommand import CloneClassCommand
from ast import NodeTransformer

def iter_fields(node):
    """
    Yield a tuple of ``(fieldname, value)`` for each field in ``node._fields``
    that is present on *node*.
    """
    for field in node._fields:
        try:
            yield field, getattr(node, field)
        except AttributeError:
            pass

class CloneClassCommandHandler(CommandHandler[CloneClassCommand], NodeTransformer):


    def ProcessTarget(self, target:Target, engine:CodeGenEngine):
        tree = engine.mapper[target.path]
        self.current_target = target
        self.visit_ClassDef
        self.visit(tree)

    def visit_ClassDef (self, node:ast.ClassDef):
        if node == self.current_target.node:
           
            node.name = self.Command.Name
            node.decorator_list.extend([ast.Name(dec,ast.Load()) for dec in self.Command.Decorators])
        return NodeTransformer.generic_visit(self,node)
    
    def Command(self) :
        return super().Command

    @classmethod
    def CommandType(cls):
        return CloneClassCommand

