import sys
import os
import re
import inspect 
if __name__ == "__main__":
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir) 
    sys.path.insert(0, parentdir) 
import importlib
import Transformers
import astor
from CGPython import CodeGenerationTransformer, PythonCodeGenEngine,PythonGenerationResolver
from inspect import isclass


def main():
    # transformer_name = "C:\\Users\\carlos\\Desktop\\Tesis\\Codigo\\Code-Generation\\src\\Transformers\\TrueStaticTransformer.py"
    transformer_name = sys.argv[1]
    path = sys.argv[2]
    path = os.path.abspath(path).replace("\\","/")

    x = re.search('^".*"$',transformer_name)
    transformer:CodeGenerationTransformer =  None

    if x:
        transformer = getattr(Transformers, transformer_name[1:-1])()
    else:
        transformer_name =  os.path.abspath(transformer_name).replace("\\","/")
        real_dir =os.path.dirname(transformer_name)
        real_name = os.path.basename(transformer_name)
        real_name = real_name[:-3 ]if  real_name[-3:] == ".py" else real_name 
        sys.path.append(real_dir)      
        module = importlib.import_module(real_name)
        attribute = getattr(module, real_name)
        if isclass(attribute) and issubclass(attribute,CodeGenerationTransformer):
                transformer = attribute()


    transformer.Engine = PythonCodeGenEngine(PythonGenerationResolver())
    transformer.Engine.From(path)
    transformer.Transform()
    mapper = transformer.Engine.mapper
    for p in mapper:
        with open(p,"w") as f:
            f.write(astor.to_source(mapper[p]))
    # print(astor.to_source(transformer.Engine.mapper[path]))

if __name__ == "__main__":
    main()