import sys
sys.path.append('../')
#from CodeGenerationCore.Target import Target 
from CodeGenerationCore import CommandHandler
from typing import Callable , Generic , TypeVar
from CodeGenerationCore import CodeGenEngine , Target

T = TypeVar("T")
G = TypeVar("G")


class PythonSingleTarget(Generic[T], Target):
    
    def __init__(self,node:T, engine:CodeGenEngine , path:str) -> None:
        self.path = path
        self.node = node
        self.engine = engine

    def Select(self, i_type:T) ->'PythonMultipleTargets[T]':
        from PythonCodeGenerationEngine import Selector
        return Selector(self.node,type(i_type)).run_descendants()

    def Execute(self, commandModifier):
        cmdType = commandModifier.__annotations__["cmd"]
        self.engine.CodeGenerationResolver.Build()
        x =self.engine.CodeGenerationResolver.ResolveCommandHandler(cmdType)
        command = cmdType()
        commandModifier(command)
        x.Command = command
        x.ProcessTarget(self,self.engine)

    def Using(self, d:Callable[['PythonSingleTarget'],None]):
        pass
    def Where(self, WhereSelector):
        pass
    def Get(self , key , value):
        pass
    def Node(self):
        pass
    def DocumentPath(self):
        pass

class PythonMultipleTargets(Generic[T], Target):
    def __init__(self,targets,engine:CodeGenEngine) -> None:
        self.targets:list[PythonSingleTarget] = targets
        self.engine = engine

    def Select(self, i_type:G)->'PythonMultipleTargets[G]':
        selectTargets = []
        for target in self.targets:
            temp = target.Select(i_type)
            selectTargets.extend(zip(temp,len(temp)*[target.path]))
        return PythonMultipleTargets([PythonSingleTarget(node,self.engine,path) for node,path in selectTargets ], self.engine)
    
    def Execute(self, commandModifier):
        for tg in self.targets:
            tg.Execute(commandModifier)

    def Using(self, d:Callable[['PythonSingleTarget[T]'],None] ) ->'PythonMultipleTargets[T]':
        return self
        
    def Where(self, WhereSelector):
        pass
    def Get(self , key , value):
        pass
    def Node(self):
        pass
    def DocumentPath(self):
        pass
