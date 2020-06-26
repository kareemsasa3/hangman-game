from pathlib import Path
import random

data_folder = Path("categories/")

def initialize():
    play_game = input("\nWould you like to play Hangman? (Y or N)\n")

    if play_game in ('Y', 'y'):
        start_game()
    elif play_game in ('N', 'n'):
        exit_game = input("\nWould you like to exit? (Y or N)\n")

        if exit_game in ('Y', 'y'):
            print("\nGoodbye\n")
            exit
        elif exit_game in ('N', 'n'):
            initialize()
        else:
            print("\nUnknown user input\n")
            initialize()
    else:
        print("\nUnknown user input\n")
        initialize()
    return 0

def start_game():
    print("\nWelcome!\n")
    choose_category()
    return 0

def choose_category():
    print("Choose a category: \n")
    print("C - Countries")
    print("M - Movies")
    print("P - Pokemon")
    print("S - Sports")
    print("T - Technology")

    choose_category = input("\n= ").upper()

    if choose_category == 'C':
        play("countries.txt")
    elif choose_category == 'M':
        play("movies.txt")
    elif choose_category == 'P':
        play("pokemon.txt")
    elif choose_category == 'S':
        play("sports.txt")
    elif choose_category == 'T':
        play("technology.txt")
    else:
        print("\nUnknown user input\n")
    return 0

def play(file_name):
    file_to_open = update_path(file_name)
    f = open(file_to_open, 'r')

    possible_words = f.readlines()
    word_to_guess = random.choice(possible_words)
    word_guessed = ""

    for i in range(len(word_to_guess)):
        if word_to_guess[i] == ' ':
            word_guessed += '  '
        else:
            word_guessed += '_ '

    print(word_guessed)
    user_guess = input("Guess a letter: ")

    if user_guess in word_to_guess:
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == user_guess:
                word_guessed += user_guess
            else:
                word_guessed += '_ '
    return 0
    
def update_path(file_name):
    file_to_open = data_folder / file_name
    return file_to_open