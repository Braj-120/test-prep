from operator import attrgetter
from os import stat


class Person:
    attrType = "Human"
    __privateAttr = "Private"

    def __init__(self) -> None:
        self.attrC = "C"

    @staticmethod
    def stat(t):
        print(t)
        print(Person.attrType)
        # print(Person.attrC)
    
    @classmethod
    def clt(cls, m):
        print(cls, m)
        print(cls.attrType)
        print(cls.__privateAttr)
        cls.newAttr = "Tm"
    
    def method1(self) -> None:
        self.attrB = "AttrB"
        print(self.newAttr)

m = Person()
m.clt("Tudles")

Person.stat("Yum")
m.stat("Mua")

Person.method1(Person)
m.method1()

N = Person()
print(N.newAttr)
N.attrType="HumanB"
print(N.attrType)
