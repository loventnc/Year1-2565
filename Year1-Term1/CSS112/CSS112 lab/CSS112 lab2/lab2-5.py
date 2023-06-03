start = int(input("Please enter a strating number:"))
end = int(input("Please enter a ending number:"))
for i in range(start,end+1):
    if i>1:
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            print(i)