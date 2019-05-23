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

    # @decorator
    # def blackjack(self):
    #     if len(self.hand) == 2 and self.hand.hand_points == 21:
    #         print('BLACKJACK!')

    @property
    def points(self):
        """blackjack point score of the hand"""
        return self.deck.get_score(self.hand)

    def __len__(self):
        return len(self.hand)

    def __str__(self):
        return f'{len(self.hand)} cards in hand: {self.hand} worth: {self.points}'

    # def __repr__(self):
    #     return Hand(len(self), self.deck)


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
        return self.hand.points

    def cashout(self):
        """leave table with chips"""
        return (
            f'{self.name} exits with ${self.chips}.\n\t'
        )

    def __str__(self):

        return (
            f'\n({self.name}: ${self.chips}) has: \n\t{self.hand}\n'
        )

    # def __repr__(self):
    #     return Player(self.name, self.buyin, self.hand=Hand(2))


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
    # SETUP
    print('\n****\nWelcome to Blackjack!\n*****\n')
    seat_one = Player(*register_player())
    dealer = Dealer()
    logging.info(seat_one)
    logging.info(dealer)
    # END SETUP

    # ROUND START

    bet_amount = int(
        input('How much do you wish to wager this round?  $')
    )

    logging.debug(
        f'seat_one is betting: ${bet_amount}, has ${seat_one.chips} before bet'
    )

    if bet_amount > seat_one.chips:
        raise BetExceedsHoldingsError(
            f'${seat_one.chips} is the max bet, add-on more chips to increase wager'
        )
    else:
        seat_one.wager(bet_amount)
        print(f'{dealer}\n')
        print(f'{seat_one}\n')

    if seat_one.hand.points == 21 and len(seat_one.hand) == 2:
        print(f'{seat_one.hand} ! BLACKJACK!!')
        seat_one.chips += bet_amount * 2.5

    while seat_one.hand.points <= 21:
        player_action = input('[H]it or [S]tay? >').upper()

        if player_action == 'H':
            seat_one.hit()

            if seat_one.hand.points > 21:
                print(f'\n{seat_one} BUSTED!!You lose.\n')
                break

        elif player_action == 'S':
            player_score = seat_one.stay()
            logging.info(player_score)

            break

        else:
            print(f'{player_action} not recognized...')

    while dealer.hand.points < 17:
        #  some games have the dealer hit on soft 17 ie ['Ax', '6']
        #  this house advantage is not applied here. See README ref #3
        dealer.hit()

        if dealer.hand.points > 21:

            print(f'Dealer busted! Player Wins!')

            seat_one.chips += bet_amount * 2.5

            print(f'${seat_one.chips} is your new balance!')

            break

        else:
            print(f'\nSHOWDOWN\n'.center(25, '*'))
            print(f'Dealer has: {dealer}\nPlayer has: {seat_one}')

            if dealer.hand.points > seat_one.hand.points:
                print(f'Sorry, player! House wins')

            elif dealer.hand.points == seat_one.hand.points:
                print(f'It is a push on {seat_one.hand.points}')
            else:
                print(f'Player wins! \n')
                seat_one.chips += bet_amount * 2
                print(f'${seat_one.chips} new balance.')

        # play_again = input('\n\tPlay Again? [Y]/[N] >')
        # if play_again == 'Y':
        #     play_again()
        # else:
        #     print(seat_one.cashout())

    # ROUND END


class BetExceedsHoldingsError(ValueError):
    """
    raise a custom error invalidating attempted illegal bets,
    where the bet amount is greater than the players chips on
    the table. The only exception is if a double-down or split 
    rule is implemented, which is not yet the case.
    """


blackjack()
