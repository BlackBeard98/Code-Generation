import ast
class Append():

    # Getter method
    @property
    def Tail(self):
        return self.__tail
      
    # Setter method
    @Tail.setter
    def Tail(self, val):
        self.__tail = val
    
  

    def Append(self, s_tail:str):
        try  :
            self.Tail
        except:
            self.__tail= []
        self.Tail = ast.parse(s_tail)
        return self
