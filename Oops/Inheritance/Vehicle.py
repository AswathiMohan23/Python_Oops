class Vehicle(object):
    def __init__(self, name, wheels):
        self.name = name
        self.wheels = wheels

    def Display(self):
        print("name : ", self.name, ", wheels : ", self.wheels)


class Electric(Vehicle):
    def printing (self):
        print(" Operated using electricity ===> child class")


car = Vehicle("car", "4 wheels")
bike = Vehicle("bike", "2 wheels")
car.Display()
bike.Display()

details = Electric(" electric car", "4 wheels")
details.Display()
details.printing()
