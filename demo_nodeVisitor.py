import ast

class VariableCounter(ast.NodeVisitor):
    """
    Counts variables assignment.
    """

    def __init__(self):
        self.count = 0
        self.variables = []

    def visit_Assign(self, node):
        self.count += 1

        for target in node.targets:
            if isinstance(target, ast.Name):
                self.variables.append(target.id)

        self.generic_visit(node)

code = """
x = 5
y = 10
Name = "Alice"
result = x + y
total = 100
"""

tree = ast.parse(code)
counter = VariableCounter()
counter.visit(tree)

print(f"Total Assignment: {counter.count}")
print(f"Variables: {', '.join(counter.variables)}")
