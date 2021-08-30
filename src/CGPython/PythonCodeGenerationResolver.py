from CodeGenerationCore.CodeGenerationResolver  import CodeGenResolver
from CodeGenerationCore import CommandHandler
from Commands import CloneClassCommand
from CommandHandlers import CloneClassCommandHandler
from CodeGenerationCore import Command
import punq
from typing import Generic



class PythonGenerationResolver(CodeGenResolver):
    def __init__(self, path_to_import:str=None) -> None:
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

    def RegisterEngine(engine):
        return super().RegisterEngine()

    def ResolveCommand():
        pass

    def ResolveCommandHandler(self,commandBuilder:type)->CommandHandler:
        #x = type(commandBuilder)
        return self.builder.resolve(CommandHandler[commandBuilder])

if __name__ == "__main__":
    
    a = PythonGenerationResolver()
    a.Build()
    x = a.ResolveCommandHandler(CloneClassCommand())
   
    print("hello")
   