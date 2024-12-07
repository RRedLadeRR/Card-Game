from card import Card

from unprintable_card import Unprintable_Card

from positionable_card import Positionable_Card

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