from Card import *
import random as rand

from CardSet import CardSet


class Deck(CardSet):
    def __init__(self):
        super().__init__()
        for i in range(2):
            self.append(Card(3, Color.MIXED, Name.OPERETTA))
            self.append(Card(6, Color.MIXED, Name.OPERA))
            self.append(Card(8, Color.BLACK, Name.LITTLE_BULL))
            self.append(Card(9, Color.BLACK, Name.BIG_BULL))
        for i in range(4):
            self.append(Card(2, Color.RED, Name.RED_EYE))
            self.append(Card(4, Color.BLACK, Name.BLACK_EYE))
            self.append(Card(6, Color.BLACK, Name.OBLIQUE))
            self.append(Card(6, Color.MIXED, Name.SIX))
            self.append(Card(7, Color.MIXED, Name.SEVEN))
            self.append(Card(8, Color.RED, Name.RED_EIGHT))
            self.append(Card(10, Color.MIXED, Name.FLOWERED_TEN))
            self.append(Card(10, Color.BLACK, Name.BLACK_TEN))
            self.append(Card(11, Color.BLACK, Name.TIGER))
            self.append(Card(12, Color.MIXED, Name.GOD))

    def shuffle(self):
        size = len(self)
        shuffled_deck = []
        for i in range(size):
            index = rand.randint(0, size - i - 1)
            shuffled_deck.append(self.pop(index))
        self.clear()
        self.extend(shuffled_deck)

    def cut(self):
        size = len(self)
        index = rand.randint(0, size - 1)
        sub_deck_1 = self[0:index]
        sub_deck_2 = self[index:size]
        self.clear()
        self.extend(sub_deck_1)
        self.extend(sub_deck_2)

    def draw(self):
        return self.remove_top_card()
