# Author: Tahjae Jackson
# Date: 09/22/2021
# Purpose: Demo function + While + If

#1 1 2 3 5 8 13 21  [fibanacci series)

#Purpose: Print the first n even fibanacci numbers
#Parameters:

def even_fibs(n):
    f1 = 1
    f2 = 1
    count=0

    while count < n:
        if f1 % 2 == 0:
            print(f1)
            count += 1

        new = f1 + f2   #NB: Shift+ back moves lines out of a loop or removes an indentation. Tab adds an indentation.
        f1 = f2
        f2 = new


even_fibs(5)