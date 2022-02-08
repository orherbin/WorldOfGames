# Importing Modules of the games and util files.
import CurrencyRouletteGame
import GuessGame
import MemoryGame
import Score


# Welcome message.
def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."


# Main game function. Prompting the user to choose requested game and difficulty.
def load_game():
    print("""Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n
    2. Guess Game - guess a number and see if you chose like the computer.\n
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS.""")

    # Choosing game.
    chosen_game = input()
    while not chosen_game.isnumeric():
        print("Please enter a valid numerical value.")
        chosen_game = input()
    while int(chosen_game) < 1 or int(chosen_game) > 3 and chosen_game.isnumeric():
        print("Please enter a number between 1 to 3.")
        chosen_game = input()

    # Choosing difficulty.
    print("Please choose game difficulty from 1 to 5:")
    difficulty = input()
    while not difficulty.isnumeric():
        print("Please enter a valid numerical value.")
        difficulty = input()
    while int(difficulty) < 1 or int(difficulty) > 5 and difficulty.isnumeric():
        print("Please enter a number between 1 to 5.")
        difficulty = input()

        # Running the specific game with the selected difficulty according to the user's choice.
        # Also updating the user's score if he won.
        if chosen_game == 1:
            GuessGame.play(difficulty)
            if GuessGame.compare_results():
                Score.add_score(difficulty)
        elif chosen_game == 2:
            MemoryGame.play(difficulty)
            if MemoryGame.is_list_equal():
                Score.add_score(difficulty)
        else:
            CurrencyRouletteGame.play(difficulty)
        if CurrencyRouletteGame.get_money_interval():
            Score.add_score(difficulty)
