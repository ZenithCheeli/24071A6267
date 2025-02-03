print("Let's check if prime or not")
num=int(input("Enter number: "))
if(num%2==0 and num>2):
    print(str(num)+ " is not a prime.")
elif(num%3==0 and num>3):
    print(str(num)+ " is not a prime.")
elif(num%5==0 and num>5):
    print(str(num)+ " is not a prime.")
elif(num%7==0 and num>7):
    print(str(num)+ " is not a prime.")
else:
    print(str(num)+ " is a prime.")