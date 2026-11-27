class Student:
    college = "NRI Institute of Technology"

    def __init__(self, name):
        self.name = name

    # Instance method
    def display(self):
        print("Name:", self.name)

    # Class method
    @classmethod
    def college_name(cls):
        print("College:", cls.college)

    # Static method
    @staticmethod
    def message():
        print("Welcome to Python OOP")

s1 = Student("Krishna")

s1.display()
Student.college_name()
Student.message()