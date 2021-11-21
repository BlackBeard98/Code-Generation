class CommandOn:
    def __init__(self,n_type) -> None:
        self.n_type = n_type

    def __call__(self, cls):
        cls.SetCommandType(self.n_type)
        return cls

def get_all_subclasses(cls):
            all_subclasses = []

            for subclass in cls.__subclasses__():
                all_subclasses.append(subclass)
                all_subclasses.extend(get_all_subclasses(subclass))
            return all_subclasses
import abc 
import ast
class ABCWithSTMTBody(metaclass = abc.ABCMeta):
    pass
for cls in get_all_subclasses(ast.stmt):
    if 'body' in cls._fields:
        ABCWithSTMTBody.register(cls)