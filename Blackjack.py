"""
TDD basic blackjack game using pytest
"""

# TODO: recreate, re-shuffle exhausted deck

from FrenchDeck import Cards
import logging

logging.basicConfig(filename='blackjack.log', level=logging.DEBUG,
                    format='%(levelname)s:%(message)s')

DECK = Cards()
logging.debug(DECK)


class Hand:
    """
    functionality of the player hands 
    """

    #  TODO: inherit from Deck?

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

    def __init__(self):
        """start with two cards from the deck"""

        #  TODO: init empty hand, or populate on init?
        #  TODO: use DECK or set as parameter for class?
        # self.cards = []
        self.cards = [DECK._deal_a_card(), DECK._deal_a_card()]
        logging.debug(self.cards)

    def receive_card(self):
        """ 'Hitting' delivers another card to hand """
        self.cards.append(DECK._deal_a_card())

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return f'{len(self.cards)} cards: {self.cards}'


my_hand = Hand()
print(my_hand.cards)


class Player:
    """player functions and properties"""

    def __init__(self, name, buyin_amount):
        self.name = name.capitalize()
        self.chips = buyin_amount
        self.hand = Hand()
        logging.debug(
            f'{self.name} buys in for ${self.chips} and is dealt {self.hand}')


my_player = Player('debug player', 100)

