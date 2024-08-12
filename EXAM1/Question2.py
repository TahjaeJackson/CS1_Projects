# Author: Tahjae Jackson
# Date: September 30, 2021
# Purpose: Question 2

"""
 Define a function get_max that takes three integers n1, n2 and n3
as parameters and prints the parameter that has the maximum value. If there are two
parameters that have the same maximum value then either of the two can be printed (but not
both).
For example:
1. if n1 = -4, n2 = 2 and n3 = 15 then your function should print 15.
2. if n1 = -10, n2 = -2 and n3 = -4 then your function should print -2.
3. if n1 = 10, n2 = 10 and n3 = 5 then your function should print 10.
4. if n1 = 5, n2 = 5 and n3 = 5 then your function should print 5.
"""

#Purpose: To display the largest value out of three integer values
#Parameters: Three integer values

def get_max(n1,n2,n3):
    if (n1 >= n2) and (n1 >= n3):
        print("The smallest value is:", n1)
    elif (n2 >= n1) and (n2 >= n3):
        print("The smallest value is:", n2)
    else:
        print("The smallest value is:", n3)

get_max(-4,2,15)