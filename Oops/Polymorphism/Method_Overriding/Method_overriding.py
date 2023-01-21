class A:
    def show(self):
        print("show method in class A")


class B(A):
    def show(self):
        print("show method of B overRides A")

a1=A()
a1.show()
print("\n===================================\n")
a2 = B()
a2.show()


