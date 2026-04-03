# Save user data

name = input("Enter name: ")
age = input("Enter age: ")

with open("user.txt", "a") as file:
    file.write(name + " - " + age + "\n")

print("Data saved")
