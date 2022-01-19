import CurrencyRouletteGame
import MemoryGame
import GuessGame
from Live import load_game, welcome

print(welcome("Guy"))
load_game()


def update(game, difficulty):
    if game == 1:
        GuessGame.play(difficulty)
    elif game == 2:
        MemoryGame.play(difficulty)
    else:
        CurrencyRouletteGame.play(difficulty)
