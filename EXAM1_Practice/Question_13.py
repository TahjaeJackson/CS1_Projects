# Author: Tahjae Jackson
# Date: September 27, 2021
# Purpose: Question 13

"""
Define a function that takes a positive integer year as parameter and prints all the leap years between the first year
of the current day calendar, i.e year 1, and year.

"""

def is_leap(year):
    year_count=1
    while year_count <= year:
        if year_count % 400 == 0:
            ans=True
        elif (year_count % 100) == 0:
            ans=False
        elif (year_count % 4) == 0:
            ans=True
        else:
            ans=False
        if ans==True:
            print(year_count)
        year_count += 1

is_leap(2000)

