class Student:

    # class attribute
    name = ""
    age = 0
    marks = 0

# create student1 object
student1 = Student()
student1.name = "Harry"
student1.age = 12
student1.marks = 95


# create another object student2
student2 = Student()
student2.name = "James"
student2.age = 15
student2.marks = 80

# access attributes
print(f"{student1.name} is {student1.age} years old with total marks = {student1.marks}")
print(f"{student2.name} is {student2.age} years old with total marks = {student2.marks}")
