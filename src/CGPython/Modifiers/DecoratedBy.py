class DecoratedBy():
    @property
    def Decorators(self):
        return self.__decorators
      
    # Setter method
    @Decorators.setter
    def Decorators(self, val):
        self.__decorators.append(val)
  
    def DecoratedBy(self, decorator:str):
        try  :
            self.Decorators
        except:
            self.__decorators = []
        self.Decorators = decorator
        return self
