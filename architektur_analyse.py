import ast
import os
import graphviz

class DependencyGraphCreator(ast.NodeVisitor):
    def __init__(self):
        self.graph = graphviz.Digraph('DependencyGraph', node_attr={'shape': 'box'})
        self.current_function = None

    def visit_FunctionDef(self, node):
        function_name = node.name
        self.current_function = function_name
        self.graph.node(function_name, function_name)
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Attribute):
            callee = node.func.attr
        elif isinstance(node.func, ast.Name):
            callee = node.func.id
        else:
            callee = "unknown"
        if self.current_function:
            self.graph.edge(self.current_function, callee)
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        class_name = node.name
        self.graph.node(class_name, class_name, shape='ellipse')
        for item in node.body:
            if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                self.graph.edge(class_name, item.name)
        self.generic_visit(node)

def analyze_python_files(directory_path):
    graph_creator = DependencyGraphCreator()
    for subdir, _, files in os.walk(directory_path):
        for filename in files:
            if filename.endswith('.py'):
                file_path = os.path.join(subdir, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    source_code = file.read()
                    tree = ast.parse(source_code)
                    graph_creator.visit(tree)
    graph_creator.graph.render('dependency_graph', view=True)

if __name__ == '__main__':
    analyze_python_files(os.getcwd())
