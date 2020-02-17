print('test')
import random

control_string = "methinks it is like a weasel"
character_string = ""
possible_character_choices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                              'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                              'w', 'x', 'y', 'z', ' ']

def generate_character_string(amount_of_characters):
    # A function that generates a 27 character string from the alphabet and ' '
    for character in range(amount_of_characters+1):
        character = random.choice(possible_character_choices)
        character_string += character
    print(character_string)

generate_character_string(27)

