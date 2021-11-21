import sys

sys.path.append('../')
from CodeGenerationCore import CommandHandler,  Command
from typing import Callable , Generic , TypeVar
from CodeGenerationCore import CodeGenEngine , SingleTarget , MultipleTargets


T = TypeVar("T")
G = TypeVar("G")


class PythonSingleTarget(Generic[T], SingleTarget):
    
    def __init__(self,node:T, engine:CodeGenEngine , path:str ,parent:'PythonSingleTarget'=None) -> None:
        self.path = path
        self.node = node
        self.engine = engine
        self.arg_dict = {}
        self.parent:PythonSingleTarget = parent

    def Select(self, i_type:G) ->'PythonMultipleTargets[G]':
        from .PythonCodeGenerationEngine import Selector
        mt = Selector(self.node,type(i_type)).run_descendants()
        return PythonMultipleTargets([PythonSingleTarget(node,self.engine,self.path,self) for node in mt ], self.engine)


    def Execute(self, commandModifier:Callable):
        cmdName = commandModifier.__code__.co_varnames[0]
        cmdType:Command = commandModifier.__annotations__[cmdName]
        if not cmdType.CommandType is None:
            if not any([on_type for on_type in cmdType.CommandType if isinstance(self.node,on_type) ] ):
                raise TypeError("The type of the target's node can't be modified by this command")
        self.engine.CodeGenerationResolver.Build()
        handler =  self.engine.CodeGenerationResolver.ResolveCommandHandler(cmdType)
        self.arg_dict[cmdName] = cmdType()
        varnames = commandModifier.__code__.co_varnames[:commandModifier.__code__.co_argcount]
        solved_args = [self.arg_dict[x] for x in varnames]
        solved_args = solved_args[:commandModifier.__code__.co_argcount]
        commandModifier(*solved_args)
        handler.Command = solved_args[0]
        handler.ProcessTarget(self,self.engine)

    def Using(self, d:Callable[['PythonSingleTarget'],tuple[None,str]]):
        arg , name = d(self)
        self.arg_dict[name] = arg 
        return self

    @property
    def Node(self):
        return self.node
    @property
    def DocumentPath(self):
        return self.path
    
    def Get(self, arg):
        return self.arg_dict[arg]

class PythonMultipleTargets(Generic[T], MultipleTargets):
    def __init__(self,targets,engine:CodeGenEngine) -> None:
        self.targets:list[PythonSingleTarget] = targets
        self.engine = engine
        
    def Assign(self,Parent):
        for tg in self.targets:
            tg.Parent = Parent

    def Select(self, i_type:G)->'PythonMultipleTargets[G]':
        selectTargets = []
        for target in self.targets:
            temp = target.Select(i_type)
            #selectTargets.extend(zip(temp,len(temp)*[target.path]))
            selectTargets.extend(temp.targets)
        return PythonMultipleTargets(selectTargets, self.engine)
    
    def Execute(self, commandModifier) ->'PythonMultipleTargets[T]':
        for tg in self.targets:
            tg.Execute(commandModifier)
        return self

    def Using(self, d:Callable[['PythonSingleTarget[T]'],tuple[None,str]] ) ->'PythonMultipleTargets[T]':
        for tg in self.targets:
            tg.Using(d)
        return self
        
    def Where(self, WhereSelector:Callable[['PythonSingleTarget[T]'],bool])->'PythonMultipleTargets[T]':
        return PythonMultipleTargets([tg for tg in self.targets if WhereSelector(tg)],self.engine)

