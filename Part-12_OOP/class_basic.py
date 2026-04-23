# Class basic example

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# object তৈরি
s1 = Student("Rakesh", 19)
s2 = Student("Amit", 20)

print(s1.name, s1.age)
print(s2.name, s2.age)
