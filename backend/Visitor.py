import ast

module = "example.py"
with open(module, "r") as file:
    tree = ast.parse(file.read())


class Visitor(ast.NodeVisitor):
    def __init__(self, module):
        self.module = module
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
            "docstring": ast.get_docstring(node) if ast.get_docstring(node) else "",
            "inherits": [base.id for base in node.bases],
            "classes": [],
            "functions": []
        }

        self.current = data
        self.generic_visit(node)
        prev["classes"].append(data)
        self.current = prev

    def get_parameters(self, arguments):
        # Get arguments
        regular_args = [arg.arg for arg in arguments.args] if arguments.args else []
        varargs = [arguments.vararg.arg] if arguments.vararg else []
        kwargs = [arguments.kwarg.arg] if arguments.kwarg else []

        all_args = regular_args + varargs + kwargs
        
        return all_args
    
    def visit_Function(self, node):
        prev = self.current
        data = {
            "name": node.name,
            "docstring": ast.get_docstring(node) if ast.get_docstring(node) else "",
            "parameters": self.get_parameters(node.__dict__["args"]),
            "classes": [],
            "functions": []
        }

        self.current = data
        self.generic_visit(node)
        prev["functions"].append(data)
        self.current = prev
        
    def visit_FunctionDef(self, node):
        self.visit_Function(node)

    def visit_AsyncFunctionDef (self, node):
        self.visit_Function(node)




visitor = Visitor(module)
visitor.visit(tree)
with open("data.json", "w") as file:
    import json
    json.dump(visitor.data, file, indent=4)