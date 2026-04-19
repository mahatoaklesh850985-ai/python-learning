# 1. Simple function
def greet():
    print("Hello")

greet()


# 2. Function with parameter
def greet_user(name):
    print("Hello", name)

greet_user("Rakesh")


# 3. Function with return
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum =", result)


# 4. Default parameter
def country(name="India"):
    print("Country:", name)

country()
country("USA")
