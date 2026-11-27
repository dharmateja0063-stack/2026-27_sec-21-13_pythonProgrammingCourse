class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Creating an object
s1 = Student("Krishna", 18)

# Calling the method
s1.display()