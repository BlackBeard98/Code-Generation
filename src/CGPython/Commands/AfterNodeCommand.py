import sys
sys.path.append("..")
from ..Modifiers import  WithNode
from CodeGenerationCore import Command


class AfterNodeCommand(Command,WithNode.WithNode):
    pass
