# Name: Tahjae Jackson
# Date: October 28, 2021
# Purpose:

# Define a State class that has three instance variables name, capital and town_list. The instance variables name and capital are
# strings that store the name of the state and name of the capital town respectively. The instance variable town_list contains
# the references of Town objects and indicates the towns that are in this state. Assume that all towns in the state have a unique
# name and only one of the towns in the list is a state capital. Your State class must support the following methods:
#
# 1. (5 points) __init__(self, gname, gtown_list, gcapital): This method should do the following:
#     a. initialize the instance variable name, town_list and capital using the values of parameters gname, gtown_list, and
#     gcapital respectively.
#     b. go through the list town_list and find the Town that has the name gcapital and call change_capital_status
#     method of the Town class to mark it as the capital of the state.
#
# 2. (5 points) get_population(self): The population of a state can be computed by adding the population of all the towns in the state.
# This method should return the sum of populations of all towns whose reference is in instance variable town_list.
#
# 3. (5 points) change_capital(self, gnew_capital): Assume that the parameter gnew_capital is a string. This method should do the following:
#     a. change the value of instance variable capital to gnew_capital.
#     b. change the capital status of the current capital of the state in town_list to False by calling change_capital_status method of the Town class
#     c. change the capital status of the town with name equal to gnew_capital to True by calling change_capital_status method of the Town class
#
# 4. (3 points) get_capital_town(self): This method should return the reference to the Town object in town_list that is marked
# as the capital town of the state.
#
# 5. (2 points) __str__(self): This method should return a string that has the name of the capital town, name of the state and
# the population of the state separated by commas. Note that the population of the state must not be stored as an instance variable.



class State:
    def __init__(self, gname, gtown_list, gcapital):
        self.name = gname
        self.gtown_list = gtown_list
        self.capital = gcapital
        for i in range(0, len(self.gtown_list)):
            if self.gtown_list[i].name == self.capital:
                self.gtown_list[i].change_capital_status()


    def get_population(self):
        sum = 0
        for i in range(0, len(self.gtown_list)):
            sum = sum + self.gtown_list[i].pop

        return sum

    def change_capital(self, gnew_capital):

        self.capital = gnew_capital

        for i in range(0, len(self.gtown_list)):
            if self.gtown_list[i].is_capital:
                self.gtown_list[i].change_capital_status()
            if self.gtown_list[i].name == self.capital:
                self.gtown_list[i].change_capital_status()

    def get_capital_town(self):
        return self.capital

    def __str__(self):
        sum = self.get_population()
        return (str(self.capital) + ", " + str(self.name) + ", " + str(sum))







