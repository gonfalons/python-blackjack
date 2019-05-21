from random import shuffle
"""
basic blackjack game (over) using classes for milestone project
"""

import logging

logging.basicConfig(filename='blackjack.log', level=logging.DEBUG,
                    format='%(levelname)s:%(message)s')


class Deck:
    """
    deck
    """

    def __init__(self):
        """build standard 52-card deck, shuffle in place, ready for play"""

        self._deck = self.make_deck()
        shuffle(self._deck)
        logging.debug(self._deck)

    @staticmethod
    def make_deck():
        """make a new deck of cards"""
        _card_ranks = [str(n) for n in range(2, 10)] + list('TJQKA')
        _card_suits = 'c h d s'.split()  # idiomatic syntax, clubs, hearts, etc
        new_deck = [  # self.deck or ._deck?
            (f'{rank}{suit}')
            for rank in _card_ranks
            for suit in _card_suits
        ]
        return new_deck

    def deal_a_card(self, amount=1):
        """return a random card to the caller"""
        cards = []
        for _ in range(amount):
            try:
                cards.append(self._deck.pop())
            except:  # TODO: test. Handle exhausted deck
                print('DECK EXHAUSTED')

        return cards

    @staticmethod
    def get_score(cards):
        """lookup and score blackjack hands independent of instances"""
        num_aces = 0
        total_score = 0

        scores = {
            'A': 11,
            'K': 10, 'Q': 10, 'J': 10, 'T': 10,
            '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2
        }

        for card in cards:
            if card[0] == 'A':
                num_aces += 1
            total_score += scores.get(card[0])

            if total_score > 21 and num_aces:
                total_score -= 10
                num_aces -= 1

        return total_score

    def __str__(self):
        return f'{len(self._deck)} cards in deck: {self._deck}'


DECK = Deck()


class Hand:
    """represent the individual player hands"""

    def __init__(self, DECK: Deck):

        self.hand = DECK.deal_a_card(2)

    def __len__(self):
        return len(self.hand)

    def __str__(self):
        return (
            f'{len(self)} cards:\n\t {self.hand} worth:\n\t '
            f'{DECK.get_score(self.hand)}'
        )


class Player:
    """owners of hands/chips/actions"""

    def __init__(self, name='Player'):
        self.hand_class = Hand(DECK)

    def hit_me(self):
        """ hitting is adding a card to player's Hand from the Deck """
        self.hand_class.deal_a_card()

    def __str__(self):
        return (
            f'{self.hand_class}'
        )


me = Player()
print(me.hand_class)

me.hit_me()
print(me)
