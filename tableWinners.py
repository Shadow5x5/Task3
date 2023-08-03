class TableWinners:
    def __init__(self):
        self.computerChoice = ""
        self.userChoice = ""
        self.gameHistory = []

    def GameResult(self, cC, uC, TOV):
        if cC == uC:
            self.gameHistory.append({"Computer choice": cC, "User choice": uC,"User result": "Draw","Computer result": "Draw"})
        elif uC in TOV.Combinations[cC]:
            self.gameHistory.append({"Computer choice": cC,"User choice": uC,"User result": "Lose","Computer result": "Win"})
        else:
            self.gameHistory.append({"Computer choice": cC,"User choice": uC,"User result": "Win","Computer result": "Lose"})
        self.PrintHistory()

    def PrintHistory(self):
        for key in self.gameHistory[-1]:
            print(f"{key}: {self.gameHistory[-1][key]}")