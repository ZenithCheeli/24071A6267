def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multi(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Infinite"
    return x / y

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = input("Enter operator (+, -, *, /): ")

if c == '+':
    print(f"Result: {add(a, b)}")
elif c == '-':
    print(f"Result: {subtract(a, b)}")
elif c == '*':
    print(f"Result: {multi(a, b)}")
elif c == '/':
    print(f"Result: {div(a, b)}")
else:
    print("Invalid operator! Please enter +, -, *, or /.")
