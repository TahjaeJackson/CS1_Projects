# Author: Tahjae Jackson
# Date: October 13, 2021
# Purpose:




# 4. Define a function that takes a list of integers glist as parameter and prints the even numbers in glist. For example if glist
# = [1, 4, 5, 20, 2, 12, 81]  then your program should print:
# 4
# 20
# 2
# 12


def even_num(glist):
    for i in glist:
        if i%2 == 0:
            print(i)

even_num([1, 4, 5, 20, 2, 12, 81])

# 5. Define a function that takes a list of integers glist as parameter and prints the numbers at even index. For example if
# glist = [1, 4, 5, 20, 2, 12, 81]  then your program should print:
# 1
# 5
# 2
# 81



def even_num_indx(glist):
    for i in range(0, len(glist)-1):
        if glist[i]%2 == 0:
            print(i)

even_num_indx([1, 4, 5, 20, 2, 12, 81])




# 6. Define a function that takes a list of integers glist and an integer n as parameters and returns a new list that
# contains the numbers in glist that are greater than n.

def greater_list(glist,n):
    greater=[]
    for i in glist:
        if i > n:
            greater.append(i)

    print(greater)

greater_list([1, 4, 5, 20, 2, 12, 81],4)



# 7. Define a function that takes two integers m and n as parameters and returns a list of all
# integers between m and n in the list (including both m and n if they are in the list). You may assume m <= n.

def range_list(m,n):
    list=[]
    for i in range(m,n+1):
        list.append(i)

    print(list)

range_list(2,9)