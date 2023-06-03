name = input("Please enter your name: ").capitalize()
age = int(input("Please enter your age: "))
def price(name,age):
    ticket_price = 0

    def members(name):
        members_name = ["Tony", "Peter", "Mark", "Kim", "James", "Kenny"]
        if name in members_name:
            members_name1 = True
            return members_name1
        else: 
            members_name1 = False
            return members_name1
            
    if members(name) == True:
        if age<=15:
            ticket_price = 3.75
            return f"Ticket price for Lauren is: $ {ticket_price:.2f}" 
        else:
            ticket_price = 7.5
            return f"Ticket price for Lauren is: $ {ticket_price:.1f}" 
    else:
        if age<=15:
            ticket_price = 7.5
            return f"Ticket price for Lauren is: $ {ticket_price:.1f}" 
        else:
            ticket_price = 15
            return f"Ticket price for Lauren is: $ {ticket_price:.1f}" 
print(price(name,age))