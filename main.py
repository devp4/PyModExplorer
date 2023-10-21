import ast

module = "example.py"
with open(module, "r") as file:
    tree = ast.parse(file.read())


class Visitor(ast.NodeVisitor):
    def __init__(self, module):
        self.module = module.split(".")[0]
        self.parent = None
        self.data = {}

    def generic_visit(self, node):
        #print(type(node).__name__, self.data)
        if isinstance(node, ast.Module) or isinstance(node, ast.ClassDef) or isinstance(node, ast.FunctionDef):
            previous_parent = self.parent
            self.parent = self.module if isinstance(node, ast.Module) else node.name
            ast.NodeVisitor.generic_visit(self, node)   
            self.parent = previous_parent
        else:
            ast.NodeVisitor.generic_visit(self, node)
    
    def visit_Module(self, node):
        self.data[self.module] = {}
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        print(node.name, self.parent)
        self.generic_visit(node)
    
    def visit_FunctionDef(self, node):
        print(node.name, self.parent)
        self.generic_visit(node)




visitor = Visitor(module)
visitor.visit(tree)


print(visitor.data)



# for node in ast.walk(tree):
#     print(node.__dict__)
#     print(node)
#     if isinstance(node, ast.ClassDef):
#         print("Class Name: ", node.name)
#         inherits = [base.id for base in node.bases]
#         print("Inherits From: ", inherits)
    
#     if isinstance(node, ast.FunctionDef):
#         print("Function Name: ", node.name)
#         arguments_data = [val.__dict__ for val in node.args.args]
#         arguments = [(val["arg"], val["annotation"].id if val["annotation"] else None) for val in arguments_data]
#         print("Function Arguments: ", arguments)