# Name: Tahjae Jackson
# Date: October 28, 2021
# Purpose: To create a driver that executes the State class



# Create a driver file that creates a State object (pick any state of your choice) with at least
# three Town objects in its town_list. The driver should also include code that calls the methods get_population,
# change_capital, get_capital_town, and __str__ methods defined in the State class .

from Question2 import *
from Question1 import *

# Declaration of the town objects to be stored in the state class
ithaca = Town("Ithaca", 2000, "New York")
albany = Town("Albany", 30000, "New York")
buffalo = Town("Buffalo", 30000, "New York")

townlist = [ithaca, albany, buffalo]

state1 = State("New York", townlist, "Albany")

state1.get_population()
print(state1)

state1.change_capital("Ithaca")
state1.get_capital_town()
# output the information after the capital has been changed
print(state1)
