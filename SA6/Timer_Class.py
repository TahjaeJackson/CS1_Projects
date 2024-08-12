# Name: Tahjae Jackson
# Date: October 17, 2021
# Purpose: To create a class for the timer

from Counter_Class import *
HOURS_LIM = 24
MIN_LIM = 60
SEC_LIM = 60
MIN_DIGITS = 2

class Timer:
    def __init__(self, hours, minutes, seconds):
        self.hours = Counter(HOURS_LIM, hours, MIN_DIGITS)
        self.minutes = Counter(MIN_LIM, minutes, MIN_DIGITS)
        self.seconds = Counter(SEC_LIM, seconds, MIN_DIGITS)

    def __str__(self):
        time = str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)
        return time

    def tick_timer(self):
        self.zero = False
        if self.seconds.tick():
            if self.minutes.tick():
                if self.hours.tick():
                    self.zero = True



    def is_zero(self):
        if self.zero:
            return self.zero