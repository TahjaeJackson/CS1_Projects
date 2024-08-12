# Name: Tahjae Jackson
# Date: November 2, 2021
# Purpose: To practice recursion

# Define a recursive function that takes a list of positive integers and counts the quantity of 3-digit numbers in the list

def three_digs(list, i =0, sum = 0):
    if i == len(list)-1:
        return sum
    if list[i] >= 100 or list[i] >= 999:
        sum = sum + 1

    return three_digs(list, i+1, sum)


def three_digs2(list):
    if len(list) == 0:
        sum = 0
        return sum
    else:
        sum = three_digs2(list[1:])
        if list[0] >= 100 or list[0] >= 999:
            sum = sum + 1

        return sum






# Define a recursive function that takes a list of positive integers and returns a list containing all 3-digit numbers in the given list

def three_digs_list(list, i =0, three_dig_list= []):
    if i == len(list)-1:
        return three_dig_list
    if list[i] >= 100 or list[i] >= 999:
        three_dig_list.append(list[i])

    return three_digs_list(list, i+1, three_dig_list)


def three_digs_list2(list):
    if len(list) == 0:
        three_dig_list = []
        return three_dig_list
    else:
        final_list = three_digs_list2(list[1:])
        if list[0] >= 100 or list[0] >= 999:
            final_list.append(list[0])

    return final_list




# Define a recursive function that takes positive integer n as parameter and prints all the multiples of 5 between 1 and n. Write 2 functions that prints:
# a. In ascending
# b. In descending

def a_multiples(n, start = 1):
    if start == n:
        return

    if start% 5 == 0:
        print(start)

    a_multiples(n, start + 1)


def a_multiples2(n):
    if n == 0:
        return
    else:
        a_multiples2(n-1)
        if n % 5 == 0:
            print(n)


def b_multiples(n):
    if n == 4:
        return

    if n % 5 == 0:
        print(n)

    b_multiples(n-1)





list = [100,20,5,300,456,99]
print(three_digs2(list))
# print(three_digs(list))

b_multiples(20)
a_multiples2(20)

print(three_digs_list(list))
print(three_digs_list2(list))

