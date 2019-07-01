TICKET_PRICE = 10

tickets_remaining = 100 

#output how many tickets are remaining using the tickets_remaining variable
print("There are {} tickets left!".format(tickets_remaining))

# gather user name and assign to a variable
name = raw_input("What is your name? ") 

# prompt the user by name and ask how many tickets they would like
num_tickets = raw_input("How many tickets would you like, {}?  ".format(name))
num_tickets = int(num_tickets)

# calculate the price (number of tickets x price) and assign to a variable
amount = num_tickets * TICKET_PRICE

# output the price to the screen
print("Total: {}".format(amount_due))
