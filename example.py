"""demo game for bootcamp milestone project"""
from random import shuffle

class Deck:

    """build standard 52-card deck, shuffle in place, ready for play"""
    def __init__(self):
        self._deck = self.make_deck()
        shuffle(self._deck)

    @classmethod
    def make_deck(cls):
        """make a new deck of cards"""
        _card_ranks = [str(n) for n in range(2, 10)] + list('TJQKA')
        _card_suits = 'c h d s'.split()  # idiomatic syntax, clubs, hearts, etc
        new_deck = [  # self.deck or ._deck?
            (f'{rank}{suit}')
            for rank in _card_ranks
            for suit in _card_suits
        ]
        return new_deck
        
    def deal_a_card(self):
        """return a random card to the caller"""
        return self._deck.pop()

my_deck = Deck()

class Hand:
    """individual players hands"""
    
    def __init__(self): # (hand=[], hand=[my_deck.deal_a_card(), my_deck.deal_a_card()])
        # self.hand = []
        # self.hand.append(my_deck.deal_a_card(), my_deck.deal_a_card())
        self.hand = [my_deck.deal_a_card(), my_deck.deal_a_card()]
