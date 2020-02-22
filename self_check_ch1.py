import random, datetime, string

control_string = "methinks it is like a weasel"

possible_character_choices = list(string.ascii_lowercase + ' ')

def generate_character_string():
    # A function that generates a character string from the alphabet and ' '
    character_string = ""
    for character in range(len(control_string)):
        character = random.choice(possible_character_choices)
        character_string += character 
    return character_string

def call_generate_character_string():
    # Keeps calling generate_character_string untill it matches control_string
    
    start_time = datetime.datetime.now().replace(microsecond=0)
    counter = 0
    shakespeare_attempt = generate_character_string()
    while shakespeare_attempt != control_string:
        shakespeare_attempt = generate_character_string()
        counter += 1

    end_time = datetime.datetime.now().replace(microsecond=0)
    duration = end_time - start_time

    print(f"\nIt took {counter} calls to function and {duration} to match the control string")
    print(f"The control string: {control_string}")
    print(f"The generated string: {shakespeare_attempt}")

call_generate_character_string()
