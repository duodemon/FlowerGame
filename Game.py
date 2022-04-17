from Deck import *
from Player import *
from constants import *


class Game:
    def __init__(self):
        self.players = [Player(1), Player(2), Player(3)]
        self.current_player_index = 0

    def new_round(self):
        self.deck = Deck()
        for i in range(rand.randint(0, 9)):
            self.deck.shuffle()
        self.deck.cut()
        self.deal_cards()

    def deal_cards(self):
        while len(self.deck) > 0:
            self.players[self.current_player_index].hand.append(self.deck.draw())
            self.next_player()

    def next_player(self):
        self.current_player_index = (self.current_player_index + 1) % NUMBER_OF_PLAYERS


def main():
    game = Game()
    while 1:
        game.new_round()
        while 1:
