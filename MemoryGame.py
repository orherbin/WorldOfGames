from os import system
import time
import random


# Generates a list of random numbers between 1 and 101. The list length will be difficulty.
def generate_sequence(difficulty):
    res = [random.randrange(1, 101, 1) for i in range(difficulty)]
    print(res)
    time.sleep(0.7)
    system('clear')


# Returns a list of numbers prompted from the user. The list length will be in the size of difficulty.
def get_list_from_user():
    user_list = input("Please enter the list of numbers presented earlier.")
    return user_list


# Compares two lists if they are equal. The function will return True / False.
def is_list_equal():
    if generate_sequence() == get_list_from_user():
        return True


# Calls the functions above and play the game. Will return True / False if the user lost or won.
def play(chosen_difficulty):
    generate_sequence(chosen_difficulty)
    get_list_from_user()
    is_list_equal()
    return is_list_equal()
