from typing import List


class Person:
    attrType = "Human"
    __privateAttr = "Private"

    def __init__(self, job, name) -> None:
        self.job = job
        self.name = name
        self.workhours = 0
    
    def __printPrivate(self):
        print(f"printing from private method {self.__privateAttr}")

    def printPrivate(self):
        self.__printPrivate()

    def work(self, hours):
        self.workhours +=hours
    
    def totalWork(self):
        print(f"Total time worked {self.workhours} for {self.name}")
    

Rick = Person("Dev", "Rick")
Morty = Person("Test", "Morty")

print(Rick.attrType)
print(Morty.attrType)
print(Person.attrType)

Rick.work(5)
Morty.work(6)
Rick.work(2)
Morty.work(3)

Rick.printPrivate()
#This is mangling
print(Rick._Person__privateAttr)

Rick.totalWork()
Morty.totalWork()

print(Rick.__class__)

print(isinstance(Rick, Person))
print(type(Rick))
print(type(1))
print(type("Rick"))
print(type({}))
print(type([]))
print(isinstance([], dict))