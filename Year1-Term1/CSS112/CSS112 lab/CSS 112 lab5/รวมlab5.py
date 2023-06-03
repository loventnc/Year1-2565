#1
def readfile():
    try:
        x = open("000",'r')
    except:
        return "Unable to open file myFile.txt"
    else:
        x = x.read()
        return f"{x}\nSuccessfully print content in myFile.txt"
    x.close()
print(readfile())

#2
x = open("myFile.txt",'r')
def number():
    num = len(x.read())
    return f"Total letters are {num}"
print(number())
x.close()

#3
x = open("myFile.txt",'r')
def words():
    y = x.read()
    words1 = y.split()
    return f"Total words are {len(words1)}"    
print(words())
x.close()

#4
def tem(start,end):
    if(start<=end):
        F = (9/5)*start+32
        file0.write(f"{start} Celcius = {F:.2f} Farenheit.\n")
        tem(start+1, end)
start = int(input("Enter  a beginning Celcius value: "))
end = int(input("Enter  an ending Celcius value: "))
file0 = open("multiply.txt", "w")
tem(start, end)
file0.close()