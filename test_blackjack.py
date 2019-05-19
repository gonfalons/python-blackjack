"""
test-driven development + user story
"""
from blackjack import DECK


### ------------------------DECK TESTS-------------------------------------- ###

def test_full_deck():
    """full 52-card deck"""
    assert len(DECK) == 52


def test_deal_random_cards():
    """check several lists of cards dealt"""
    one_card = [DECK.deal_a_card()]
    two_cards = [DECK.deal_a_card(), DECK.deal_a_card()]
    five_cards = [
        DECK.deal_a_card(), DECK.deal_a_card(), DECK.deal_a_card(
        ), DECK.deal_a_card(), DECK.deal_a_card(),
    ]
    assert len(one_card) == 1
    assert len(two_cards) == 2
    assert len(five_cards) == 5
    print(f'-{one_card}-\n-{two_cards}-\n-{five_cards}-')


def test_fair_dealing():
    """make sure all cards dealt are removed from deck, no repeats"""
    hitme = DECK.deal_a_card
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


### ------------------------PLAYER TESTS-------------------------------------- ###
def test_player_populates_correct_values():
    pass
### ------------------------INTERACTIVE TESTS-------------------------------------- ###
### ------------------------HAND TESTS-------------------------------------- ###
### ------------------------CHIP TESTS-------------------------------------- ###
