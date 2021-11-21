class Command:
   @classmethod
   @property
   def CommandType(cls):
      try:
         return cls.__type
      except:
         return None
    
   @classmethod
   def SetCommandType(cls,__type):
      try:
         cls.__type.append( __type)
      except:
         cls.__type = []
         cls.__type.append(__type)
              