class RemoveArg():
    @property
    def RArgs(self):
        try:
            return self.__rargs
        except:
            return []
      
    # Setter method
    @RArgs.setter
    def RArgs(self, val):
        self.__rargs.append(val)
  
    def RemoveArg(self, name:str,value=None, argtype=2):
        try  :
            self.__rargs
        except:
            self.__rargs = []
        self.RArgs = (name,value,argtype)
        return self