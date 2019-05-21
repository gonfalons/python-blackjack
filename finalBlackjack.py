from random import shuffle
import logging

logging.basicConfig(filename='blackjack.log', level=logging.INFO,
                    format='%(levelname)s:%(message)s')


class Deck:
    """
    Deck will populate cards and deal them out to Hands
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
logging.debug(DECK)


class Hand:
    """
    Hand will need access to the Deck objects.
    """

    def __init__(self, amount=2,input_deck=DECK):
        self.deck = input_deck
        self.hand = self.deck.deal_a_card(amount)

    def get_new_card(self):
        self.hand += self.deck.deal_a_card()

    @property
    def hand_points(self):
        return self.deck.get_score(self.hand)

    def __str__(self):
        return f'{len(self.hand)} cards in hand: {self.hand} worth: {self.hand_points}'


my_hand = Hand()


class Player:
    """
    Player will need access to Hand objects
    """

    def __init__(self, hand_cls=Hand):
        self.hand = Hand()
        logging.info(self.hand)

    def hit(self):
        self.hand.get_new_card()
        logging.info(self.hand)

    def __str__(self):
        pass


me = Player()
me.hit()
