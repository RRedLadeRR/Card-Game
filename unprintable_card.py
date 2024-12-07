class Card:

    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    suits = [u"\u2660", u"\u2663", u"\u2665", u"\u2666"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep
    
class Unprintable_Card(Card):

    def __str__(self):
        return "<Cant be printed>"