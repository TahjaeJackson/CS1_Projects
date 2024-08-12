# Author: Tahjae Jackson
# Date: September 22, 2021
# Purpose: Problem 1

year = 1
BRUTUS_INITIAL_WEALTH = float (1.00)
INTEREST = 1.05
wealth = float(1)
CURRENT_YEAR = 2021

while year <= CURRENT_YEAR:
    wealth = wealth * INTEREST
    # print("At the end of year", year, ", Brutus has $", wealth)
    year += 1

wealth = "{:.3e}".format(wealth)
print ("At the end of year", CURRENT_YEAR, ", Brutus has $",wealth)

# https://stackoverflow.com/questions/24118366/round-exponential-float-to-2-decimals
# The site above was used as source in determining how to round the float to two decimal places.