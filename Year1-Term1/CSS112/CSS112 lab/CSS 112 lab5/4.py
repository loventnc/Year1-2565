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