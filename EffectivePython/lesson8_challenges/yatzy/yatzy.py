from game_logic import YatzyGame
from interface import Interface

game = YatzyGame()
interface = Interface(game = game)

if __name__ == '__main__':
    interface.main_menu()