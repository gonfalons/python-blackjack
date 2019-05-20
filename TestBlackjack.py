"""
test-driven development + user story
"""
from Blackjack import (
    DECK,
    Hand,
)


### ------------------------DECK TESTS-------------------------------------- ###

def test_full_deck():
    """full 52-card deck"""
    assert len(DECK) == 52


def test_deal_random_cards():
    """check several lists of cards dealt"""
    one_card = [DECK._deal_a_card()]
    two_cards = [DECK._deal_a_card(), DECK._deal_a_card()]
    five_cards = [
        DECK._deal_a_card(), DECK._deal_a_card(), DECK._deal_a_card(
        ), DECK._deal_a_card(), DECK._deal_a_card(),
    ]
    assert len(one_card) == 1
    assert len(two_cards) == 2
    assert len(five_cards) == 5
    print(f'-{one_card}-\n-{two_cards}-\n-{five_cards}-')


def test_fair_dealing():
    """make sure all cards dealt are removed from deck, no repeats"""
    hitme = DECK._deal_a_card
    ten_cards = [
        hitme(), hitme(), hitme(), hitme(), hitme(
        ), hitme(), hitme(), hitme(), hitme(), hitme()
    ]
    ten_again = [
        hitme(), hitme(), hitme(), hitme(), hitme(
        ), hitme(), hitme(), hitme(), hitme(), hitme()
    ]
    for card in ten_cards:
        assert card not in ten_again


def test_deck_length():
    """make sure deck has been dealing out cards as expected"""
    assert len(DECK) == (
        24)  # dealt one, two, five, ten, ten cards == 52 starting cards - 28 dealt = 24


def test_deck_renews_after_exhausted():
    """recreate, re-shuffle deck afterwards"""
    pass


### ------------------------HAND TESTS-------------------------------------- ###
def test_hand_score_lookup():
    """test a variety of hand combinations to make sure they are scored properly"""

    five_pts = ['2c', '3s']
    assert Hand.get_blackjack_score(five_pts) == 5

    twelve_pts = ['As', 'Ac', 'Td']
    assert Hand.get_blackjack_score(twelve_pts) == 12

    thirteen_pts = ['Ad', '2s', 'Tc']
    assert Hand.get_blackjack_score(thirteen_pts) == 13

    fourteen_pts = ['Ah', 'Ad', 'Ac', 'As', 'Tc']
    assert Hand.get_blackjack_score(fourteen_pts) == 14

    nineteen_pts = ['Ac', '8d']
    assert Hand.get_blackjack_score(nineteen_pts) == 19

    bj = ['Js', 'Ac']
    assert Hand.get_blackjack_score(bj) == 21

    hand_five = ['As', '2d', '3c', '4h', '5s', '6c']
    assert Hand.get_blackjack_score(hand_five) == 21

    bust_with_ace = ['Ah', '2s', 'Qh', 'Qd']
    assert Hand.get_blackjack_score(bust_with_ace) == 23

    bust_no_ace = ['7s', '8h', '9d']
    assert Hand.get_blackjack_score(bust_no_ace) == 24


def test_hand_populates():
    pass


def test_wager_required_to_receive_cards():
    pass

### ------------------------PLAYER TESTS-------------------------------------- ###


def test_player_populates_correct_values():
    pass
### ------------------------INTERACTIVE TESTS-------------------------------------- ###
### ------------------------CHIP TESTS-------------------------------------- ###