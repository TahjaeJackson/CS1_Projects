# Author: Tahjae Jackson
# Date: September 27, 2021
# Purpose: Write a function that takes two positive integers(m and n) and returns the larger



def return_larger(m,n):
    if m>n:
        return m
    else:
        return n



#Write a function that takes two positive integers(m and n) and returns their product

def product(m,n):
    product= m * n
    return product




# use functions from 2i and 2ii to find the larger of two products

print(return_larger(product(125,1234),product(234,678)))


