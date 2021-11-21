from CodeGenerationCore.CodeGenerationResolver  import CodeGenResolver
from CodeGenerationCore import CommandHandler
from .Commands import *
from .CommandHandlers import *
from CodeGenerationCore import Command
import punq
from typing import Generic, Tuple
import sys
import importlib
from inspect import isclass



class PythonGenerationResolver(CodeGenResolver):
    def __init__(self, imports:list[Tuple[str,str]]=[]) -> None:
        self.imports = imports
        self.builder = punq.Container()

    def Build(self):
        def get_all_subclasses(cls):
            all_subclasses = []

            for subclass in cls.__subclasses__():
                all_subclasses.append(subclass)
                all_subclasses.extend(get_all_subclasses(subclass))

            return all_subclasses

        for cls  in get_all_subclasses(CommandHandler):
            x = cls.CommandType()
            self.builder.register(CommandHandler[x], cls)

        for path, modname in self.imports:
            sys.path.append(path)      
            module = importlib.import_module(modname)  
            for attribute_name in dir(module):
                attribute = getattr(module, attribute_name)

                if isclass(attribute):
                    if attribute != CommandHandler and issubclass(attribute,CommandHandler):    
                        x = attribute.CommandType()
                        self.builder.register(CommandHandler[x], attribute)        
                        # Add the class to this package's variables
                        globals()[attribute_name] = attribute

    def RegisterEngine(engine):
        return super().RegisterEngine()

    def ResolveCommand():
        pass

    def ResolveCommandHandler(self,commandBuilder:type)->CommandHandler:
        #x = type(commandBuilder)
        return self.builder.resolve(CommandHandler[commandBuilder])
