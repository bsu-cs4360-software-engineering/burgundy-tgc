class Hand:
    def __init__(self, deck, max_cards=13):
        """
        deck = deck class instance
        max_cards = maximum cards allowed in hand
        """
        self.deck = deck
        self.cards_in_hand = []  # cards currently in hand
        self.max_cards = max_cards

    def draw_card(self):
        # draws card from the deck and adds it to the hand
        if len(self.cards_in_hand) < self.max_cards:
            card = self.deck.draw()  # Assuming the Deck class has a draw() method
            if card:
                self.cards_in_hand.append(card)
                print(f"Drew card: {card.name} (Damage: {card.damage})")
            else:
                print("The deck is empty.")
        else:
            print("Hand is full, cannot draw more cards.")

    def play_card(self, card_index, field):
        """
        card_index = index of card in deck
        field = where cards are played to
        """
        if 0 <= card_index < len(self.cards_in_hand):
            card = self.cards_in_hand.pop(card_index)
            print(f"Playing card: {card.name} (Damage: {card.damage})")
            field.apply_card(card)
        else:
            print("Invalid card index.")

    def show_hand(self):
        # shows the cards in your hand as well as the damage they deal.
        if self.cards_in_hand:
            print("Cards in hand:")
            for i, card in enumerate(self.cards_in_hand):
                print(f"{i}: {card.name} (Damage: {card.damage})")
        else:
            print("Hand is empty.")

