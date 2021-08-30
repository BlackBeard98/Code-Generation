from Core import Engine
import ast
import astor



def change_name(node):
    node.name = node.name + "_test"

a = Engine().From(
    "C:\\Users\\carlos\\Desktop\\Tesis\\Codigo\\Code-Generation\\src\\mod1.py").Select(
    ast.ClassDef).Action(
    change_name).run()
print(a)
b = astor.to_source(a)
print(b)