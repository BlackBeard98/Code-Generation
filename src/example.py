from Core import Engine
import ast
import astor



def change_name(node):
    node.name = node.name + "_test"

a = Engine().From("mod1.py").Select(ast.ClassDef).Action(change_name).run()
b = astor.to_source(a)
print(b)