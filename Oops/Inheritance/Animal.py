class WildAnimal(object):
    def __init__(self, name, food):
        self.name = name
        self.food = food

    def Display(self):
        print("name  : ", self.name, ", food : ", self.food)

    def stay(self):
        print("lives in the forest")


class Carnivore(WildAnimal):
    def printing(self):
        print("Its an animal ====> child class")


animal1 = WildAnimal("zebra", "grass")
animal1.Display()

animal2 = Carnivore("lion", "flesh")
animal2.Display()
animal2.printing()
animal2.stay()



