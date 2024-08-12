# Name: Tahjae Jackson
# Date: October 28, 2021
# Purpose: Define a Town class that has four instance variables name, population, state and is_capital. The instance
# variable name is a string that stores the name of the Town, population is an integer that stores the population of the
# town, state is a string that stores the name of the state the town is located in and is_capital is a boolean value
# that indicates the town is the state capital. Your Town class must support the following methods:

# 1. (2 points) __init__(self, gname, gpop, gstate): Assume that the parameters gname and gstate are strings and gpop is an integer.
# This method must initialize the instance variables name, population and state of the object being created using the parameters gname,
# gpop, and gstate respectively . The instance variable is_capital should be initialized to False and should not use a parameter to set
# the value to False.

# 2. (2 points) update_population(self, n): Assume that given parameter n is an integer. This method changes the value of the instance
# variable population to n.

# 3. (2 points) change_capital_status(self): If the value of the instance variable is_capital is False then this method should change
# it to True and vice versa.

# 4. (3 points) __str__(self): This method should return a string that has the name of the town, name of the state and the population
# of the town separated by commas. If the town is the capital of the state, in other words when the value of is_capital is True,
# it should add an asterisk to the end of the string being returned.


class Town:
    def __init__(self, gname, gpop, gstate):
        self.name = gname
        self.pop = gpop
        self.state = gstate
        self.is_capital = False

    def update_population(self,n):
        self.pop = n

    def change_capital_status(self):
        if self.is_capital:
            self.is_capital = False
        else:
            self.is_capital = True


    def __str__(self):
        if self.is_capital:
            return (self.name + ", " + self.state + ", " + str(self.pop) + " *")
        else:
            return (self.name + ", " + self.state + ", " + str(self.pop))
