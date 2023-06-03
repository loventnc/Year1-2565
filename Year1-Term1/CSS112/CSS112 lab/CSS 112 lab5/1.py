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