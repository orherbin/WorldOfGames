from random import randint


# Generates number between 1 to difficulty and save it to secret_number.
def generate_number(difficulty):
    secret_number = randint(1, difficulty)
    return secret_number


# Prompts the user for a number between 1 to difficulty and returns the number.
def get_guess_from_user(difficulty):
    print(f"Please choose a number between 1 to {difficulty}.")
    user_guess = input()
    return user_guess


# Compares the secret generated number to the one prompted by the get_guess_from_user.
def compare_results():
    if get_guess_from_user() == generate_number():
        return True


# Calls the functions above and play the game. Will return True / False if the user lost or won.
def play(chosen_difficulty):
    generate_number(chosen_difficulty)
    get_guess_from_user(chosen_difficulty)
    compare_results()
    return compare_results()
