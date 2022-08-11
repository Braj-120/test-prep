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

Rick.attrType = "Human A"
Person.attrType = "Human B"

print(Rick.attrType)
print(Morty.attrType)
print(Person.attrType)