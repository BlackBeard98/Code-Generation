import ast
from typing import Union, Callable
import inspect
import re
from .utils import _get_ast

class WithNode():

    # Getter method
    @property
    def Node(self):
        return self.__node
      
    # Setter method
    @Node.setter
    def Node(self, val):
        self.__node = val
    

    def WithNode(self, node:Union[str,Callable]):
        if isinstance( node, str):
            self.Node = ast.parse(node)
        if isinstance(node,Callable):
            self.Node = _get_ast(node)
        return self