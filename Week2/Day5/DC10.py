# Part 1 : Quizz :
# Answer the following questions

# What is a class?
# It’s a blueprint or a template for creating objects 

# What is an instance? 
# It is a copy of the class with actual values, literally an object belonging to a specific class

# What is encapsulation?
# It is a concept used to bundle data and methods into easy-to-use units

# What is abstraction?
# It is the process of simplifying complex systems by modeling classes based on the essential properties and behaviors they possess

# What is inheritance?
# It is the process by which one class takes on the attributes and methods of another.

# What is multiple inheritance?
# That's when a class can inherit from two different classes

# What is polymorphism?
# The ability to use a standard interface for multiple forms or data types

# What is method resolution order or MRO?
# It is the order in which a method is searched for in a classes hierarchy



# Part 2: Create A Deck Of Cards Class.
# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:

# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.

import random

class DeckOfCards:
    def __init__(self):
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.deck = self._generate_deck()

    def _generate_deck(self):
        return [{'suit': suit, 'value': value} for suit in self.suits for value in self.values]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        if not self.deck:
            print("No cards left in the deck.")
            return None
        return self.deck.pop()

deck = DeckOfCards()
print(deck.deck)

deck.shuffle()
print(deck.deck)

dealt_card = deck.deal()
print(dealt_card)

print(deck.deck)
