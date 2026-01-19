import ast


class ErrorFinder(ast.NodeVisitor):
    def __init__(self):
        self.errors = []
        self.defined_vars = set()
        self.used_vars = set()

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.defined_vars.add(target.id)
        self.generic_visit(node)

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.used_vars.add(node.id)
        self.generic_visit(node)

    def find_unused_variables(self):
        unused_vars = self.defined_vars - self.used_vars
        for var in unused_vars:
            self.errors.append({
                "type": "Unused Variable",
                "line": "Unknown",
                "message": f"Variable '{var}' is defined but never used.",
                "suggestion": f"Remove '{var}' or use it in your code."
            })
        return self.errors


# ⬇⬇⬇ MUST be at module level (no indentation)
def detect_errors(code_string):
    tree = ast.parse(code_string)

    finder = ErrorFinder()
    finder.visit(tree)

    errors = finder.find_unused_variables()

    return {
        "success": True,
        "errors": errors,
        "error_count": len(errors)
    }