class Person(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def Display(self):
        print("name : ", self.name, "\nid : ", self.id)


emp1 = Person("Tom", 2)
emp1.Display()


class Employee (Person):
    def print(self):
        print("")


details = Employee("John", 3)
details.Display()
