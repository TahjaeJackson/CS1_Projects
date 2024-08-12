# Name: Tahjae Jackson
# Date: October 17, 2021
# Purpose: Using classes and objects to create a functioning timer. This class is specifically for counting down



# Purpose: To count down

class Counter:
    def __init__(self, limit, initial = 0, min_digits = 1):
        self.limit = limit
        self.min_digits = min_digits
        if initial in range(0, limit):
            self.counter = int(initial)
        else:
            self.counter = int(limit - 1)
            print("THIS INITIAL VALUE IS NOT IN RANGE")



    def get_value(self):  #This returns the counters value as an integer
        return self.counter


    # Purpose: To continuosly subtract one from the countdown
    # Parameter: the memory address
    # Return: A boolean that states whether the count has started over

    def tick(self):

        self.counter = self.counter - 1
        wraparound = False
        if self.counter < 0:
            self.counter = (self.limit - 1)
            wraparound = True

        return wraparound

    # Purpose: To convert the integer to a string
    # Parameter: the memory address
    # Return: The converted string

    def __str__(self):
        num_string = str(self.counter)
        if len(num_string) < self.min_digits:
            for i in range(0,self.min_digits-len(num_string)):
                num_string = "0" + num_string

        return num_string




