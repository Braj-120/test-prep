class Person:
    _attr = "Human"
    def __init__(self, name) -> None:
        self.name = name

class Employee(Person):
    __attrRole = "IC"

    def __init__(self, name, job) -> None:
        super().__init__(name)
        self.job = job
    
    @property
    def role(self):
        print(self.__attrRole)

    @role.setter
    def role(self, b):
        self.__attrRole = b

    def print(self):
        print(self._attr)

e = Employee("B", "Dev")
e.print()
print(e._attr)

e.role
e.role = "Test"
e.role
