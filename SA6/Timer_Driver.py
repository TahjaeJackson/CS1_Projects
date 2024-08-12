# Name: Tahjae Jackson
# Date: October 17, 2021
# Purpose: To create a driver for the timer class

from Timer_Class import *

hr = 1
min = 30
sec = 0
timer1 = Timer(hr, min, sec)
fp = open("TimerOutput","w")

while ( hr != 0) or (min != 0) or (sec != 0):
    print(timer1)
    timer1.tick_timer()
    if timer1.is_zero():
        break
    fp.write(str(timer1) + "\n")

fp.close()

