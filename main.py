from Hand import Hand
from DBController import DBController
from Field import Field
from Deck import Deck

def main():
    field = Field()  # create a field for playing cards
    hand = Hand() # create a hand to hold drawn cards
    deck = Deck(DBController("info.json"))
    deck.populate()
    deck.shuffle()

    print("Welcome to the Trading Card Game!")

    while True:
        # show the user the options
        print("\nAvailable commands: draw, play <card_number>, show, quit")
        command = input("Enter your command: ").strip().lower()

        if command == "draw":
            hand.add_card(deck.draw())  # draws a card from the deck

        elif command.startswith("play"):
            # ensures the user uses the play command correctly, and provides the corrected method if needed
            try:
                _, card_number = command.split()  # split the entered command into parts based on spaces (play is ignored since it must be entered here)
                card_number = int(card_number)  # Convert card number to integer
                field.apply_card(hand.play_card(card_number))  # Play the specified card
            except (ValueError, IndexError):
                print("Invalid command. Use 'play <card_index> to play a card.")

        elif command == "show":
            hand.show_hand() # shows the cards in the current hand

        elif command == "quit":
            print("Thanks for playing.")
            break  # end the loop and the game
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()