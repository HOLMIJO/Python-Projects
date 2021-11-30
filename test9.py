# Created a parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Created a child class, inherits functionality from parent class
class Employee(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

y = Employee("Joseph", "Holmin")
y.printname()

