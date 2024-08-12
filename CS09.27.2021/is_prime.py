# Author: Tahjae Jackson
# Date: September 27, 2021
# Purpose: Using a return statement to build is prime

#Purpose: To check if a number is a prime number
#Parameter: The value of an integer 'n' will be passed through the function


def is_prime(n):
    if n == 1:
        print(False)
        return #This could be substitued by an else

    factor = 2
    while factor < n :
        if n % factor == 0:
            #print(False)
            #break
            return False
        factor += 1

    if factor == n :
        #print (True)
        return True


i = 1
while i<100:
    check = is_prime(i)
    if check == True:
        print(i)
    i += 1