# Function Practice Set

# 1. Square function
def square(n):
    return n * n

print("Square:", square(5))


# 2. Even/Odd function
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(7))


# 3. Sum of list
def list_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print("Sum:", list_sum([1, 2, 3, 4]))


# 4. Greeting with default
def greet(name="User"):
    print("Hello", name)

greet()
greet("Rakesh")
