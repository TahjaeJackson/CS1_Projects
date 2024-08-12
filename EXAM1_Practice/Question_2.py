# Author: Tahjae Jackson
# Date: September 27, 2021
# Purpose: Question 2

"""
In the above problem, how will you change the function identify_triangle if it has to check if given angles can form a
triangle (add up to 180) and print “invalid input” if a triangle cannot be formed?
"""

ANGLE_SUM = 180

#Purpose: This function accepts the values of the three angles in the triangle
#Parameter: There are no parameters.

def identify_triangle():
    x = input("Please enter the value of the first angle ")
    angle_1 = int(x)

    y = input("Please enter the value of the second angle ")
    angle_2 = int(y)

    z = input("Please enter the value of the third angle ")
    angle_3 = int(z)

    sum = angle_1 + angle_2 + angle_3
    while sum !=180 :
        print("INVALID INPUT.")
        print("The sum of the angles is not 180")
        x = input("Please enter the value of the first angle ")
        angle_1 = int(x)

        y = input("Please enter the value of the second angle ")
        angle_2 = int(y)

        z = input("Please enter the value of the third angle ")
        angle_3 = int(z)
        sum = angle_1 + angle_2 + angle_3
    if angle_3==angle_2==angle_1:
        print("This is an equilateral triangle")
    elif (angle_3==angle_2|angle_2==angle_1|angle_1==angle_3):
        print("This is an isosceles triangle")
    else:
        print("This is an isosceles triangle")

identify_triangle()