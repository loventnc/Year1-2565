def greeting(first,last):
    def getFullname():
        return first + " " + last
    print("Hi, " + getFullname()+ "!")
first = input("What is your name?: ")
last = input("What is your last name?: ")
greeting(first, last)