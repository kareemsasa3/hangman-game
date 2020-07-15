from pathlib import Path
import random
import os
from os import system


data_folder = "./categories/"


def initialize_program():
    system('clear')
    print("----------WELCOME----------")
    play_game = input("PLAY HANGMAN? (Y or N): ").upper()

    if play_game == 'Y':
        choose_category()
    elif play_game == 'N':
        exit_game = input("\nEXIT? (Y or N): ")

        if exit_game == 'Y':
            print("\n----------GOODBYE----------")
            exit
        else:
            initialize_program()
    else:
        initialize_program()
    return 0


def choose_category():
    system('clear')
    print("-----CHOOSE A CATEGORY:-----")
    print("C - COUNTRIES")
    print("M - MOVIES")
    print("P - POKEMON")
    print("S - SPORTS")
    print("T - TECHNOLOGY")
    print("----------------------------")
    category = input("= ").upper()

    if category == 'C':
        setup_game("countries.TXT")
    elif category == 'M':
        setup_game("movies.TXT")
    elif category == 'P':
        setup_game("pokemon.TXT")
    elif category == 'S':
        setup_game("sports.TXT")
    elif category == 'T':
        setup_game("technology.TXT")
    else:
        print("\nBAD USER INPUT")
        choose_category()        
    return 0


def setup_game(file_name):
    system('clear')
    print("CATEGORY: " + os.path.splitext(file_name)[0].upper())
    file_to_open = update_path(file_name)
    f = open(file_to_open, 'r')
    possible_words = f.readlines()
    word_to_guess = random.choice(possible_words)
    word_guessed = setup_blank_string(word_to_guess)
    execute_guess(word_to_guess, word_guessed)
    return 0


def setup_blank_string(word_to_guess):
    print("\nWORD TO GUESS: " + word_to_guess)
    word_guessed = ""
    
    for i in range(len(word_to_guess)-1):
        if word_to_guess[i] == ' ':
            word_guessed += '  '
        else:
            word_guessed += '_ '
    
    print("\n" + word_guessed)
    return word_guessed


def execute_guess(word_to_guess, word_guessed):
    guesses_remaining = 5
    location_of_guess = []
    print("\n# OF INCORRECT GUESSES REMAINING: " + str(guesses_remaining))
    user_guess = input("\nGUESS A LETTER: ")[0].lower()

    if user_guess in word_to_guess:
        print("\nLETTER '" + user_guess.upper() + "' FOUND\n")        
        for i in range(len(word_to_guess)-1):
            if word_to_guess[i] == user_guess:
                location_of_guess.append(str(word_to_guess.index(user_guess)))
                word_guessed = update_string(user_guess, word_guessed, location_of_guess)

    else:
        print("\nLETTER '" + user_guess.upper() + "' NOT FOUND\n")
        guesses_remaining = guesses_remaining - 1

    #execute_guess()

        
def update_string(user_guess, word_guessed, location_of_guess):
    print("LOCATION OF GUESSES: " + str(location_of_guess))
    for i in range(len(location_of_guess)-1):
        if location_of_guess[i] == i:
            word_guessed = word_guessed[:i] + user_guess + s[i+1:]
    print(word_guessed)


def update_path(file_name):
    return data_folder + file_name


initialize_program()
