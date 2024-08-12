# Author: Tahjae Jackson
# Date: September 27, 2021
# Purpose: Question 6

"""

 Define a function print_evens that takes a positive integer n as parameter and prints all the even numbers between 0 and n,
 including n if it is an even number.

"""

def print_evens (n):
    count=0
    while count <= n :
        count += 1
        if count % 2 == 0:
            print(count)


print_evens(18)