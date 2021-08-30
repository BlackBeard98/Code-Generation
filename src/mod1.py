from typing import Callable
@singleton
class A:
    """Return the pathname of the KOS root directory."""
    def __init__(self) -> None:
        """Return the pathname of the KOS root directory."""
        print("Soy __init__ de A")
    def soy(self, xcas:str):
        print( "soy")
        class B:
            def __init__(self) -> None:
                print("Soy __init__ de B")
a =A()