import ast
from typing import Union, Callable
import inspect
import re
from .utils import _get_ast

class WithBody():

    # Getter method
    @property
    def Body(self):
        return self.__body
      
    # Setter method
    @Body.setter
    def Body(self, val):
        self.__body = val
    

    def WithBody(self, body:Union[str,Callable]):
        if isinstance( body, str):
            self.Body = [ast.parse(body)]
        if isinstance(body,Callable):
            self.Body = _get_ast(body).body
        return self

