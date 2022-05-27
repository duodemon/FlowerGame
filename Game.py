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
    game.new_round()
    for player in game.players:
        print("Player " + str(player.id) + ": " + str(player.hand))
        input_string = input("Play card(s): ")
        index_list = [int(x) for x in input_string.split(",")]
        if len(index_list) == 1:
            removed_card = player.hand.remove_card(index_list[0])
            print("Player " + str(player.id) + " played " + str(removed_card))

        elif len(index_list) > 1:
            removed_cards = CardSet(player.hand.remove_cards(index_list))
            print("Player " + str(player.id) + " played " + str(removed_cards))

        print("Player " + str(player.id) + " remaining cards: " + str(player.hand))


if __name__ == "__main__":
    main()