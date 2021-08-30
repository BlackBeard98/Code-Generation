class InheritsFrom():
    @property
    def InheritsTypes(self):
        return self.__inheritsTypes
      
    # Setter method
    @InheritsTypes.setter
    def InheritsTypes(self, val):
        self.__inheritsTypes.append(val)
  
    def InheritsFrom(self, i_type:type):
        if self.InheritsTypes is None:
            self.self.__inheritsTypes = []
        self.InheritsTypes = i_type
        return self
