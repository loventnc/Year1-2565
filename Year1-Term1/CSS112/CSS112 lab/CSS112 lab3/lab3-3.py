primenumber = int(input("Enter a number test:"))

def primenumbercheck(primenumber):
    if primenumber > 1:
        for i in range(2,primenumber):
            if (primenumber % i) == 0:
                return print("This is not a prime number")
                break
        else:
            return print("This is a prime number")
    else:
        return print("This is not a prime number")
primenumbercheck(primenumber)