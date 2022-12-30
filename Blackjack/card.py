'''card.py'''

class Card:
    '''Card'''

    SUIT_SYMBOLS = {
        0: "\u2666",  # diamonds
        1: "\u2665",  # hearts
        2: "\u2663",  # clubs
        3: "\u2660"  # spades
    }

    VALUE_NAMES = {
        1: "A",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "T",
        11: "J",
        12: "Q",
        13: "K"
    }

    def __init__(self):
        pass

    def __str__(self):
        pass