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

class Positionable_Card(Card):

    def __init__(self, rank, suit, face_up = True):
        super().__init__(rank, suit)
        self.is_face_up = face_up
    def __str__(self):
        if self.is_face_up:
            rep = super().__str__()
        else:
            rep = "▮▮"
        return rep
    def flip(self):
        self.is_face_up = not self.is_face_up

card1 = Card("A", Card.suits[0])
card2 = Unprintable_Card("A", Card.suits[1])
card3 = Positionable_Card("A", Card.suits[2])
print("\nPrinting Card object: ")
print(card1)
print("\nPrinting object Unprintable_Card: ")
print(card2)
print("\nPrinting object Positionable_Card: ")
print(card3)
print("\nFliping object Positionable_Card")
card3.flip()
print("\nPrinting object Positionable_Card:")
print(card3)



# class Hand:

#     def __init__(self):
#         self.cards = []

#     def __str__(self):
#         if self.cards:
#             rep = ""
#             for card in self.cards:
#                 rep += str(card) + "\t"
#         else:
#             rep = "<empty>"
#         return rep
    
#     def clear(self):
#         self.cards = []

#     def add(self, card):
#         self.cards.append(card)

#     def give(self, card, other_hand):
#         self.cards.remove(card)
#         other_hand.add(card)

# class Deck(Hand):

#     def populate(self):
#         for suit in Card.suits:
#             for rank in Card.ranks:
#                 self.add(Card(rank,suit))

#     def shuffle(self):
#         import random
#         random.shuffle(self.cards)

#     def deal(self, hands, per_hand = 1):
#         for rounds in range(per_hand):
#             for hand in hands:
#                 if self.cards:
#                     top_card = self.cards[0]
#                     self.give(top_card, hand)
#                 else:
#                     print("No cards left")

# deck1 = Deck()
# print("New deck created")
# print("Here is new deck:")
# print(deck1)

# deck1.populate()
# print("\nNew cards in deck apeared")
# print("Here how it looks now:")
# print(deck1)

# deck1.shuffle()
# print("\nDeck shuffled")
# print("Here how it looks now")
# print(deck1)

# my_hand = Hand()
# your_hand = Hand()
# hands = [my_hand, your_hand]
# deck1.deal(hands, per_hand = 5)
# print("\nWe get 5 more cards")
# print("My cards: ")
# print(my_hand)
# print("your_hand")
# print(your_hand)
# print("In deck left: ")
# print(deck1)

# deck1.clear()
# print("\nDeck is empty")
# print("Here how it looks now:", deck1)





# card1 = Card(rank="A", suit=Card.suits[0])
# print("Printing object-card on screen ")
# print(card1)

# card2 = Card(rank="2", suit=Card.suits[0])
# card3 = Card(rank="3", suit=Card.suits[0])
# card4 = Card(rank="4", suit=Card.suits[0])
# card5 = Card(rank="5", suit=Card.suits[0])
# print("\nPrinting 4 more cards: ")
# print(card2)
# print(card3)
# print(card4)
# print(card5)

# my_hand = Hand()
# print("\nPrinting card, that i have before deal")
# print(my_hand)

# my_hand.add(card1)
# my_hand.add(card2)
# my_hand.add(card3)
# my_hand.add(card4)
# my_hand.add(card5)
# print("\nPrinting five new cards: ")
# print(my_hand)

# your_hand = Hand()
# my_hand.give(card1, your_hand)
# my_hand.give(card2, your_hand)
# print("\nMy first 2 cards i gave you")
# print("Now in your hands: ")
# print(your_hand)
# print("And in my hands:")
# print(my_hand)

# my_hand.clear()
# print("\nCard in my hands after i droped all cards: ")
# print(my_hand)