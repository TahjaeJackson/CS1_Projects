# Name: Tahjae Jackson
# Date: November 8, 2021
# Purpose: To create a quick sort function

# Purpose: To create a function that does the partitioning in the quicksort
# Parameters: a list of values, the starting and ending index locations of the range and a compare function
# Return: The index location of the pivot

def partition(the_list, p, r, compare_func):
    pivot = the_list[r]
    (i, j)= (p - 1, p)
    while j <= r - 1:
        if compare_func(the_list[j],pivot):
             j = j + 1

        if compare_func(pivot, the_list[j]):
            i = i + 1
            (the_list[i], the_list[j]) = swap(the_list[i], the_list[j])
            j = j + 1

    (the_list[i + 1], the_list[r]) = swap(the_list[i + 1], the_list[r])
    return i + 1

# Purpose: To compare two values
# Parameters: Two values
# Return: a boolean declaring if the first value should come first

def compare_func(a, b):
    if a >= b:
        return True
    else:
        return False

# Purpose: To switch values between variables
# Parameters: Two variables
# Return: the swapped variables

def swap(a,b):
    temp = a
    a = b
    b = temp

    return a, b

# Purpose: Using quicksort to arrange a list of values
# Parameters: an unsorted list, the starting and ending index locations of the range and a compare function
# Return: Nothing

def quicksort(the_list, p, r, compare_func):
    if p >= r:
        return
    else:
        q = partition(the_list, p, r, compare_func)
        quicksort(the_list,p, q - 1, compare_func)
        quicksort(the_list, q + 1, r, compare_func)

# Purpose: To sort a list
# Parameters: a list and a compare function
# Return: none

def sort(the_list, compare_func):
    first = 0
    last = len(the_list)-1
    quicksort(the_list, first, last, compare_func)




# TEST FOR PARTITITON
# list = [2, 8, 7, 1, 3, 5, 6, 4]
# list2 = ["Dartmouth", "Cornell", "Upenn"]
# print (partition(list, 6, len(list)-1, compare_func))










