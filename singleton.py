class Singleton:
    __innervar=None
    class inner:
        def __init__(self) -> None:
            self.val = None
    def __init__(self) -> None:
        if Singleton.__innervar is None:
            Singleton.__innervar = Singleton.inner()
    def __getattr__(self, name):
        return getattr(self.__innervar, name)
    def __setattr__(self, name, value):
        return setattr(self.__innervar, name, value)

a = Singleton()
a.val = 6
print(a.val)
b = Singleton()
b.val = 8
print(a.val)
print(b.val)
print("---------------------------------------")

class BetterSingleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, BetterSingleton):
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

i = BetterSingleton(2,3)
i.data = 1
print(i.a, i.b)
j = BetterSingleton(4,5)
j.data = 2


print(i.data)
print(j.data)
print(j.a, j.b)
print(i.a, i.b)
print("---------------------")
"""
# Subclassing like this fails miserably due to init
class SubBetterSingleton(BetterSingleton):
    def __init__(self, a, b, c) -> None:
        super().__init__(a, b)
        self.c = c


s = SubBetterSingleton(9, 8, 7)

print(i.data)
print(j.data)
print(j.a, j.b)
print(i.a, i.b)
print(i.a, i.b)
print(s.a, s.b, s.c)
print(s.data)
"""
"""
## Output of above
2
4 5
4 5
4 5
Traceback (most recent call last):
  File "G:\test\singleton.py", line 59, in <module>
    print(s.a, s.b, s.c)
AttributeError: 'BetterSingleton' object has no attribute 'c'
##
"""

print("-------------------------------")
class Singleton:
    _instances = None

    def __new__(cls, *args, **kwargs):
        if Singleton._instances is None:
            Singleton._instances = super(Singleton, cls).__new__(cls)
        return Singleton._instances
    


class OneOfAKind(Singleton):

    def __init__(self, a, b, c):
        print('--> OneOfAKind __init__')
        self.a=a
        self.b=b
        self.c = c

osa = OneOfAKind(4, 5, 6)
osa.data = 88
print(osa.a, osa.b, osa.c, osa.data)

ofk = OneOfAKind(44,55,66)
print(osa.a, osa.b, osa.c, osa.data)

ofk.data = 98
ofk.c=77
print(osa.a, osa.b, osa.c, osa.data)
print(ofk.a, ofk.b, ofk.c, ofk.data)


