#1
c = int(input("Plese enter the tempetature  in celslus :" )) ;f = (9*c/5)+32 ;print ("The" ,float(c) ,"Celslus =" ,float(f) ,"Farenhite")

#2
num = int(input("Enter number"))
sum = 0
i = 1
while i <= num:
    sum = sum+i
    i = i+1 
print("Summation of numbers from 1 to" ,num,  "is:" ,sum)

#3
num = int(input("Enter a number to to make a multiplication table"))
n=1
while n <= 12:
    print(num ,"*" ,n, "=" ,num*n)
    n+=1

#4
from traceback import print_tb
score = int(input("Plese enter your score: "))
if score > 80:
    print("You got A")
elif score >= 79:
    print("You got B+")
elif score >= 74:
    print("You got B") 
elif score >= 69:
    print("You got C+")
elif score >= 64:
    print("You got C")
elif score >= 59:
    print("You got D+")
elif score >= 54:
    print("You got D")
else:
    print("You got F")

#5
start = int(input("Please enter a strating number:"))
end = int(input("Please enter a ending number:"))
for i in range(start,end+1):
    if i>1:
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            print(i)