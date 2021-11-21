import sys
sys.path.append("..")
from ..Modifiers import WithName,DecoratedBy,WithBody,Append , RemoveArg
from CodeGenerationCore import Command
from .utils import CommandOn 
from ast import FunctionDef

@CommandOn(FunctionDef)
class ModifyMethodCommand(Command,WithName.WithName,DecoratedBy.DecoratedBy,WithBody.WithBody,Append.Append, RemoveArg.RemoveArg):
    pass

