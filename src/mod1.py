class A:
    def __init__(self) -> None:
        print("Soy __init__ de A")
        class B:
            def __init__(self) -> None:
                print("Soy __init__ de B")