# Name: Tahjae Jackson
# Date: October 19, 2021
# Purpose: To create a class handles the functionality of each card

class Card:

    def __init__(self, cardnum, cardtype):
        self.cardnum = str(cardnum)
        self.cardtype = cardtype


    def __str__(self):

        # The following nested if statement decides what type of card is chosen
        if self.cardtype == 1:
            type = "clubs"
        elif self.cardtype == 2:
            type = "spades"
        elif self.cardtype == 3:
            type = "diamonds"
        elif self.cardtype == 4:
            type = "hearts"

        # The following nested if statement decides which type of non-numerical card is choosen
        self.cardnum = str(self.cardnum)
        if self.cardnum == "11":
            self.cardnum = "Jack"
        elif self.cardnum == "12":
            self.cardnum = "Queen"
        elif self.cardnum == "13":
            self.cardnum = "King"


        return ((self.cardnum) + " of " + type + "\n")