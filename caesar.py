import string

def alphabet_position(letter):
    return string.ascii_lowercase.index(letter.lower())

def rotate_character(char, rot):
    if not char.isalpha():
        return char

    new_pos = (alphabet_position(char) + rot) % 26
    if char == char.upper():
        return string.ascii_uppercase[new_pos]
    else:
        return string.ascii_lowercase[new_pos]

def encrypt(text, rot):
    new_message = ""

    for char in text:
        new_message += rotate_character(char, rot)

    return new_message

