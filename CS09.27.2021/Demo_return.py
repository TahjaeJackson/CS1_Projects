# Author: Tahjae Jackson
# Date: September 27, 2021
# Purpose: Demo return statement

def func(n,m):
    return (n+m) #when you execute a return statement, you will get kicked out of the function.

# x = (func (100,200) + func(10,20))
# print(x)

# print(func(func(100,200),func(10,20)))

a1 = func(100,200)
a2 = func(10,20)
x = func(a1,a2)
print(x)

"""return statements can be used in place of a break. The main difference is that break statments only work in a loop, while return 
can get you out of a function"""