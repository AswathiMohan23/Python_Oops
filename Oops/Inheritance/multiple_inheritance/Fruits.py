class MonocotFruits(object):
    def __init__(self):
        self.name1 = "coconut"
        self.division1 = "Monocotyledons"


class DicotFruits(object):
    def __init__(self):
        self.name2 = "Mango"
        self.division2 = "Dicotyledons"


class Fruits(MonocotFruits, DicotFruits):
    def __init__(self):
        DicotFruits.__init__(self)
        MonocotFruits.__init__(self)

    def Display(self):
        print(self.name1, " ====> ", self.division1)
        print(self.name2, " ====> ", self.division2)


obj = Fruits()
obj.Display()