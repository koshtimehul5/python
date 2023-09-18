userInput = int(input("Enter your age: "))
ticketPrice = 6

if (userInput< 16):
    print("Ticket price is  £",ticketPrice/2)
elif (userInput>=60):
    print("Ticket price is  £",ticketPrice/3)
else:
    print("Ticket price is  £",ticketPrice)