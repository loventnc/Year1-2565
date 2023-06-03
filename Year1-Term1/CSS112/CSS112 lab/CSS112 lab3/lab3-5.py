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
