TICKET_PRICE = 10

tickets_remaining = 100 

while tickets_remaining >= 1:
    print("There are {} tickets left!".format(tickets_remaining))
    name = raw_input("What is your name? ").capitalize()
    number_tickets = raw_input("How many tickets would you like, {}?  ".format(name))
    number_tickets = int(number_tickets)
    amount = number_tickets * TICKET_PRICE
    print("Total: {}".format(amount))
    continue_yn = raw_input("Do you want to proceed? Y/N  ")
    if continue_yn.lower() == "y": 
        # ask for credit card info
        print("Sold!")
        tickets_remaining -= number_tickets
    else: 
        print("Thank you for your time, {}".format(name))
print("Sorry the tickets are sold out! :(")
