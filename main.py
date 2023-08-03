from сontroller import Controller
import sys
if __name__ == '__main__':
    Game = Controller(sys.argv[1:])
    Game.Play()