# Author: Tahjae Jackson
# Date: September 27, 2021
# Purpose: Question 3

"""
You will now write a function that defines a part of bank ATM functionality. When you enter an amount to withdraw cash from
the ATM the machine tries to minimize the number of currency notes(bills) it gives out. Let us assume the machine has only 20
dollar, 5 dollar and 1 dollar bills. Now your job is to define a function  help_atm that takes an integer withdrawal_amount as
parameter and prints the number of 20 dollar, 5 dollar and 1 dollar notes the ATM should give the customer.

For example:
If withdrawal_amount is 38 then the function should print:
    1  20 dollar
    3  5 dollar
    3 1 dollar
If withdrawal_amount is 30 then the function should print:
    1  20 dollar
    2  5 dollar
"""

def help_atm( withdrawal_amount):
    num_20 = 0
    num_5 = 0
    num_1 = 0
    while withdrawal_amount >= 20 :
          withdrawal_amount -= 20
          num_20 += 1


    while withdrawal_amount >= 5 :
        withdrawal_amount -= 5
        num_5 += 1

    while withdrawal_amount >= 1:
          withdrawal_amount -= 1
          num_1 += 1

    print("There are ",num_20,"20 dollar bills")
    print("There are ",num_5,"5 dollar bills")
    print("There are ",num_1,"1 dollar bills")

help_atm(20)



