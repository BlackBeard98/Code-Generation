class WithName():

    def __init__(self) -> None:
        pass  
    # Getter method
    @property
    def Name(self):
        return self.__name
      
    # Setter method
    @Name.setter
    def Name(self, val):
        self.__name = val
  
    def WithName(self, Name):
        self.Name = Name
        return self


