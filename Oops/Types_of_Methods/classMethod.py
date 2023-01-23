class Student:

    school = "Abc"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def info(cls):
        return cls.school


s1 = Student(34,67,20)
s2 = Student(23,44,56)
print(s1.avg()) # here we are passing self and not object
print(s2.avg())

print(Student.info())