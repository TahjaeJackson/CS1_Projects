# Author: Tahjae Jackson
# Date: September 22, 2021
# Purpose: Problem 2

year = 1
BRUTUS_INITIAL_WEALTH = float (1.00)
PORTIA_INITIAL_WEALTH = float (100000)
BRUTUS_INTEREST = 1.05
PORTIA_INTEREST = 1.04
brutus_wealth = float(1)
portia_wealth = float(100000)
CURRENT_YEAR = 2021

while brutus_wealth <= portia_wealth :
    brutus_wealth = brutus_wealth * BRUTUS_INTEREST
    portia_wealth = portia_wealth * PORTIA_INTEREST
    # print("At the end of year", year, ", Brutus has $", wealth)
    if brutus_wealth <= portia_wealth:
        year += 1

portia_wealth = "{:.2e}".format(portia_wealth) #This function puts the float to two decimal places
portia_wealth = float (portia_wealth)
brutus_wealth = "{:.2e}".format(brutus_wealth)
brutus_wealth = float (brutus_wealth)
print("At the end of year", year, "Brutus has $", brutus_wealth, "and Portia has $", portia_wealth)
difference = brutus_wealth - portia_wealth
difference = "{:.2e}".format(difference)
difference = float(difference)
print("This is the first year that Brutus has exceeded Portia. He exceeds her by approximately: $", difference)




# https://stackoverflow.com/questions/24118366/round-exponential-float-to-2-decimals
# The site above was used as source in determining how to round the float to two decimal places.