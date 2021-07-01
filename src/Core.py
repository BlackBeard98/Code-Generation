from ast import parse, NodeTransformer, AST , NodeVisitor


class Engine:
    def From(self, file:str):
        with open(file,"r") as r:
            return Selector(parse(r.read()))
            

class Selector:
    def __init__(self, tree):
        self.tree = tree
        self.type = None

    def Select (self,i_type):
        return Conditional(self.tree,i_type)

class Conditional:
    def __init__(self, tree, i_type):
        self.tree = tree
        self.i_type = i_type
        self.conditions = []

    def Where(self, condition):
        self.conditions.append(condition)
        return self

    def Action(self , action):
        return Executer(self.tree,self.i_type,self.conditions,action)

class Executer(NodeTransformer):
    def __init__(self,tree,i_type,conditions,action):
        self.tree = tree
        self.i_type = i_type
        self.conditions = conditions
        self.action = action

    def generic_visit(self, node):
        if isinstance(node,self.i_type):
            for con in self.conditions:
                if not con(node):
                    return NodeTransformer.generic_visit(self,node)
            self.action(node)

        return NodeTransformer.generic_visit(self,node)
    def run(self):
        return self.visit(self.tree)