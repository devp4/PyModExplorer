import ast
from Visitor import Visitor

with open("Visitor.py", "r") as file:
    tree = ast.parse(file.read())

visitor = Visitor("Visitor.py")
visitor.visit(tree)