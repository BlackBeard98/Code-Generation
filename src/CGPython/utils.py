from typing import List, TypeVar, Generic,Type

T = TypeVar("T") 


def get_all_subclasses(cls:T) -> List[Type[T]]:
            all_subclasses = []

            for subclass in cls.__subclasses__():
                all_subclasses.append(subclass)
                all_subclasses.extend(get_all_subclasses(subclass))
            return all_subclasses
