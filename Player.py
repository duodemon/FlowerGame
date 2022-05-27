from CardSet import CardSet


class Player:
    def __init__(self, id):
        self.hand = CardSet()
        self.id = id

    def play_cards(self):
        return self.hand

