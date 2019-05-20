"""
test-driven development + user story
"""


from Blackjack import (Cards,
                       Hand,
                       Player,
                       )


DECK = Cards()


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


test_hand = Hand()


def test_hand_score_lookup():
    """test a variety of hand combinations to make sure they are scored properly"""

    five_pts = ['2c', '3s']
    assert test_hand.get_score(five_pts) == 5

    twelve_pts = ['As', 'Ac', 'Kd']
    assert test_hand.get_score(twelve_pts) == 12

    thirteen_pts = ['Ad', '2s', 'Tc']
    assert test_hand.get_score(thirteen_pts) == 13

    fourteen_pts = ['Ah', 'Ad', 'Ac', 'As', 'Tc']
    assert test_hand.get_score(fourteen_pts) == 14

    nineteen_pts = ['Ac', '8d']
    assert test_hand.get_score(nineteen_pts) == 19

    bj = ['Js', 'Ac']
    assert test_hand.get_score(bj) == 21

    hand_five = ['As', '2d', '3c', '4h', '5s', '6c']
    assert test_hand.get_score(hand_five) == 21

    both_ace_values = ['Ac', '9h', 'As']
    assert test_hand.get_score(both_ace_values) == 21

    bust_with_ace = ['Ah', '2s', 'Qh', 'Jd']
    assert test_hand.get_score(bust_with_ace) == 23

    bust_no_ace = ['7s', '8h', '9d']
    assert test_hand.get_score(bust_no_ace) == 24


def test_hand_init_populates():
    assert len(test_hand.cards) == 2


def test_printable_hand_string():
    assert 'Blackjack.Hand object' not in str(test_hand)
    print(test_hand)


def test_len_hand():
    assert len(test_hand)


def test_hand_can_receive_cards_properly():
    """can add cards to hands, can still be scored"""
    assert len(test_hand) == 2
    test_hand.cards.append(DECK._deal_a_card())
    assert len(test_hand) == 3
    print(test_hand)


### ------------------------PLAYER TESTS-------------------------------------- ###
# class TestPlayer:
#     def test_player_has_an_attr:
#         x = "hello"
#         assert hasattr(x, "check")
#  TODO: move to test_classes?

test_player = Player('tester', 500)


def test_player_inits_parameters():
    assert test_player.name == 'Tester'
    assert test_player.chips == 500
    assert len(test_player.hand) == 2


def test_exception_raised_when_overbetting():
    """players can only bet up to their chip count"""
    pass


def test_player_populates_correct_values():
    pass


### -------------------------CHIP TESTS-------------------------------------- ###


### ------------------------INTERACTIVE TESTS-------------------------------------- ###

def test_hand_standing_returns_correct_score():
    pass


def test_wager_required_to_receive_cards():
    pass
