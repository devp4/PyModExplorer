import ast

class Visitor(ast.NodeVisitor):
    def __init__(self, module):
        self.module = module
        self.current_module = []
        self.current_class = []

        self.current = {}
        self.data = {}  
    
    def visit_Module(self, node):
        self.data = {
            "name": self.module,
            "children": [
                {
                    "name": "Imports",
                    "children": []
                }
            ],
            "attributes": {
                "type": "module",
                "docstring": ast.get_docstring(node) if ast.get_docstring(node) else ""
            }
        }

        self.current = self.data["children"]
        self.current_module = self.data["children"]
        self.generic_visit(node)
        self.current_module[0]["children"].sort(key=lambda imp: "children" not in imp)

    def visit_Import(self, node):
        imports = self.current_module[0]["children"]

        for name in node.names:
            imports.append({
                "name": name.name,
                "attributes": {
                    "type": "import"
                }
            })

    def visit_ImportFrom(self, node):
        imports = self.current_module[0]["children"]

        data = {
            "name": node.module,
            "children": [],
            "attributes": {
                "type": "module"
            }
        }

        for name in node.names:
            data["children"].append({
                "name": name.name,
                "attributes": {
                    "type": "import"
                }
            })

        imports.append(data)
    
    def getInheritence(self, node):
        if isinstance(node, ast.Name):
            return node.id
        
        if isinstance(node.value, ast.Name):
            return node.value.id + "." + node.attr
        
        names = []
        _node = node
        while (not isinstance(_node, ast.Name)):
            names.append(_node.attr)
            _node = _node.value

        names.append(_node.id)
        joined_names = ".".join(names[::-1])
        return joined_names

    def get_class_variables(self, node):
        class_vars = []
        vars_seen = set()

        for item in node.body:
            if isinstance(item, ast.Assign):
                for target in item.targets:
                    if isinstance(target, ast.Name) and target.id not in vars_seen:
                        class_vars.append({
                            "name": target.id,
                            "attributes":{
                                "type": "variable"
                            }
                        })
                        vars_seen.add(target.id)

        return class_vars

    def visit_ClassDef(self, node):
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
                "children": [{"name": self.getInheritence(base), "attributes": {"type": "class"}} for base in node.bases]
            },
            {
                "name": "Class Variables",
                "children": self.get_class_variables(node),
            },
            {
                "name": "Instance Variables",
                "children": [],
            }
        ])

        self.current_class = data["children"]
        self.current = data["children"]

        self.generic_visit(node)
        prev.append(data)
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
                "docstring": ast.get_docstring(node) if ast.get_docstring(node) else ""
            },
        }

        data["children"].extend([{
            "name": "Parameters",
            "children": self.get_parameters(node.__dict__["args"])
        }])

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
            current_instance_variables = [variable["name"] for variable in self.current_class[2]["children"]]
            for target in targets:
                if isinstance(target, ast.Attribute):
                    if target.value.id:
                        if target.attr not in current_instance_variables:
                            self.current_class[2]["children"].append({
                                "name": target.attr,
                                "attributes": {
                                    "type": "variable"
                                }
                            })

                            current_instance_variables.append(target.attr)


def getTreeFromModule(module):
    with open(module, "r") as file:
        tree = ast.parse(file.read())

    return tree

def getTreeFromSourceCode(content):
    tree = ast.parse(content)
    return tree