import sys
sys.path.append("..")
from ..Modifiers import WithName,DecoratedBy,WithBody,Append,WithArg
from CodeGenerationCore import Command
from .utils import CommandOn 
from ast import FunctionDef

@CommandOn(FunctionDef)
class CloneMethodCommand(Command,WithName.WithName,DecoratedBy.DecoratedBy,WithBody.WithBody,Append.Append,WithArg.WithArg):
    pass

