# Casefold example

text1 = "HELLO"
text2 = "hello"

# Without casefold
print("Without casefold:", text1 == text2)

# With casefold
print("With casefold:", text1.casefold() == text2.casefold())


# Real user input example
name = "Rakesh"

user = input("Enter name: ")

if user.casefold() == name.casefold():
    print("Matched")
else:
    print("Not matched")
