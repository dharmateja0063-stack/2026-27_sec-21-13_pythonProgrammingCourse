class Student:
    def __init__(self):
        self.name = "Krishna"
        self._age = 18
        self.__marks = 90

    def display(self):
        print("Name:", self.name)
        print("Age:", self._age)
        print("Marks:", self.__marks)

s1 = Student()
s1.display()