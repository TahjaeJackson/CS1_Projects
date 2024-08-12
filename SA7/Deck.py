# Name: Tahjae Jackson
# Date: October 19, 2021
# Purpose: To create the class of the Deck


from random import *
from Card import *

CARDTOTAL = 52 #Maximum number of cards
CARDLIM = 13 #Maximum number of cards per type



# Purpose: To create a class to execute the functionality of a deck and dealing cards

class Deck:

    # This creates a list to store the cards within the object
    def __init__(self):
        self.card_list = []

    def add_standard_cards(self):
        x = 1
        y = 1

        # appending of cards to the pack
        while y <= 4:
            d = Card(x, y)
            self.card_list.append(d)
            if x == CARDLIM:
                y += 1
                x = 0

            x += 1


    # shuffling the cards
    def shuffle(self):
        min = 0
        max = len(self.card_list)-1
        for z in range(min, max):
            indx = randint(min, max)

            # swapping the locating of cards randomly
            temp = self.card_list[z]
            self.card_list[z] = self.card_list[indx]
            self.card_list[indx] = temp


    # function that is used to deal a certain number of cards and to display those cards
    def deal(self, num = 0):
        hand = Deck()
        for z in range(len(self.card_list)-1,len(self.card_list)-num-1, -1):
            hand.card_list.append(self.card_list[z])
            del self.card_list[z]

        return hand






