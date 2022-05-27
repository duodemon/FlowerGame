class CardSet(list):
    def __init__(self, initial_list=None):
        super().__init__()
        if initial_list is not None:
            self.add_cards(initial_list)

    def __str__(self):
        str_list = [str(x) for x in self]
        return ", ".join(str_list)

    def add_card(self, card):
        self.append(card)

    def add_cards(self, card_list):
        self.extend(card_list)

    def remove_top_card(self):
        return self.pop()

    def remove_card(self, index):
        return self.pop(index)

    def remove_cards(self, index_list):
        return [self.pop(x) for x in sorted(index_list, reverse=True)]

