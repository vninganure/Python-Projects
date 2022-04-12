from typing import TextIO

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as name:
    names = name.readlines()

with open("./Input/Letters/starting_letter.txt", ) as letter_content:
    letter = letter_content.read()
    for namee in names:
        str_namee = namee.strip()
        letter_update = letter.replace(PLACEHOLDER, str_namee)
        print(letter_update)
        with open(f"./Output/ReadyToSend/Letter_for_{str_namee}.txt", mode="w") as sendfile:
            sendfile.write(letter_update)