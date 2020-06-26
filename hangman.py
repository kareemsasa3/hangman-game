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
    return 0
    
def update_path(file_name):
    return 0