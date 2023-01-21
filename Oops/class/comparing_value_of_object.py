class Details:
    def __init__(self):
        self.name="Tom"
        self.age=15

    def change_data(self):
        self.age=4

    def compare(self, data2):
        if self.age == data2.age:
            return True
        else:
            return False


data1=Details()
data2=Details()
data1.name = "Ravi"
data1.change_data()
if data1.compare(data2):
    print("same age")
else:
    print("different age")

print(data1.name,data1.age)
print(data2.name,data2.age)
