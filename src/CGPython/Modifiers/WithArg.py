class WithArg():
    @property
    def Args(self):
        try:
            return self.__args
        except:
            return []
      
    # Setter method
    @Args.setter
    def Args(self, val):
        self.__args.append(val)
  
    def WithArgs(self, name:str,value=None, argtype=2):
        try  :
            self.__args
        except:
            self.__args = []
        self.Args = (name,value,argtype)
        return self