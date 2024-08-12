# Author: Tahjae Jackson
# Date: September 27, 2021
# Purpose: Question 8

"""

Define a function product_even that takes a positive integer n as parameter and prints the product of all even numbers
between 1 and n (including n).

"""

def product_even(n):
    product=1
    count=0
    while count <= n:
        count += 1
        if count % 2 == 0:
            product = product * count
    print(product)

product_even(6)

