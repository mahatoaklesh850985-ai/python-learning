# Password Checker

password = input("Enter password: ")

# Check length
if len(password) < 6:
    print("Password too short")

# Check strong password
elif password.isdigit():
    print("Password should not be only numbers")

elif password.isalpha():
    print("Password should not be only letters")

else:
    print("Strong password")
