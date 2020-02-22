import random

class PlayingCard:
    """A class that represents a simple playing card"""

    def __init__(self):
        """Initizalize the attributes of the playing card"""
        self.ranks = ['two', 'three', 'four', 'five', 'six', 'seven',
                      'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace'] 
        self.suits = ['hearts', 'diamonds', 'spades', 'clubs']
        self.color = ['black', 'red']

    def possible_ranks(self):
        """Function that prints what different ranks a card can have"""
        print("\nA playing card can have one the following 13 ranks:")
        for rank in self.ranks:
            print(f"\t- {rank}")

    def possible_suits(self):
        """Function that prints the possible suits a card can have"""
        print("\nA playing card can have one the following 4 suits:")
        for suit in self.suits:
            print(f"\t- {suit}")

    #def possible_colors(self, suit):

    def generate_playing_card(self):
        """A function that generates a playing card with the initialized attributes"""
        generated_rank = random.choice(self.ranks)
        generated_suit = random.choice(self.suits)
        generated_card = f"{generated_rank} of {generated_suit}"

        return generated_card

p1 = PlayingCard()