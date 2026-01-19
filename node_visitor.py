import ast

class FunctionNameFinder(ast.NodeVisitor):
    """
    Finds all function names.
    """

    def __init__(self):
        self.function_names = []

    def visit_FunctionDef(self, node):
        self.function_names.append(node.name)
        self.generic_visit(node)

code = """
def login(username, password):
    pass
    
def logout():
    pass
    
def send_email(to, subject, body):
    pass
"""

tree = ast.parse(code)
finder = FunctionNameFinder()
finder.visit(tree)

print("Function Founded:")
for name in finder.function_names:
    print(f" - {name}")