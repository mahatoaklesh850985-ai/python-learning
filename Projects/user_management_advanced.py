# Advanced User System

users = []

while True:
    print("\n1. Add")
    print("2. View")
    print("3. Delete")
    print("4. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        name = input("Name: ")
        users.append(name)

    elif ch == "2":
        for u in users:
            print(u)

    elif ch == "3":
        name = input("Enter name to delete: ")
        if name in users:
            users.remove(name)
            print("Deleted")
        else:
            print("Not found")

    elif ch == "4":
        break
