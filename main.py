from _ast import AST
import ast
from typing import Any

module = "example.py"
with open(module, "r") as file:
    tree = ast.parse(file.read())


class Visitor(ast.NodeVisitor):
    def __init__(self, module):
        self.module = module.split(".")[0]
        self.current = {}
        self.data = {}  
    
    def visit_Module(self, node):
        self.data[self.module] = {
            "classes": [],
            "functions": []
        }

        self.current = self.data[self.module]
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        prev = self.current
        data = {    
            "name": node.name,
            "inherits": [base.id for base in node.bases],
            "classes": [],
            "functions": []
        }

        self.current = data
        self.generic_visit(node)
        prev["classes"].append(data)
        self.current = prev
        
    # def visit_FunctionDef(self, node):
    #     prev = self.current
    #     prev[node.name] = {}
    #     self.current = prev[node.name]

    #     # Get arguments
    #     arguments = node.__dict__["args"]
    #     regular_args = [arg.arg for arg in arguments.args] if arguments.args else []
    #     varargs = [arguments.vararg.arg] if arguments.vararg else []
    #     kwargs = [arguments.kwarg.arg] if arguments.kwarg else []

    #     all_args = regular_args + varargs + kwargs

    #     # Get Return
        

    #     data = {
    #         "type": "function",
    #         "arguments": all_args
    #     }

    #     self.generic_visit(node)
    #     prev[node.name].update(data)
    #     self.current = prev




visitor = Visitor(module)
visitor.visit(tree)
with open("data.json", "w") as file:
    import json
    json.dump(visitor.data, file, indent=4)





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