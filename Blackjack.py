"""
basic blackjack game. 
"""

# TODO: recreate, re-shuffle exhausted deck

from FrenchDeck import Cards
import logging

logging.basicConfig(filename='blackjack.log', level=logging.INFO,
                    format='%(levelname)s:%(message)s')

DECK = Cards()
logging.debug(DECK)

class Hand:
    """
    functionality of the player hands 
    """
    @staticmethod
    def get_blackjack_score(cards):
        """lookup and score blackjack hands independent of instances"""
        


