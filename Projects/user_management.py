# User Management System

class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def show(self):
        print("User:", self.name)


class Admin(User):
    def __init__(self, name, password):
        super().__init__(name, password)

    def show(self):
        print("Admin:", self.name)


users = []

while True:
    print("\n1. Add User")
    print("2. View Users")
    print("3. Login")
    print("4. Exit")

    choice = input("Enter choice: ")

    # Add user
    if choice == "1":
        name = input("Enter name: ")
        password = input("Enter password: ")

        user = User(name, password)
        users.append(user)

        print("User added")

    # View users
    elif choice == "2":
        for u in users:
            u.show()

    # Login system
    elif choice == "3":
        name = input("Enter name: ")
        password = input("Enter password: ")

        found = False

        for u in users:
            if u.name == name and u.password == password:
                print("Login successful")
                found = True
                break

        if not found:
            print("Invalid credentials")

    elif choice == "4":
        break

    else:
        print("Invalid choice")
