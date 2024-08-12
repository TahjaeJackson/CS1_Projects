# Author: Tahjae Jackson
# Date: September 27, 2021
# Purpose: Break and continue

#break and continue statemnets only make sense inside a loop

def func(n):
    i = 5
    while i<n :
        i +=1
        if i == 8:
            """break""" #a break statement will exit the lopp
            continue # a continue statement will cause the loop back to go back to the header

        print(i)
    print("Out of while loop")

func(15)