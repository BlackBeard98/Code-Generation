import sys
sys.path.append("..")
from ..Modifiers import WithName,DecoratedBy,InheritsFrom, WithBody,Append
from CodeGenerationCore import Command
from .utils import CommandOn 
from ast import ClassDef 

@CommandOn(ClassDef)
class CloneClassCommand(Command,
                        WithName.WithName,
                        DecoratedBy.DecoratedBy,
                        InheritsFrom.InheritsFrom,
                        WithBody.WithBody,
                        Append.Append):
    pass


