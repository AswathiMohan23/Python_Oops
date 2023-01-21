class Dog:

    # class attribute
    name = ""
    age = 0

# create dog1 object
dog1 = Dog()
dog1.name = "Tommy"
dog1.age = 3

# create another object dog2
dog2 = Dog()
dog2.name = "Stuart"
dog2.age = 2

# access attributes
print("My name is {}".format(dog1.name))
