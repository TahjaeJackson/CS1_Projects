# Author: Tahjae Jackson
# Date: September 30, 2021
# Purpose: Question 5

"""
Define a function cs1_asterisk_prefix that takes a positive integer n
as a parameter and prints n lines of text where each line has some number of asterisks (*)
followed by “cs1”. The number of asterisks in each line should be as follows:
1. The first line should have one asterisk before the string “cs1”. So the first line should
be “*cs1”.
2. In every subsequent line that number of asterisks preceding “cs1” should increase by
one. So the second line should be “**cs1”, third line should be “***cs1” and the
pattern continues for the subsequent lines of text.
For example:
1. if n = 5, the pattern printed by your function should look like:
*cs1
**cs1
***cs1
****cs1
*****cs1
2. if n = 1, the pattern printed by your function should look like:
*cs1

"""

#Purpose: To print n lines of text where each line has some number of asterisks (*)nfollowed by “cs1”
#Parameters: A positive integer, n

def cs1_asterick_prefix(n):
    count = 1
    astericks = ""
    num_astericks = 1
    while count <= n:
        while num_astericks <= count:
            astericks = astericks + "*"
            num_astericks += 1
        print(astericks + "cs1")
        count += 1

cs1_asterick_prefix(10)
