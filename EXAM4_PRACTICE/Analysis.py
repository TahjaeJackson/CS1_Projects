# Name: Tahjae Jackson
# Date: November 9, 2021
# Purpose:



def func1(n): #O(n)
   count = 0
   for i in range(n):
       count = count + 2
   print(count)

def func2(n): #O(n)
   i = 3
   while i < n:
       i = i + 1

def func3(n): #O(n)
   i = 0
   while i < n-3:
       i = i + 1

def func4(n): #O(log n)
   i = 1
   while i < n:
       i = i * 3

def func5(n): #O(log n)
   i = n
   while i > 1:
       i = i // 10

def func6(n): #O(n^2)
   i = 0
   while i < n:
       j = 0
       while j < n:
           print(i, j)
           j = j + 1

       i = i + 1

def func7(n): #O(n)
   i = 0
   while i < n:
       j = 0
       while j < 5: #This loop runs constant times
           print(i, j)
           j = j + 1
       i = i + 1

def func8(n): #O(n^2)
   i = 0
   while i < n:
       j = n
       while j > 0:
           print(i, j)
           j = j - 1

       i = i + 1

def func9(n): # O(n log(n))
   i = 1
   while i < n: #This loop runs log(n) times
       j = 0
       while j < n: #This loop runs n times
           print(i, j)
           j = j + 1

       i = i * 10


def func10(n):#O(n log(n))
   i = 1
   while i < n: #This loop runs n times
       j = 1
       while j < n:#This loop runs log(n) times
           print(i, j)
           j = j * 2

       i = i + 1


#With lists
def func11(glist): #O(n) where n = len(glist)
   i = 0
   while i < len(glist):
       print(glist[i])
       i = i + 1



def func12(glist): #O(log n) where n = len(glist)
   m = len(glist)-1
   while m > 0:
       print(glist[m])
       m = m // 2


def func13(glist): #O(n ^ 2) where n = len(glist)
   i = 1
   while i < len(glist):
       print(glist[i:]) #Slicing is O(n)
       i = i + 1

def func14(glist): #O(n log n) where n = len(glist)
   for i in range(len(glist)):
       m = len(glist) - 1
       while m > 0:
           print(glist[m])
           m = m // 2

def func15(glist): #O(n^2) where n = len(glist)
   for i in range(len(glist)):
       for j in range(len(glist)):
           if glist[i] == glist[j] and i != j:
               print(i, j)



#Recursion

def func16(n): #O(n)
   if n <= 1:
       return 1
   return n * func16(n - 1)

def func17(n): #O(log n)
   if n == 0:
       return 1
   else:
       return func17(n//2)






#Assume both m and n are positive integers
def func18(n, m): #O(n + m)
   print("yes")
   if n == 1  and m == 1:
       return

   if n == 1:
       func18(n, m-1)
   else:
       func18(n-1, m)


def func19(n): #O(n^2)
   i = 0
   j = 0
   while i < n: #This condition is checked n2 times because i gets reset to 0 in the body of the if condition.
       i = i + 1
       if i == n-1 and j < n: #This condition becomes true n times
           i = 0
           j = j + 1


def func20(n): #O(1)
   if n > 10 or n < 0:
       return 0

   return n + func20(n+1)




def func21(glist): #O(n^2) where n = len(glist)
   if len(glist) == 0:
       return 1

   return glist[-1]*func21(glist[:len(glist)-1])


def func22(glist, i = 0): #O(n) where n = len(glist)
   if i == len(glist):
       return 0
   return glist[i] + func22(glist, i + 1)


#Dictionary examples. Assume gdict is a dictionary in the following questions

def func23(gdict, val): #O(n) where n = len(gdict)
   for k in gdict:
       print(k)
       if gdict[k] == val:
            return True


   else:
       return False


#
# dict = {1:3, 2:4, 3:5, 4:8, 5:12 }
# func23(dict,12)


def func24(gdict1, gdict2): #O(n)
   # Runtime of len is O(1)
   if len(gdict1) != len(gdict2):
       return False

   for k in gdict1:#This loop runs O(n)times
       if k in gdict2: #This check is O(1)in dictionaries
           if gdict1[k] != gdict2[k]:
               return False
       else:
           return False

   return True


def func25(glist): #O(n)
   d = deque()

   for x in glist:
       d.appendleft(x)

   return d


def func26(d, glist): #O(m^2 * n)   #Assume d is a deque
   for x in glist:
       if x in d:
           d.remove(x)
