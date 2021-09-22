class DecoratedBy():
    @property
    def Decorators(self):
        try:
            return self.__decorators
        except:
            self.__decorators = []
            return self.__decorators
      
    # Setter method
    @Decorators.setter
    def Decorators(self, val):
        self.__decorators.append(val)
  
    def DecoratedBy(self, decorator:str,*args):
        try  :
            self.Decorators
        except:
            self.__decorators = []
        self.Decorators = (decorator,args)
        return self
