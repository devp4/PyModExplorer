import ast

module = "example.py"
with open(module, "r") as file:
    tree = ast.parse(file.read())


class ParentChildBasedVisitor(ast.NodeVisitor):
    # Format JSON for react-d3-tree use
    def __init__(self, module):
        self.module = module
        self.current = {}
        self.data = {}  
    
    def visit_Module(self, node):
        self.data["name"] = self.module
        self.data["children"] = []
        self.data["_attributes"] = {}

        self.current = self.data["children"]
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        prev = self.current
        data = {    
            "name": node.name,
            "children": [],
            "attributes": {
                "docstring": ast.get_docstring(node) if ast.get_docstring(node) else "",
                "inherits": [base.id for base in node.bases],
            }
        }

        self.current = data["children"]
        self.generic_visit(node)
        prev.append(data)
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
            "children": [],
            "attributes": {
                "docstring": ast.get_docstring(node) if ast.get_docstring(node) else "",
                "parameters": self.get_parameters(node.__dict__["args"]),
            },
        }

        self.current = data["children"]
        self.generic_visit(node)
        prev.append(data)
        self.current = prev
        
    def visit_FunctionDef(self, node):
        self.visit_Function(node)

    def visit_AsyncFunctionDef (self, node):
        self.visit_Function(node)




visitor = ParentChildBasedVisitor(module)
visitor.visit(tree)
with open("data2.json", "w") as file:
    import json
    json.dump(visitor.data, file, indent=4)