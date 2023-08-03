from tableWinners import  TableWinners
from tableVictories import TableVictories
from myHMAC import MyHMAC
import random
import sys

class Controller:
    def __init__(self, args):
        if len(args) % 2 == 0 or len(args) < 3 or len(args) != len(set(args)):
            print('You must provide at least three unique arguments, and the number of arguments must be odd. Here are examples: "Apple Orange Pear Banana Kiwi", "Red Blue Green Yellow Purple Orange Pink".')
            sys.exit()
        self.TOV = TableVictories(args)
        self.TOW = TableWinners()
        self.PCHMAC = MyHMAC()
        self.ComputerMoveValue = ""
        self.UserMoveValue = ""

    def Play(self):
        while(True):
            self.ComputerMove()
            for index, key in enumerate(self.TOV.Combinations, start=1):
                print(f"{index} - {key}")
            print("0 - Exit")
            print("? - Help")
            print("# - Check HMAC")
            print("Enter your move: ")
            value = input()
            if value.isdigit() and int(value) == 0:
                return
            elif value == '?':
                self.TOV.PrintCombinations()
            elif value == '#':
                self.PCHMAC.CheckHMAC()
            else:
                for index, key in enumerate(self.TOV.Combinations, start=1):
                    if int(value) == index:
                        self.UserMoveValue = key
                        self.CheckResult()

    def ComputerMove(self):
        value = random.randint(1, len(self.TOV.Combinations))
        for index, key in enumerate(self.TOV.Combinations, start=1):
            if value == index:
                self.PCHMAC.CreationOfHMAC(key)
                self.ComputerMoveValue = key

    def CheckResult(self):
        self.TOW.GameResult(self.ComputerMoveValue, self.UserMoveValue, self.TOV)
        print(f"The secret key: {self.PCHMAC.secret_key.hex()}")
        print()