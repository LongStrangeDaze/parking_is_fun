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

class Car():
    def __init__(self, make, model, year, color, plate):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.plate = plate


class Garage():
    def __init__(self, cars_added, spots, car_info, ticket):
        self.cars_added = []
        self.spots = 8
        self.car_info = {}
        self.ticket = 0


# This should print out the amount of spots availiable?

    def spots(self):
        return self.spots

# when a car is added it should ask for the things defined in the Car class created.


def add_car(self, car):

    # Had to ask a buddy how to set this up, going to do only 8 spots, each needs a letter and a number to work.  no symbols or special characters.
    self.identifier = ['A1', 'B2', 'C3', 'D4', 'E5', 'F6', 'G7', 'H8']

    if self.spots > 0:
        self.cars_added.append(str(car).split(', '))

    # This should lower the amount of spots we have when cars are added.
        self.spot -= 1

    # here is where we define the car_info into a dictionary.  This will let store the info we need.
        self.car_info = {'ticket': [], 'make': [],
                         'model': [], 'year': [], 'color': [], 'plate': []}

# Here we are adding the cars to our list and should be storing the desctriptions in the dictionary.
    for index, i in enumerate(self.cars_added):
        self.car_info['ticket'].append(self.indetifier[index])
        self.car_infor['make'].append(i[0])
        self.car_infor['model'].append(i[1])
        self.car_infor['year'].append(i[2])
        self.car_infor['color'].append(i[3])
        self.car_infor['plate'].append(i[4])
    return "Your car is now under our care."


