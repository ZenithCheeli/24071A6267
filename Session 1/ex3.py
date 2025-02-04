import math as m
print("Finding GCD")
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
while(b!=0):
    r = a%b
    a=b
    b=r

print("Gcd is "+ str(a))
print("Finding LCM")
c = int(input("Enter number 1: "))
d = int(input("Enter number 2: "))
lcm = m.lcm(c,d)
print("Lcm is "+ str(lcm))