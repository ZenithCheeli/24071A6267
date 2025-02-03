def fibo(x):
    if x == 0 or x == 1:
        return x
    else:
        return fibo(x - 1) + fibo(x - 2)

a = int(input("Enter number: "))

for i in range(a+1):
    print(fibo(i), end=" ")
