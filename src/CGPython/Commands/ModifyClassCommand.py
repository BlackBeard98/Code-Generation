#from abc import ABC
import sys
sys.path.append("..")
from ..Modifiers import WithName,DecoratedBy,InheritsFrom, WithBody,Append
from CodeGenerationCore import Command


class ModifyClassCommand(Command,WithName.WithName,DecoratedBy.DecoratedBy,InheritsFrom.InheritsFrom,WithBody.WithBody,Append.Append):
    pass


