# Author: Tahjae Jackson
# Date: September 22, 2021
# Purpose: Global vs Local vs parameters


"""
def func1(n):
    x=10   #x is a local variable. It's only accessible in this function. It cannot be accessed outside of the function.
    print (n,x)

def func2(m):
     x=200
     print(m,x)

func1(4)
func2(7)
func1(11)

# scope of a variable is where the variable is available
#local variables only stay in memory while the function code is running. After the fuction has completed the running process, the variables are erased from memory.
"""


#   GLOBAL AND LOCAL VARIABLE

"""
x=1000
def func1(n):
    x=10
    print(n,x)

func1(4)
print(x)
"""

#The code above will treat the x in the code as a local variable and the code would delete the value stored after the function's completion.
# It would output the value 1000 for x


#GLOBAL VARIABLES How to use global variables in a function. (Using global variables is not recommended

#Multiple functions can interact with each other using variable

x= 1000

def func1(n):
    global x
    x=10
    print(n,x)

def func2(n):
    global x
    x = 200
    print(n,x)

func1(4)
print(x)
func2(11)
print (x)




