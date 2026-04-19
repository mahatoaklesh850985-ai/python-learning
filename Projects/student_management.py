# Student Management System

students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    # Add student
    if choice == "1":
        name = input("Enter name: ")
        age = input("Enter age: ")
        city = input("Enter city: ")

        student = {
            "name": name,
            "age": age,
            "city": city
        }

        students.append(student)
        print("Student added successfully")

    # View students
    elif choice == "2":
        for s in students:
            print(s)

    # Search student
    elif choice == "3":
        search = input("Enter name to search: ")

        found = False
        for s in students:
            if s["name"].casefold() == search.casefold():
                print(s)
                found = True
                break

        if not found:
            print("Student not found")

    # Exit
    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice")
