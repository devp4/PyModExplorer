import ast

# Your Python code as a string
python_code = """
class MyClass:
    class_var = 42  # This is a class variable

    def __init__(self):
        self.instance_var = 'Hello'  # This is an instance variable

    def some_method(self):
        self.another_instance_var = 'World'  # This is also an instance variable
"""

# Parse the Python code into an AST
tree = ast.parse(python_code)

# Find and inspect ClassDef nodes
for node in ast.walk(tree):
    if isinstance(node, ast.ClassDef):
        class_name = node.name  # Get the name of the class
        instance_variables = {}
        class_variables = {}

        for item in node.body:
            if isinstance(item, ast.FunctionDef):
                # Methods (FunctionDef)
                for method_item in item.body:
                    if isinstance(method_item, ast.Assign):
                        # Assignment (Assign) within a method
                        for target in method_item.targets:
                            if isinstance(target, ast.Name):
                                if item.name == '__init__':
                                    # Inside __init__, it's an instance variable assignment
                                    instance_variables[target.id] = None
                                else:
                                    # In other methods, it's a local variable
                                    pass
            elif isinstance(item, ast.Assign):
                # Assignment (Assign) within the class body
                for target in item.targets:
                    if isinstance(target, ast.Name):
                        if target.id in instance_variables:
                            # It's an instance variable assignment
                            instance_variables[target.id] = None
                        else:
                            # It's a class variable assignment
                            class_variables[target.id] = None

        print(f"Class Name: {class_name}")
        print(f"Instance Variables: {list(instance_variables.keys())}")
        print(f"Class Variables: {list(class_variables.keys())}")
