from tabulate import tabulate

class TableVictories:

    def __init__(self, arguments):
        self.Combinations = {}
        n = len(arguments)
        count = int((n - 1) / 2)
        elements_to_append = arguments[:count]
        arguments.extend(elements_to_append)
        for i in range(len(arguments) - count):
                element = arguments[i]
                elements_after_subtraction = arguments[i + 1:i + 1 + count]
                self.Combinations[element] = elements_after_subtraction

    def PrintCombinations(self):
        table_title = "Combination table to win the game"
        headers = list(self.Combinations.keys())
        row_names = list(self.Combinations.keys())
        data = []
        for key in self.Combinations:
            tempArr = []
            for header in headers:
                if header in self.Combinations[key]:
                    tempArr.append("Win")
                elif header == key:
                    tempArr.append("Draw")
                else:
                    tempArr.append("Lose")
            data.append(tempArr)
        table = tabulate(data, headers=headers, tablefmt="grid", showindex=row_names, stralign="center")
        table_with_title = f"{table_title}\n{table}"
        print(table_with_title)
        print()