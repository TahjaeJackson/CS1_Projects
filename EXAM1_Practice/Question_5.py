# Author: Tahjae Jackson
# Date: September 27, 2021
# Purpose: Question 5

"""
Define a function print_evens that takes a positive integer n as parameter and prints all the even numbers between 0 and n,
excluding n irrespective of if it is even or odd.

"""
# Purpose: To print all the even numbers
# Parameters: The positive integer n

def print_evens (n):
    count=0
    while count < n :
        count += 1
        if count % 2 == 0:
            print(count)


print_evens(17)