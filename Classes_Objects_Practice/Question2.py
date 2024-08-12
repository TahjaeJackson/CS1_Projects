# Name: Tahjae Jackson
# Date: October 17, 2021
# Purpose: Using classes and objects to create a functioning timer. This class is specifically for counting down

# Define a Bubbleset class that has only one instance variable blist. The instance variable blist must be a list that has
# references to Bubble objects as elements. Your Bubbleset class must include the following methods:

# 1. (3 points) __init__(self, n): This method must create n Bubble objects and add their references to instance variable blist.
# Every bubble must start at the center point of the bottom boundary of your graphics window. For example in the video I use x = 200 and
# y = 400 as the starting point for all the bubbles.

# 2. (3 points) update(self): This method should update the bubble objects stored in instance variable blist by calling the
# update method defined in Bubble class on each of the bubble objects in blist.

# 3. (3 points) draw(self): This method should draw the bubble objects stored in instance variable blist by calling the draw
# method defined in Bubble class on each of the bubble objects in blist.

# 4. (3 points) add_bubbles(self, n):This method should add n Bubble objects to instance variable blist. All the bubbles
# added must start at the center point of the bottom boundary of your graphics window. For example in the video I use x = 200
# and y = 400 as the starting point of all the bubbles.

# 5. (3 points) pop_bubbles(self, x, y):This method should find Bubble objects in blist whose center is located at (x, y)
# and mark them as popped using pop_bubble method of Bubble class.

# 6. (5 points) remove_popped_bubbles(self): This method should find Bubble objects in blist that are popped and remove them from blist.

from Question1 import *

class Bubbleset:
    def __init__(self,n):
        list = []
        for i in range(0,n):

