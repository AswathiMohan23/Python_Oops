from abc import ABC, abstractmethod


class polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass

class Triangle(polygon):
    def noofsides(self):
        print("3 sides")

class pentagon(polygon):
    def noofsides(self):
        print("5 sides")

R = Triangle()
R.noofsides()

R= pentagon()
R.noofsides()





