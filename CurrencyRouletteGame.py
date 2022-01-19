from currency_converter import CurrencyConverter
from random import randint


# Gets the current currency rate from USD to ILS and generates an interval.
def get_money_interval(difficulty):
    num = randint(1, 100)
    print(f"The selected number is {num}")
    c = CurrencyConverter()
    converted_num = c.convert(num, 'USD', 'ILS')
    min_range = converted_num - (5 - difficulty)
    max_range = converted_num + (5 - difficulty)
    get_guess_from_user()
    if max_range >= get_guess_from_user() >= min_range:
        return True


# Prompts a guess from the user to enter a guess of value to a given amount of USD.
def get_guess_from_user():
    player_guess = input("Please enter your guess:")
    return player_guess


def play(difficulty):
    return get_money_interval(difficulty)
