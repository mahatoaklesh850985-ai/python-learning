# Case insensitive search

names = ["Rakesh", "Amit", "Suman"]

user = input("Enter name: ")

for name in names:
    if user.casefold() == name.casefold():
        print("Found")
        break
else:
    print("Not Found")
