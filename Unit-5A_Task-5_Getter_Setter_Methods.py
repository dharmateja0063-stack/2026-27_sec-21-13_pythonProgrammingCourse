class Student:
    def __init__(self, marks):
        self.__marks = marks

    # Getter method
    def get_marks(self):
        return self.__marks

    # Setter method
    def set_marks(self, marks):
        self.__marks = marks

s1 = Student(80)

print("Original Marks:", s1.get_marks())

s1.set_marks(95)

print("Updated Marks:", s1.get_marks())