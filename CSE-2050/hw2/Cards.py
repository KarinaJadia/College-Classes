import random

class Card:
    def __init__ (self, value, suit):
        """
        the constructor
        """
        self.value = value # the value of a card (the 3 in 3 of diamonds)
        self.suit = suit # the suit of a card (the diamonds in 3 of diamonds)
    
    def getVal (self):
        """
        value getter (made so that I can access values for all cards)
        """
        return self.value
    
    def getSuit (self):
        """
        suit getter (made so that I can access suits for all cards)
        """
        return self.suit
    
    def repr (self):
        """
        returns the information of the card in the form [value] of [suit]
        for example if value = 4 and suit = clubs, it would say "4 of clubs"
        """
        return f'{self.value} of {self.suit}'
    
    def __lt__ (self, other):
        """
        sorts cards by suits, then values in this order:
        spades > hearts > diamonds > clubs
        ace > king > queen > jack > 10-1
        """

        if self.getSuit() < other.getSuit(): # tests the suits and returns true if first suit is smaller than second
            return True
        elif self.getSuit() > other.getSuit():
            return False
        else: # comes here if they have the same suit
            if self.getVal() < other.getVal():
                return True
            else:
                return False

    def __eq__ (self, other):
        """
        checks if a card equals a card
        """
        if self.repr() == other.repr(): # checks if their string representations are equal
            return True
        else:
            return False


class Deck:
    def __init__ (self, values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13), suits = ('clubs', 'diamonds', 'hearts', 'spades')):
        self.values = values
        self.suits = suits
        self.card_list = []
        for suit in self.suits:
            for val in self.values:
                self.card_list.append(Card(val, suit))
    
    def __len__ (self):
        """
        returns the length of the card list
        creates a counter and iterates through card list, adds 1 to counter for each element in card list
        """
        counter = 0
        for card in self.card_list:
            counter += 1
        return counter

    def sort (self):
        """
        sorts the card list from least to greatest
        I just called the python sort method and it worked
        """
        self.card_list.sort()
        return self.card_list

    def __repr__ (self):
        """
        gives card_list a string representation by creating one giant string of all cards and returning that
        """
        st = 'deck: ' # the giant string that will be filled with each card
        for c in self.card_list:
            st = st + '(' + c.repr() + ') ' # adds each card's string representation to the main string
        return st

    def shuffle (self):
        """
        shuffles the deck card list using the shuffle method from the random module
        """
        random.shuffle(self.card_list)
        return self.card_list

    def draw_top (self):
        """
        removes the last element on the card list and returns it
        """
        try:
            x = self.card_list[-1] # takes the last element and puts it into a variable
            self.card_list.pop() # removes the last element
            return x.repr() # returns the card in string form
        except:
            return 'error: cannot draw from empty deck'


class Hand (Deck):
    def __init__ (self, values, suits):
        super().__init__(values, suits)
        self.card_list = []
        for suit in suits:
            for val in values:
                self.card_list.append(Card(val, suit))

    def __repr__ (self):
        """
        returns string representation of the card list
        """
        st = 'hand: '
        for c in self.card_list:
            st = st + '(' + c.repr() + ') ' # adds each card's string representation to the main string
        return st

    def play(self, Card):
        """
        returns a specific card and removes it from hand
        """
        try:
            self.card_list.remove(Card) # removes specified card
            return Card.repr() # returns a string representation of removed card
        except:
            return 'error: card does not exist'