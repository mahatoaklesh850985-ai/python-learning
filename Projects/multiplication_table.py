# Multiplication Table

def table(num):
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

n = int(input("Enter number: "))
table(n)
