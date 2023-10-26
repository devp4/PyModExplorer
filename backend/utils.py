import ast

module = "example2.py"
with open(module, "r") as file:
    tree = ast.parse(file.read())


class ParentChildBasedVisitor(ast.NodeVisitor):
    def __init__(self, module):
        self.module = module
        self.current_class = []
        self.current = {}
        self.data = {}  
    
    def visit_Module(self, node):
        self.data = {
            "name": self.module,
            "children": [],
            "attributes": {
                "type": "module",
                "docstring": ast.get_docstring(node) if ast.get_docstring(node) else ""
            }
        }

        self.current = self.data["children"]
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        print(node.decorator_list)
        prev_class = self.current_class
        prev = self.current
        
        data = {    
            "name": node.name,
            "children": [],
            "attributes": {
                "type": "class",
                "docstring": ast.get_docstring(node) if ast.get_docstring(node) else "",
            }
        }

        data["children"].extend([
            {
                "name": "Inherits",
                "children": [{"name": base.id} for base in node.bases]
            },
            {
                "name": "Class Variables",
                "children": [],
                "attributes": {
                    "count": 0
                }
            },
            {
                "name": "Instance Variables",
                "children": [],
                "attributes": {
                    "count": 0
                }
            }
        ])

        self.current_class = data["children"]
        self.current = data["children"]

        self.generic_visit(node)
        prev.append(data)
        data["children"][1]["attributes"]["count"] = len(data["children"][1]["children"])
        data["children"][2]["attributes"]["count"] = len(data["children"][2]["children"])
        self.current_class = prev_class
        self.current = prev

    def get_parameters(self, arguments):
        # Get arguments
        regular_args = [arg.arg for arg in arguments.args] if arguments.args else []
        varargs = [arguments.vararg.arg] if arguments.vararg else []
        kwargs = [arguments.kwarg.arg] if arguments.kwarg else []

        all_args_names = regular_args + varargs + kwargs
        all_args = [{
            "name": arg,
            "attributes": {
                "type": "parameter"
            }
        } for arg in all_args_names]

        return all_args
    
    def visit_Function(self, node):
        prev = self.current
        data = {
            "name": node.name,
            "children": [],
            "attributes": {
                "type": "function",
                "docstring": ast.get_docstring(node) if ast.get_docstring(node) else "",
                "parameterCount": 0
            },
        }

        data["children"].extend([{
            "name": "Parameters",
            "children": self.get_parameters(node.__dict__["args"])
        }])
        data["attributes"]["parameterCount"] = len(data["children"])

        self.current = data["children"]
        self.generic_visit(node)
        prev.append(data)
        self.current = prev
        
    def visit_FunctionDef(self, node):
        self.visit_Function(node)

    def visit_AsyncFunctionDef (self, node):
        self.visit_Function(node)

    def visit_Assign(self, node):
        targets = node.targets

        # Get all class and instance variables of a class
        if self.current_class:
            for target in targets:
                # Class Variable
                if isinstance(target, ast.Name):
                    self.current_class[1]["children"].append({
                        "name": target.id,
                        "attributes": {
                            "type": "varaible"
                        }
                    })
                
                # Instance Variable
                elif isinstance(target, ast.Attribute):
                    if target.value.id:
                        self.current_class[2]["children"].append({
                            "name": target.attr,
                            "attributes": {
                            "type": "varaible"
                            }
                        })


visitor = ParentChildBasedVisitor(module)
visitor.visit(tree)
with open("data3.json", "w") as file:
    import json
    json.dump(visitor.data, file, indent=4)