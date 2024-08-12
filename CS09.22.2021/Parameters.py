# Author: Tahjae Jackson
# Date: September 22, 2021
# Purpose: Demo parameters

#Purpose: To show the working of parameter
#Parameter: A string parameter representing a course
#Return: _____ (not yet applicable)
""" THE COMMENTS MENTIONED ABOVE SHOULD ALWAYS BE PRESENTED WHEN USING A FUNCTION"""


def demo_function(course, term):
    print("Welcome to", course, term)
    print("Are you having fun?")

print("Before the function call")
demo_function("CS1", "F21")  #This is how you call a function. Also, if a parameter was not passed, the code will not work.
demo_function("CS10", "F21")
print("After the function call")
