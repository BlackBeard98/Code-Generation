#from abc import ABC
import sys
sys.path.append("..")
from ..Modifiers import WithName,DecoratedBy,InheritsFrom, WithBody,Append
from CodeGenerationCore import Command
from .utils import CommandOn 
from ast import ClassDef 

@CommandOn(ClassDef)
class ModifyClassCommand(Command,
                        WithName.WithName,
                        DecoratedBy.DecoratedBy,
                        InheritsFrom.InheritsFrom,
                        WithBody.WithBody,
                        Append.Append):
    pass


