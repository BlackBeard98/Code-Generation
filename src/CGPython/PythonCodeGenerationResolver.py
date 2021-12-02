from CodeGenerationCore.CodeGenerationResolver  import CodeGenResolver
from CodeGenerationCore import CommandHandler
from .Commands import *
from .CommandHandlers import *
from CodeGenerationCore import Command
import punq
from typing import Generic, Tuple, Type
import sys
import importlib
from inspect import isclass
from .utils import get_all_subclasses



class PythonGenerationResolver(CodeGenResolver):
    def __init__(self, imports:list[Type[CommandHandler]]=[]) -> None:
        self.imports = imports
        self.builder = punq.Container()

    def Build(self):
        commandHandlers = get_all_subclasses(CommandHandler)
        for cls  in commandHandlers:
            x = cls.CommandType()
            self.builder.register(CommandHandler[x], cls)

        for cls  in self.imports:
            if not cls in commandHandlers:
                x = cls.CommandType()
                self.builder.register(CommandHandler[x], cls)
        
        # for path, modname in self.imports:
        #     sys.path.append(path)      
        #     module = importlib.import_module(modname)  
        #     for attribute_name in dir(module):
        #         attribute = getattr(module, attribute_name)

        #         if isclass(attribute):
        #             if attribute != CommandHandler and issubclass(attribute,CommandHandler):    
        #                 x = attribute.CommandType()
        #                 self.builder.register(CommandHandler[x], attribute)        
        #                 # Add the class to this package's variables
        #                 globals()[attribute_name] = attribute

    def RegisterEngine(engine):
        return super().RegisterEngine()

    def ResolveCommand():
        pass

    def ResolveCommandHandler(self,commandBuilder:type)->CommandHandler:
        #x = type(commandBuilder)
        return self.builder.resolve(CommandHandler[commandBuilder])
