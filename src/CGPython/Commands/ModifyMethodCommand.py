import sys
sys.path.append("..")
from ..Modifiers import WithName,DecoratedBy,WithBody,Append
from CodeGenerationCore import Command

class ModifyMethodCommand(Command,WithName.WithName,DecoratedBy.DecoratedBy,WithBody.WithBody,Append.Append):
    pass

