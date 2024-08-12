# Author: Tahjae Jackson
#  Date: September 26, 2021
#  Purpose: To practice for the exam

"""1. Given the three inner angles of a triangle they are valid if the sum of three
angles is 180. If they are valid then using the following conditions you can identify if it is an equilateral, isosceles or
scalene triangle.

A triangle is equilateral if all three angles are equal
A triangle is isosceles is any of the two angles are equal
A triangle is scalene otherwise

Define a function identify_triangle that takes three integers that represent the values of three angles as parameters and does
the following:

 If they can form a triangle then it prints the type of the triangle (equilateral, isosceles, or scalene)
In this problem you can assume that the given values for parameters add up to 180 and need not check that condition.
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

    if angle_3==angle_2==angle_1:
        print("This is an equilateral triangle")
    elif (angle_3==angle_2|angle_2==angle_1|angle_1==angle_3):
        print("This is an isosceles triangle")
    else:
        print("This is an isosceles triangle")

identify_triangle()
