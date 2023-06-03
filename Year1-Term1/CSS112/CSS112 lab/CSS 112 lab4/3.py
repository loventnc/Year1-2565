def Mul(a,b):
    if(b<=12):
        print(f"{a} x {b} = {a*b}")
        Mul(a,b+1)
num = int(input("Enter a number: "))
print("Multiplication Table of " ,num, "is:")  
Mul(num,1)