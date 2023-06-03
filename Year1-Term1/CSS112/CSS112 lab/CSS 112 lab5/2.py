x = open("myFile.txt",'r')
def number():
    num = len(x.read())
    return f"Total letters are {num}"
print(number())
x.close()