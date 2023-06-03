x = open("myFile.txt",'r')
def words():
    y = x.read()
    words1 = y.split()
    return f"Total words are {len(words1)}"    
print(words())
x.close()