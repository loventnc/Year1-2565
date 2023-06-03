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