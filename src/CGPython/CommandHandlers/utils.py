def iter_fields(node):
    """
    Yield a tuple of ``(fieldname, value)`` for each field in ``node._fields``
    that is present on *node*.
    """
    for field in node._fields:
        try:
            yield field, getattr(node, field)
        except AttributeError:
            pass

class Handles:
    def __init__(self,k) -> None:
        self.k = k

    def __call__(self, f):
        f.SetCommandType(self.k)
        return f
