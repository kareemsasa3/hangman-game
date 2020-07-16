from pathlib import Path
import random
import os
from os import system

data_folder = "./categories/"
guesses_remaining = 5

def initialize_program():
    system('clear')
    print("----------WELCOME----------")
    play_game = input("PLAY HANGMAN? (Y or N): ").upper()

    if play_game == 'Y':
        choose_category()
    elif play_game == 'N':
        exit_game = input("\nEXIT? (Y or N): ").upper()

        if exit_game == 'Y':
            print("----------GOODBYE----------")
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
    global data_folder
    system('clear')
    file_to_open = data_folder + file_name
    f = open(file_to_open, 'r')
    possible_words = f.readlines()
    word_to_guess = random.choice(possible_words)
    word_guessed = setup_blank_string(word_to_guess)
    execute_guess(word_to_guess, word_guessed, file_name)
    return 0

def setup_blank_string(word_to_guess):
    word_guessed = ""
    
    for i in range(len(word_to_guess)-1):
        if word_to_guess[i] == ' ':
            word_guessed += '  '
        else:
            word_guessed += '_ '
    return word_guessed

def execute_guess(word_to_guess, word_guessed, file_name):
    global guesses_remaining
    characters_remaining = []

    for i in word_guessed:
        if i == "_":
            characters_remaining.append(i)
            
    if characters_remaining == []:
        determine_win(word_to_guess, word_guessed)        
        
    print("CATEGORY: " + os.path.splitext(file_name)[0].upper())
    print("\n" + word_guessed)
    print("\n# OF INCORRECT GUESSES REMAINING: " + str(guesses_remaining))
    user_guess = input("\nGUESS A LETTER: ")[0].lower()

    if user_guess in word_to_guess:
        print("\nLETTER '" + user_guess.upper() + "' FOUND\n")        
        word_guessed = update_string(user_guess, word_to_guess, word_guessed)
    else:
        guesses_remaining = guesses_remaining - 1
    determine_loss()
        
    system('clear')
    execute_guess(word_to_guess, word_guessed, file_name)
    
def update_string(user_guess, word_to_guess, word_guessed):
    location_of_guess = []
    
    for i in range(len(word_to_guess)):
        if word_to_guess[i] == user_guess:
            location_of_guess.append(i)

    for i in range(len(location_of_guess)):
        location_of_guess[i] = location_of_guess[i] * 2
            
    for i in range(len(word_guessed)):
        for t in location_of_guess:
            if i == t:
                word_guessed = word_guessed[:i] + user_guess.upper() + word_guessed[i+1:]

    print("\n" + word_guessed)
    return word_guessed

def determine_win(word_to_guess, word_guessed):
    word_guessed = word_guessed.replace(" ", "").lower().rstrip()
    word_to_guess = word_to_guess.replace(" ", "").lower().rstrip()
        
    if word_to_guess == word_guessed:
        print("----------------------------")
        print("CONGRATULATIONS! YOU WON")
        print("----------------------------")
        play_again()

def determine_loss():
    global guesses_remaining
    
    if guesses_remaining == 0:
        system('clear')
        print("----------------------------")
        print("OUT OF GUESSES -- YOU LOSE")
        print("----------------------------")
        play_again()

def play_again():
    global guesses_remaining
    again = input("\nPLAY AGAIN? (Y or N): ").upper()
    
    if again == 'Y':
        guesses_remaining = 5
        choose_category()
    else:
        print("THANKS FOR PLAYING -- GOODBYE")
        exit()

# add functionality for checking if character has been used before
#                     - checks if character is alphabetic
#                     - checks if user input is single character

initialize_program()
