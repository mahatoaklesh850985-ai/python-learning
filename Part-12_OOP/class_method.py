# Class with method

class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)

s1 = Student("Rakesh")
s1.greet()
