# Inheritance example

class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)


class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

    def display(self):
        print("Marks:", self.marks)


s1 = Student("Rakesh", 85)

s1.show()
s1.display()
