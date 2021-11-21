import inspect
import re
import ast
def _get_ast(func):
    # Get function source
    source = inspect.getsource(func)

    # Fix extra indent if present
    spaces = re.search(r'^\s*', source).group()
    if spaces:
        source = re.sub(r'(^|\n)' + spaces, '\n', source)

    # Preserve line numbers
    #source = '\n' * (func.__code__.co_firstlineno - 2) + source

    return ast.parse(source, mode= 'exec')