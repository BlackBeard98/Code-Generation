#from abc import ABC
import sys
sys.path.append("..")
from Modifiers import WithName,DecoratedBy,InheritsFrom
from CodeGenerationCore import Command


class CloneClassCommand(Command,WithName.WithName,DecoratedBy.DecoratedBy,InheritsFrom.InheritsFrom):
    pass


