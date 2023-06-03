#1
def greeting(first,last):
    def getFullname():
        return first + " " + last
    print("Hi, " + getFullname()+ "!")
first = input("What is your name?: ")
last = input("What is your last name?: ")
greeting(first, last)

#2
def tem(start,end):
    if(start<=end):
        F = (9/5)*start+32
        print(f"{start} Celcius = {F:.2f} Farenheit.")
        tem(start+1, end)
start = int(input("Enter  a beginning Celcius value: "))
end = int(input("Enter  an ending Celcius value: "))
tem(start, end)

#3
def Mul(a,b):
    if(b<=12):
        print(f"{a} x {b} = {a*b}")
        Mul(a,b+1)
num = int(input("Enter a number: "))
print("Multiplication Table of " ,num, "is:")  
Mul(num,1)

#4
name = input("Please enter your name: ").capitalize()
age = int(input("Please enter your age: "))
def price(name,age):
    ticket_price = 0

    def members(name):
        members_name = ["Tony", "Peter", "Mark", "Kim", "James", "Kenny"]
        if name in members_name:
            members_name1 = True
            return members_name1
        else: 
            members_name1 = False
            return members_name1
            
    if members(name) == True:
        if age<=15:
            ticket_price = 3.75
            return f"Ticket price for Lauren is: $ {ticket_price:.2f}" 
        else:
            ticket_price = 7.5
            return f"Ticket price for Lauren is: $ {ticket_price:.1f}" 
    else:
        if age<=15:
            ticket_price = 7.5
            return f"Ticket price for Lauren is: $ {ticket_price:.1f}" 
        else:
            ticket_price = 15
            return f"Ticket price for Lauren is: $ {ticket_price:.1f}" 
print(price(name,age))