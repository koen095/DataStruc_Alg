from playing_card import PlayingCard

class DeckOfCards:
    """A class that represents a deck of playing cards"""

    def __init__(self):
        """Initialize the attributes of the deck of cards"""
        self.cards_in_deck = 52

    def draw_card(self):
        """Function that draws a card from the deck"""
        drawn_card = PlayingCard().generate_playing_card()
        print(f"Drawn: {drawn_card}")

    #def funcname(self, parameter_list):
     #   """Function that keeps track of the drawn cards"""

   # def funcname(self):
    #    """Function that ..."""   

new_deck = DeckOfCards()
new_deck.draw_card()