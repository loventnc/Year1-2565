def tem(start,end):
    if(start<=end):
        F = (9/5)*start+32
        print(f"{start} Celcius = {F:.2f} Farenheit.")
        tem(start+1, end)
start = int(input("Enter  a beginning Celcius value: "))
end = int(input("Enter  an ending Celcius value: "))
tem(start, end)