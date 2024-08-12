# Author: Tahjae Jackson
# Date: 09/20/2021
# Purpose: Fibanacci

#1 1 2 3 5 8 13 21  [fibanacci series)
n = 5
f1 = 1
f2 = 1
count=0
limit = 100

while f1 < limit:
    print(f1)
    count += 1
    new = f1 + f2
    f1 = f2
    f2 = new
