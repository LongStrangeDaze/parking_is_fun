# Your parking gargage class should have the following methods:
# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True
# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

# We will need to different classes: One for cars and the other for the garage.

class Garage():
    def __init__(self, ticket, spots ,myTicket):
        self.ticket = ticket
        self.spots = spots
        self.myTicket = myTicket

    # def spots_available(self):
    #     return self.spots

    def available_Ticket(self):
        if len(self.ticket) == 0:
            print('There are no more tickets available.')
        else:
            available_spot = self.ticket.pop(0)
            print(f"Park in space {available_spot}")
            self.spots.append(available_spot)
            self.myTicket[available_spot] = "unpaid"
            if self.myTicket == {}:
                return
            else:
                print(self.myTicket)

    def pay(self):

        available_spot = input('What spot were you in? ')

        if self.myTicket[available_spot] == 'unpaid':
            pay = input('Type pay to pay')
            if pay == 'pay':
                self.myTicket[available_spot] = 'paid'
                print('Ticket has been paid, you have 15 minutes to leave.')
        else:
            print('Please enter payment of $5')

    def remove_car(self):
        leave = input('If leaving, enter parking spot. ')
        if self.myTicket[leave] == 'paid':
            self.spots.remove(leave)
            self.ticket.append(leave)
            self.ticket.sort()
            del self.myTicket[leave]
        else: 
            return self.pay
parking_spots = ['A1', 'B2', 'C3', 'D4', 'E5', 'F6', 'G7', 'H8']

terry_chet_parking = Garage(parking_spots, [], {})

def Garage():
    while True:
        Welcome = input('Welcome. Would you like to park, pay, leave, or quit? ')
        if Welcome == 'park':
            terry_chet_parking.available_Ticket()
        elif Welcome == 'pay':
            terry_chet_parking.pay()
        elif Welcome == 'leave':
            terry_chet_parking.remove_car()
        elif Welcome == 'quit':
            break
        else:
            print('Please enter park, pay, leave, or quit. ')
    
Garage()