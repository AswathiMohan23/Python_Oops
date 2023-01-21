class Base:
    def __init__(self, name):
        self.name = name


class Child(Base):

    # Constructor
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age

    # To get name
    def getAge(self):
        return self.age


class GrandChild(Child):

    # Constructor
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address

    # To get address
    def getAddress(self):
        return self.address

    def Display(self):
        print("name : ", self.name)
        print("age : ", self.age)
        print("address : ", self.address)


obj = GrandChild("Tom", 13, "India")
print(obj.getAge(), obj.getAddress())
obj.Display()
