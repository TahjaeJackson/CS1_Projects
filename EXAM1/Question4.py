# Author: Tahjae Jackson
# Date: September 30, 2021
# Purpose: Question 4

"""
The Fibonacci sequence is a sequence of numbers: 1, 1, 2, 3, 5, 8, … where every number
is equal to the sum of two numbers before it in the sequence.
In this question define a function print_fibs_decreasing that takes a positive integer n as
parameter and prints all the numbers in Fibonacci series that are between 1 and n in
decreasing order. n is included and your function should print it, if it is a Fibonacci sequence
number. You are not allowed to use Python syntax that has not been discussed in class. For
example:
1. if n = 10, then your function should print
8
5
3
2
1
1
2. if n = 5, then your function should print
5
3
2
1
1
3. if n = 1, then your function should print
1
1
"""

#Purpose: To print fibonacci numbers in decreasing order, from the upper limit entered to 1
#Parameters: An uppper limit integer n

def print_fibs_decreasing(n):
    f1 = 1
    f2 = 1
    limit = n

    while f2 <= limit:
        new = f1 + f2
        if new <= limit:
            f1 = f2
            f2 = new
        temp = f2
        f2 = new
    f2 = temp
    while f2 >= 1:
        print(f2)
        new = f2 - f1
        f2 = f1
        f1 = new

print_fibs_decreasing(10)
