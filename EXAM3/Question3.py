# Name: Tahjae Jackson
# Date: October 28, 2021
# Purpose:

# Define a Country class that has two instance variables name and state_list. The instance variable name is a string and
# state_list is a list of State objects that indicates the states in the country. Your Country class must support the following methods:

# 1. (2 points) __init__(self, gname, gstate_list): Assume that the parameters gname is a string and gstate_list is a list that
# contains references to State objects. This method must initialize the instance variables name and state_list of the object
# being created using the parameters gname and gstate_list respectively .

# 2. (5 points) get_population(self):The population of a country can be computed by adding the population of all the states
# in the country. This method should return the sum of populations of all states whose reference is in instance variable state_list.

# 3. (3 points) print_states_info(self):This method should print the information about each state in instance variable state_list by calling
# the __str__ method of the State class.

# [Note that your code should not call __str__ method directly. It should instead use code that indirectly calls __str__ method.]

from Question2 import *

class Country:

    def __init__(self, gname, gstate_list):
        self.name = gname
        self.state_list = gstate_list


    def get_population(self):
        sum = 0
        for i in range(0, len(self.state_list)):
            sum = sum + self.state_list[i].get_population()

        return sum

    def print_states(self):
        for i in range(0, len(self.state_list)):
            print(str(self.state_list[i]))

