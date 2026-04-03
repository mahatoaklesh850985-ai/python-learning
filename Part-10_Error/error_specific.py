# Specific error

try:
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    print(a / b)

except ValueError:
    print("Enter valid number")

except ZeroDivisionError:
    print("Cannot divide by zero")
