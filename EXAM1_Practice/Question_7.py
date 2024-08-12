# Author: Tahjae Jackson
# Date: September 27, 2021
# Purpose: Question 7

"""

Define a function print_odds that takes a positive integer n as parameter and prints all the odd numbers between 0 and
  n, including n if it is an odd number.

"""

def print_odds(n):
    count=0
    while count<=n :
        count += 1
        if count % 2 == 1:
            print (count)

print_odds(17)
