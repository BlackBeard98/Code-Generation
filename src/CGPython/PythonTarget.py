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
        self.arg_dict = {}

    def Select(self, i_type:T) ->'PythonMultipleTargets[T]':
        from PythonCodeGenerationEngine import Selector
        return Selector(self.node,type(i_type)).run_descendants()

    def Execute(self, commandModifier:Callable):
        cmdName = commandModifier.__code__.co_varnames[0]
        cmdType = commandModifier.__annotations__[cmdName]
        self.engine.CodeGenerationResolver.Build()
        x =self.engine.CodeGenerationResolver.ResolveCommandHandler(cmdType)
        self.arg_dict[cmdName] = cmdType()
        solved_args = [self.arg_dict[x] for x in commandModifier.__code__.co_varnames]
        commandModifier(*solved_args)
        x.Command = solved_args[0]
        x.ProcessTarget(self,self.engine)

    def Using(self, d:Callable[['PythonSingleTarget'],tuple[None,str]]):
        arg , name = d(self)
        self.arg_dict[name] = arg 
        return self
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

    def Using(self, d:Callable[['PythonSingleTarget[T]'],tuple[None,str]] ) ->'PythonMultipleTargets[T]':
        for tg in self.targets:
            tg.Using(d)
        return self
        
    def Where(self, WhereSelector:Callable[['PythonSingleTarget[T]'],bool])->'PythonMultipleTargets[T]':
        return PythonMultipleTargets([tg for tg in self.targets if WhereSelector(tg)],self.engine)

    def Get(self , key , value):
        pass
    def Node(self):
        pass
    def DocumentPath(self):
        pass
