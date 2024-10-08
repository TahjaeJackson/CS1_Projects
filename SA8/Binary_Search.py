# Name: Tahjae Jackson
# Date: October 31, 2021
# Purpose: Using recursion to implement binary search

# binary_search.py
# Code provided for CS 1 Short Assignment 7.
# Performs binary search on a sorted list of random numbers.

from random import randint


# Purpose: Perform binary search for key on the sublist of the_list starting at index left and going up to and including index right.
# Return: If key appears in the_list, return the index where it appears. Otherwise, return None.
# Parameters: A sorted list, the key to be search for, and the beginning and ending of the range of the search

def binary_search(the_list, key, left=None, right=None):
    # If using the default parameters, then search the entire list.
    if left == None and right == None:
        left = 0
        right = len(the_list) - 1

    # ADDED BINARY SEARCH CODE
    if left > right:
        return None
    else:
        mid = (left + right) // 2
        if the_list[mid] == key:
            return mid
        elif the_list[mid] < key:
            # we return the function so that is the value is found, returns the value of the mid, exits the recursion, instead of erasing the location of the found key
            return binary_search(the_list, key, mid + 1, right)
        elif the_list[mid] > key:
            return binary_search(the_list, key, left, mid - 1)






# Driver code for binary search.
n = int(input("How many items in the list? "))

# Make a list of n random ints.
i = 0
the_list = []
while i < n:
    the_list.append(randint(0, 1000))
    i += 1

# Binary search wants a sorted list.
the_list = sorted(the_list)
print("The list: " + str(the_list))

while True:
    key = input("What value to search for? ('?' to see the list, 'q' to quit): ")

    if key == "?":
        print("The list: " + str(the_list))
    elif key == "q":
        break
    else:
        key = int(key)
        index = binary_search(the_list, key)
        if index == None:
            print(str(key) + " not found")
        else:
            print(str(key) + " found at index " + str(index))