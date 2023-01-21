from abc import ABC, abstractmethod


class Computer:
    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print("Running")


class Programmer:
    def work(self,com):
        print("Solving error")
        com.process()


#com = Computer()
com1=Laptop()
prog1 = Programmer()
prog1.work(com1)
#com.process()

