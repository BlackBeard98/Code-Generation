import ast
from ast import AST
from os import name
import sys
sys.path.append("..")
from CodeGenerationCore import CommandHandler , Command , Target 
from CodeGenerationCore import Target
from CodeGenerationCore import CodeGenEngine
from ..Commands.CloneClassCommand import CloneClassCommand
from ast import NodeTransformer
from .utils import Handles , iter_fields
import copy

@Handles(CloneClassCommand)
class CloneClassCommandHandler(CommandHandler[CloneClassCommand], NodeTransformer):


    def ProcessTarget(self, target:Target, engine:CodeGenEngine):
        tree = engine.mapper[target.path]
        self.current_target = target
        self.visit(tree)

    def generic_visit(self, node):
        for field, old_value in iter_fields(node):
            if isinstance(old_value, list):
                new_values = []
                if self.current_target.node in old_value:
                    old_value.insert(old_value.index(self.current_target.node),copy.deepcopy(self.current_target.node))
                for value in old_value:
                    if isinstance(value, AST):
                        if value == self.current_target.node:
                            copy.deepcopy(value)
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
                node.body = self.Command.Body
            except: 
                pass
            try:
                node.body.extend(self.Command.Tail)
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
        pass
        ##return super().Command

