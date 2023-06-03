start = int(input("Please enter a starting number: "))
end = int(input("Please enter a ending number: "))
i = 1
print(f"Prime numbers between {start} and {end} are: ") 
for i in range(start , end):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i)