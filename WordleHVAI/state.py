import numpy as np

from configs import Configs


class State():
    def __init__(self, p1):
        self.configs = Configs()
        self.POLICIES_DIR = self.configs.POLICIES_DIR

        self.p1 = p1

        self.boardHash = None
        self.isEnd = False
        self.playerSymbol = 1

    def getHash(self, guess):
        output_string = ""
        for attempt in range(1, 7):

            for i in range(min(len(guess), 5)):
                if guess[i] == self.p1.answer[i]:
                    output_string += "!"
                elif guess[i] in self.p1.answer:
                    output_string += "o"
                else:
                    output_string += "x"
        return output_string[:5]

    def winner(self, guess):
        if guess == self.p1.answer:
            self.isEnd = True
            return 1
        self.isEnd = False
        return None

    def updateStates(self, input_arr):
        arr = []
        score = 0
        for j in input_arr:
            arr.append(j[1])
        arr = arr[:5]
        for index in arr:
            score += index
        return score

    def generate_output(self, guess):
        output_string = []
        for attempt in range(1, 7):

            for i in range(min(len(guess), 5)):
                print(self.p1.answer)
                print(i)
                if guess[i] == self.p1.answer[i]:
                    output_string.append([guess[i], 50])
                elif guess[i] in self.p1.answer:
                    output_string.append([guess[i], 3])
                else:
                    output_string.append([guess[i], 2])
        return output_string[:5]

    def reset(self):

        self.boardHash = None
        self.isEnd = False
        self.playerSymbol = 1

    def assign_value(self, arr):
        for i in arr:
            for j in range(len(self.p1.alphabet)):
                if i[0] == self.p1.alphabet[j]:
                    self.p1.states[j] = (self.p1.states[j] + i[1]) / self.p1.total

    # play with human
    def playGame(self):
        while not self.isEnd:
            # Player 1

            # specific to bot-------------------------------
            p1_action = self.p1.chooseAction()
            # take action and upate board state
            print(p1_action)
            output1 = self.generate_output(p1_action)
            self.assign_value(output1)
            self.p1.total += 1



            win = self.winner(p1_action)
            if win is not None:
                if win == 1:
                    print(self.p1.name, "wins!")

                break
