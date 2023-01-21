class Details:
    def __init__(self):
        self.name="Tom"
        self.age=15

    def change_data(self):
        self.age=20


data1=Details()
data2=Details()
data1.name = "Ravi"
data1.change_data()
print(data1.name,data1.age)
print(data2.name,data2.age)
