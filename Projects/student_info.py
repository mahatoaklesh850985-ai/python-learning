# Student info

student = {}

student["name"] = input("Enter name: ")
student["age"] = input("Enter age: ")
student["city"] = input("Enter city: ")

print("Student Details:")
for key in student:
    print(key, ":", student[key])
