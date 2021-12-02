import ast
import sys
sys.path.append("..")
from ast import AST , FunctionDef
from os import name
from CodeGenerationCore import CommandHandler , Command , Target 
from CodeGenerationCore import Target
from CodeGenerationCore import CodeGenEngine
from ..Commands.CreateMethodCommand import CreateMethodCommand
from ast import NodeTransformer
from .utils import Handles


@Handles(CreateMethodCommand)
class CreateMethodCommandHandler(CommandHandler[CreateMethodCommand], NodeTransformer):


    def ProcessTarget(self, target:Target, engine:CodeGenEngine):
        tree = engine.mapper[target.path]
        self.current_target = target
        self.visit(tree)
        self

    def create(self ,node):
        try:
            node.name = self.Command.Name
        except:
            pass
        try:
            node.body = self.Command.Body
        except:
            pass
        args = []
        df = []
        for ag in self.Command.Args:
            if ag[2] == 2:
                if ag[1] == None:
                    args.append(ast.arg(arg=ag[0]))
                else:
                    df.append(ag)
        for ag in df:
            args.append(ast.arg(arg=ag[0]))
        node.args = ast.arguments([],args,defaults=[ast.parse(x[1],mode='eval') for x in df ])
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
            new_Class = FunctionDef()
            self.create(new_Class)
            node.body.append(new_Class)
        return NodeTransformer.generic_visit(self,node)
    
    def Command(self) :
        pass
        ##return super().Command
