# Author: Tahjae Jackson
# Date: September 29, 2021
# Purpose: To further explore functions

def func(n):
    print(n * n)

var = func #var becomes a function. Functions can behav elike variables.

var(3)

def func1(f):
    f(10) # here, f is a function and 10 is the parameter of that function

func1(func)