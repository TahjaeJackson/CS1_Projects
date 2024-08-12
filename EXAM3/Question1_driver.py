# Name: Tahjae Jackson
# Date: October 28, 2021
# Purpose: To create a driver to execute the town class and its functionality

# Create a driver file that creates a Town object (pick any town of your choice) and does the following on that object:
# 1. without directly calling __str__ method prints the string returned when __str__ method is called on the object created above.
# 2. changes the capital status for the object created above.
# 3. again, without directly calling __str__ method prints the string returned when __str__ method is called on the object created above to see if an asterisk is added at the end of the string.
# 4. updates the population of the town to 5000.

from Question1 import *

town1 = Town("Ithaca", 200000, "New York") #This is the declaration of the town class
print(town1)
town1.change_capital_status()
print(town1)
town1.update_population(5000)
print(town1)
