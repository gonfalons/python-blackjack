"""
Build a standard playing card deck from scratch, built for Blackjack
Shuffled (insecurely) on instantiation
"""

from random import shuffle


class Cards:

    """
    Simulated French Deck, with the standard 52-card deck capabilities.
    Used for "single-shoe" (one deck) blackjack simulation
    """

    _card_ranks = [str(n) for n in range(2, 10)] + list('TJQKA')
    _card_suits = 'c h d s'.split()  # idiomatic syntax, clubs, hearts, etc

    def __init__(self):
        """build standard 52-card deck, shuffle in place, ready for play"""

        self._deck = [
            (f'{rank}{suit}')
            for rank in self._card_ranks
            for suit in self._card_suits
        ]

        shuffle(self._deck)

    def _deal_a_card(self):
        """bottom-dealing is insecure but functional!"""
        try:
            return self._deck.pop()

        except:
            #  TODO: handle exhausted deck
            print('WARNING! Deck is out of cards!')
            print(f'{self}')

    def __len__(self):
        return len(self._deck)

    def __str__(self):
        return f'{len(self)} cards in the deck: \n {self._deck}'
