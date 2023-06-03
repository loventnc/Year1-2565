hour = int(input("How many hours did you work last week? "))
money = int(input("What is your pay rate per hour(between 10-25)"))

def normalrate(hour ,money):
    if hour <= 40: return (hour*money)
    else:
        return ((hour-40)*(1.5*money))+(40*money)
print(normalrate(hour ,money))
    