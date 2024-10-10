from Card import Card
class Hand:
    def __init__(self, max_cards=4):
        """
        max_cards = maximum cards allowed in hand
        """
        self.cards_in_hand = []  # cards currently in hand
        self.max_cards = max_cards

    def add_card(self, card: Card):
        """
        card = Card object to be added to hand
        """
        if card == 0:
            print("Deck is empty")
        elif not isinstance(card, Card):
            raise ValueError
        else:
            if len(self.cards_in_hand) < self.max_cards:
                self.cards_in_hand.append(card)
                print(f"Drew card: {card.name}")
            else:
                print("Hand is full, cannot draw more cards.")

    def play_card(self, card_index):
        """
        card_index = index of card in deck
        field = where cards are played to
        """
        if 0 <= card_index < len(self.cards_in_hand):
            card = self.cards_in_hand.pop(card_index)
            print(f"Playing card: {card.name}")
            return card
        else:
            print("Invalid card index.")
            return 0

    def show_hand(self):
        # shows the cards in your hand as well as the damage they deal.
        if self.cards_in_hand:
            print("Cards in hand:")
            for i, card in enumerate(self.cards_in_hand):
                print(f"{i}: {card.name}")
        else:
            print("Hand is empty.")
    
    def get_hand(self):
        return self.cards_in_hand
    
    def get_card_name_by_index(self, index):
        if 0 <= index < len(self.cards_in_hand):
           return self.cards_in_hand[index].get_name()
        else:
            return "No Card"