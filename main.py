from Hand import Hand
from DBController import DBController
from Field import Field
from Deck import Deck

import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

def main():
    field = Field()
    hand = Hand()
    deck = Deck(DBController("info.json"))
    deck.populate()
    deck.shuffle()

    #Making windwow
    app = customtkinter.CTk()
    app.geometry("600x500")
    app.title("THE ULTIMATE TGC GAME THING")
    app.resizable(False, False)
    app.columnconfigure([0, 1, 2, 3, 4], minsize=100, pad=20, weight=1)

    #adding buttons/labels
    name_label = customtkinter.CTkLabel(master = app, text = "TGC CARD GAME", bg_color = "black", height = 50, text_color = 'white')
    name_label.grid(row = 0, column = 0, padx = 20, pady = 20, sticky = 'ew', columnspan = 5)
    deck_button = customtkinter.CTkButton(master = app, width = 100, height = 200, text = 'Deck', fg_color= 'white', text_color='black', command = lambda: update_from_deck())
    deck_button.grid(row = 1, column = 4)
    boss_label = customtkinter.CTkLabel(master = app, height = 100, text = 'BOSS HEALTH: ' + str(field.get_boss_health()))
    boss_label.grid(row = 1, column = 1, columnspan = 2)
    play_card_buttons = []
    for i in range(4):
        button = customtkinter.CTkButton(app, width = 100, height = 200, text = 'No Card', fg_color = 'white', text_color='black', command = lambda i = i: update_from_playing_a_card(i))
        button.grid(row = 2, column = i)
        play_card_buttons.append(button)

    #update buttons
    def update_from_deck():
        hand_length = len(hand.get_hand())
        if hand_length == 4:
            return 0
        else:
            drawed_card = deck.draw()
            if drawed_card != 0:
                hand.add_card(drawed_card)
                play_card_buttons[hand_length].configure(text = drawed_card.get_name())

    def update_from_playing_a_card(index: int):
        field.apply_card(hand.play_card(index))
        boss_label.configure(text = "BOSS HEALTH: " + str(field.get_boss_health()))
        playing_cards = hand.get_hand()
        hand.show_hand()
        for i in range(4):
            play_card_buttons[i].configure(text = hand.get_card_name_by_index(index = i))
        if field.get_boss_health() <= 0:
            boss_label.configure(text = "BOSS HAS BEEN DEFEATED")
            deck_button.configure(state = "disabled")
            for button in play_card_buttons:
                button.configure(state = "disabled")

    #Keep window open
    app.mainloop()

if __name__ == "__main__":
    main()