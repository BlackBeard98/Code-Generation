import ast
class WithBody():

    def __init__(self) -> None:
        pass  
    # Getter method
    @property
    def Body(self):
        return self.__body
      
    # Setter method
    @Body.setter
    def Body(self, val):
        self.__body = val
    
    def a(self):
        pass

    def WithBody(self, sbody:str):
        import inspect
        self.Body = ast.parse(sbody)
        return self
