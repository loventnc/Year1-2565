#1
namelist = ["Jeff" ,"Jack" ,"Jim"]
name1 = (input("What is your name?:" ))
namecap = name1.capitalize()

def Checkname(namecap ,namelist):
    if namecap in namelist:
        return print("Hello, %s. Good morning my friend!" %namecap)
    else:
        return print("Who are you? \nNice to meet you anyway... %s :)." %namecap)
Checkname(namecap ,namelist)

#2
hour = int(input("How many hours did you work last week? "))
money = int(input("What is your pay rate per hour(between 10-25)"))

def normalrate(hour ,money):
    if hour <= 40: return (hour*money)
    else:
        return ((hour-40)*(1.5*money))+(40*money)
print(normalrate(hour ,money))

#3
primenumber = int(input("Enter a number test:"))

def primenumbercheck(primenumber):
    if primenumber > 1:
        for i in range(2,primenumber):
            if (primenumber % i) == 0:
                return print("This is not a prime number")
                break
        else:
            return print("This is a prime number")
    else:
        return print("This is not a prime number")
primenumbercheck(primenumber)

#4
elements = int(input("Enter number of elements :"))
listnum = []

def createlist(elements):
    for a in range(elements): 
        member = int(input())
        listnum.append(member)
createlist(elements)
print("The entered list is",listnum)
print("The maximum number entered is",max(listnum))
print("The minimum number entered is",min(listnum))

#5
print("Please enter a choice for your selection:")
print("Enter 1 if you want to calulate the area of a triangle.")
print("Enter 2 if you want to calulate the volumn of cubic.")
print("Enter 3 if you want to calulate the volumn of cone.")

choice = int(input("Enter your choice here:"))

def area():
    base = int(input("Please the base length :"))
    height = int(input("Please the height :"))
    a = 1/2 * base * height
    result = "The are of triangle with base = {} and height = {} is {} "
    return result.format(base,height,a)

def cubic():
    base = int(input("Please the base width :"))
    length = int(input("Please the length :"))
    height = int(input("Please the height :"))
    result_cubic = base * length * height
    result = "The cubic volum of width = {} length = {} and height = {} is {}"
    return result.format(base,length,height,result_cubic)

def conic():
    base = int(input("Please the base diameter :"))
    height = int(input("Please the height :"))
    c = base/2
    result_conic = (((c**2)*22/7)*height)/3
    result = "The conical volumn of cone with daimeter = {:.1f} and hegiht = {:.1f} is {:.12f}"
    return result.format(base,height,result_conic)

if choice == 1:
    print(area())
elif choice == 2:
    print(cubic())
elif choice == 3:
    print(conic())
else:
    print("Invalid Choice")