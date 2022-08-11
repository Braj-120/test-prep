class Person:
    attr = "Human"
    def __init__(self, name) -> None:
        self.name = name

class Employee(Person):
    attr = "IC"

    def __init__(self, job, **kw) -> None:
        super().__init__(**kw)
        self.job = job

class Manager(Person):
    attr = "Management"
    def __init__(self, dept, empcount, **kw) -> None:
        super().__init__(**kw)
        self.dept = dept
        self.empcount = empcount

class FreshHire(Employee, Manager):
    def __init__(self, name, job, dept, empcount) -> None:
        super().__init__(name=name, job=job, dept=dept, empcount=empcount)

    def print(self):
        print(self.name, self.job, self.dept, self.empcount)


fh = FreshHire("B", "Manager", "IT", 20)

fh.print()