from ast import Sub
from typing import Any


class Immutable:
    """
    An Immutable class
    """
    __slots__ = ["var1", "var2"]

    def __init__(self, var1, var2) -> None:
        super().__setattr__("var1", var1)
        super().__setattr__("var2", var2)

    def __setattr__(self, __name: str, __value: Any) -> None:
        raise AttributeError("Not mutable")

i = Immutable(1, 2)
print(i.var1)
print(i.var2)
i.var3 = 4
