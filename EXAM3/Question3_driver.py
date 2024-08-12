# Name: Tahjae Jackson
# Date: October 28, 2021
# Purpose: To create a driver that executes the country class

# Create a driver file that creates a Country object for the USA, with at least two states added to its state_list.
# The drive should also include code that calls the methods get_population and print_states_info .

from Question3 import *
from Question2 import *
from Question1 import *

# This is the declaration of town objects that will be stored in the first state object
ithaca = Town("Ithaca", 2000, "New York")
albany = Town("Albany", 30000, "New York")
buffalo = Town("Buffalo", 30000, "New York")
state1 = State("New York",[ithaca, albany, buffalo], "Albany")

# This is the declaration of town objects that will be stored in the second state object
miami = Town("Miami", 20000, "Florida")
naples = Town("Naples", 300000, "Florida")
orlando = Town("Orlando", 40000, "Florida")
state2 = State("Florida", [miami, naples, orlando], "Miami")

c_list = [state1, state2]
country1 = Country("USA", c_list) # This is the creation of an object in the Country class
print("The population of the country is: ", country1.get_population())

print("\n\nHere are the details for each state: \n")
country1.print_states()