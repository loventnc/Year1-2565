from traceback import print_tb
score = int(input("Plese enter your score: "))
if score > 80:
    print("You got A")
elif score >= 79:
    print("You got B+")
elif score >= 74:
    print("You got B") 
elif score >= 69:
    print("You got C+")
elif score >= 64:
    print("You got C")
elif score >= 59:
    print("You got D+")
elif score >= 54:
    print("You got D")
else:
    print("You got F")