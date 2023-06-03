namelist = ["Jeff" ,"Jack" ,"Jim"]
name1 = (input("What is your name?:" ))
namecap = name1.capitalize()

def Checkname(namecap ,namelist):
    if namecap in namelist:
        return print("Hello, %s. Good morning my friend!" %namecap)
    else:
        return print("เตอร์มีแฟนไปแล้ว ว้ายๆ %s." %namecap)
Checkname(namecap ,namelist)

