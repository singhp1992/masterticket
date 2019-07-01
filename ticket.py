SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100 

def calculate_price(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >= 1:
    print("There are {} tickets left!".format(tickets_remaining))
    name = raw_input("What is your name? ").capitalize()
    number_tickets = raw_input("How many tickets would you like, {}?  ".format(name))
    try: 
        number_tickets = int(number_tickets)
        if number_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets available".format(tickets_remaining))
    except ValueError as err: 
        print("There seems to be an issue, try using a number!".format(err))
    else:
        amount = calculate_price(number_tickets)
        print("Total: ${}".format(amount))
        continue_yn = raw_input("Do you want to proceed? Y/N  ")
        if continue_yn.lower() == "y": 
            print("Sold!")
            tickets_remaining -= number_tickets
        else: 
            print("Thank you for your time, {} :)".format(name))
print("Sorry the tickets are sold out! :(")
