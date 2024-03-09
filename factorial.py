n = int(input("Enter the number"))

Factorial = 1
if(n<0):
    print("Factorial Does not exist")
if(n == 0):
    print("1")
else:
    for i in range(1,n+1):
        Factorial = Factorial * i


print(Factorial)