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


my_hand = Hand()
print(my_hand.get_score(['Ah', 'Ad', '6s']))
