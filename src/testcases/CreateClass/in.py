from ast import NodeVisitor

class A:
    
    def __init__(self,name:str) -> None:
        self.name = name
    
    def A_soy(self):
        print(self.name)