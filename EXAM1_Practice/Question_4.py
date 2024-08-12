# Author: Tahjae Jackson
# Date: September 27, 2021
# Purpose: Question 4

"""
 A leap year is defined as follows:
a) A year is a leap year if it is divisible by 400  (Example: 2000)
b) A year is a not a leap year if it is divisible by 100 but not by 400 (Example: 1900, 2100)
c)  A year is a leap year if it is divisible by 4 but not by 100 (Example: 2008)
d) All other years are not leap years
Define a function is_leap that takes year (positive integer) as parameter and prints True or False.
"""

# Purpose: Defining a function to determin a leap year
# Paramenter: The year that the user wants to find out if it is leap

def is_leap(year):
    if year % 400 == 0:
        print(True)
    elif (year % 100) == 0:
        print(False)
    elif (year % 4) == 0:
        print(True)
    else:
        print(False)

is_leap(2100)

