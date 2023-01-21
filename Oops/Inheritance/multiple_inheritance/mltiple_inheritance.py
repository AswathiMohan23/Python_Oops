class Base1(object):
    def __init__(self):
        self.name1 = "Harry"


class Base2(object):
    def __init__(self):
        self.name2 = "Anna"


class Derived(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("child class accessing parent classes")

    def Display(self):
        print(self.name1)
        print(self.name2)


obj = Derived()
obj.Display()