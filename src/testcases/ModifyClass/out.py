from typing import Callable


class A:
    """Return the pathname of the KOS root directory."""

    def __init__(self) ->None:
        """Return the pathname of the KOS root directory."""
        print('Soy __init__ de A')

    def soy(self, xcas: str):
        print('soy')


        @suma((5))
        @casa
        class B(A):

            def __init__(self) ->None:
                print('Soy __init__ de B')
            import ast


        @suma((5))
        @casa
        class C(A):

            def __init__(self) ->None:
                print('Soy __init__ de C')
            import ast


a = A()
