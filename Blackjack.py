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

    def __init__(self,  count, input_deck=DECK):
        self.deck = input_deck
        self.hand = self.deck.deal_a_card(count)

    def get_new_card(self):
        self.hand += self.deck.deal_a_card()

    @property
    def hand_points(self):
        return self.deck.get_score(self.hand)

    def __str__(self):
        return f'{len(self.hand)} cards in hand: {self.hand} worth: {self.hand_points}'


my_hand = Hand(2)


class Player:
    """
    Player object accessing a Hand class
    representing the player info and stats
    """

    def __init__(self, name='Player', buyin=100):

        self.name = name
        self.chips = buyin
        self.hand = Hand(2)

        logging.info(self)

    def wager(self, amount):
        self.chips -= amount
        self.betting = amount
        print(f'{self.name} wagers: ${amount} and has ${self.chips} remaining')

    def hit(self):
        """Player hand receives a card from the deck"""
        self.hand.get_new_card()
        print(self)

    def stay(self):
        """Player ends round with his current score"""
        print(f'{self.name} stays with {self.hand}')
        return self.hand.hand_points

    def cashout(self):
        """leave table with chips"""
        return (
            f'{self.name} exits with ${self.chips}.\n\t'
        )

    def __str__(self):

        return (
            f'\n({self.name}: ${self.chips}) has: \n\t{self.hand}\n'
        )


class Dealer(Player):
    """
    similar to Player, but less options, and house always covers player
    """

    def __init__(self):
        super().__init__()
        self.name = 'Dealer'
        self.chips = 1_000_000_000_000
        self.hand = Hand(1)

    def __str__(self):

        return (
            f'\n({self.name}: has: \n\t{self.hand}\n'
        )


me = Player()


def register_player():
    """
    build player data
    """
    username = input('Username: ')
    buyin = int(input('Buyin: > $'))
    return username, buyin


def payout_wagers():
    """award wins"""
    pass


def blackjack():
    """
    game logic
    """
    print('Welcome to Blackjack!')
    seat_one = Player(*register_player())
    dealer = Dealer()
    logging.info(seat_one)
    logging.info(dealer)
    print(f'{dealer}')
    print(f'{seat_one}')

    seat_one_bet_amount = int(
        input('How much do you wish to wager this round?  $')
    )
    if seat_one_bet_amount > seat_one.chips:
        raise Exception(
            f'{seat_one.name}, you cant bet so much! Bet at most ${seat_one.chips}.')
    else:
        seat_one.wager(seat_one_bet_amount)

    # try:
    #     bet_amount = int(
    #         input('How much do you want to wager this round? : > $'))
    #     assert bet_amount <= seat_one.chips, "You can't bet so much!"

    #     seat_one.wager(bet_amount)
    # except:
    #     f"You can't bet so much! Please bet less than ${seat_one.chips}"

    # while seat_one.hand.hand_points <= 21:

    #     player_action = input('[H]it or [S]tay? >').upper()

    #     if player_action == 'H':
    #         seat_one.hit()

    #     elif player_action == 'S':
    #         player_score = seat_one.stay()
    #         logging.info(player_score)

    #         break

    #     else:
    #         print(f'{player_action} not recognized...')

    # if seat_one.hand.hand_points > 21:
    #     print(f'{seat_one} BUSTED!!')

    # while dealer.hand.hand_points < 17:
    #     #  some games have the dealer hit on soft 17 ie ['Ax', '6']
    #     #  this house advantage is not applied here. See README ref #3
    #     dealer.hit()

    # dealer_score = dealer.stay()
    # logging.debug(dealer_score)

    # if player_score > dealer_score:
    #     print(f'{seat_one} wins! Awarded the pot of XXX')
    # elif player_score == dealer_score:
    #     print('PUSH!')
    # else:
    #     print(f'Sorry {seat_one.name}, you lose this round.')


blackjack()
