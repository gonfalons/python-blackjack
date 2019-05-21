"""
basic python blackjack
intentional over-use of classes
"""
from random import shuffle
import logging
logging.basicConfig(filename='blackjack.log', level=logging.DEBUG,
                    format='%(levelname)s:%(message)s')


def register_players():
    """print greeting, get player names, buyins"""
    print('Welcome to Blackjack! Closest to 21 wins! Good Luck!\n')
    player_name = input('What is your  name?')
    player_buyin = int(input('How much will you be buying in for today? > $'))
    return player_name, player_buyin


test_register_players = ('testplayer', 500)


class Blackjack:
    """
    one class to rule them all
    parent class for all game objects (players, chips, hands)
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
            cards.append(self._deck.pop())
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


DECK = Blackjack()


class Hand():
    """represent the individual player hands"""

    def __init__(self, deck: DECK):
        self.hand = deck.deal_a_card(2)
        print(self.hand)


my_hand = Hand(DECK)
print(my_hand)
# test = Blackjack()

# class Player:
#     def __init__(self, name, buyin):
#         self.name = name
#         self.chips = buyin
#         # self.hand = Hand()

#     # @classmethod
#     # def from_register_make_player(cls, player_info):
#     #     return cls(*player_info)

# class Fruits:
