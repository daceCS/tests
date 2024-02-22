import numpy as np
import pickle
import os
import random
from configs import Configs

class BotPlayer():
    def __init__(self, name):
        self.configs = Configs()

        self.name = name
        self.alphabet = ['a',
                    'b',
                    'c',
                    'd',
                    'e',
                    'f',
                    'g',
                    'h',
                    'i',
                    'j',
                    'k',
                    'l',
                    'm',
                    'n',
                    'o',
                    'p',
                    'q',
                    'r',
                    's',
                    't',
                    'u',
                    'v',
                    'w',
                    'x',
                    'y',
                    'z', ]
        self.lr = self.configs.lr
        self.decay_gamma = self.configs.decay_gamma
        self.exp_rate = self.configs.exp_rate
        self.loops = 0
        self.total = 1
        self.attempts = 0
        self.best = ""
        self.answer = self.configs.answer

        self.states = []


    def getHash(self, guess):
        output_string = []
        for attempt in range(1, 7):

            for i in range(min(len(guess), 5)):
                if guess[i] == self.configs.answer[i]:
                    output_string.append([guess[i], 30])
                elif guess[i] in self.configs.answer:
                    output_string.append([guess[i], 3])
                else:
                    output_string.append([guess[i], 2])
        return output_string[:5]

    def is_valid_word(self, word):
        with open("words.txt") as f:
            word_array = f.read().splitlines()

            if word in word_array:
                return True
            else:
                return False

#specific to bot----------------------
    def chooseAction(self):

        while self.attempts < 6:
            random_string = ""
            for i in range(5):
                letter = random.choices(self.alphabet, weights=self.states, k=1)
                random_string += str(letter)[2]
                self.loops += 1
                self.total += 1

            if self.is_valid_word(random_string) is True:
                self.attempts += 1
                return random_string

#-----------------------

    def addStates(self, board_hash):
        self.states.append(board_hash)
#specific to bot-------------------------------
    def loadPolicy(self):
        file = open(os.path.join(self.configs.POLICIES_DIR, "policies.txt"), 'r')
        print(str(file.readlines()))
        self.states = [1.2241055766628708e-06, 8.160753792662567e-07, 8.160703844398758e-07, 8.160737143071452e-07, 1.2241105714698894e-06, 1.2241155663054405e-06, 8.160770442056652e-07, 8.160787091722495e-07, 8.160753792526686e-07, 8.160886990512399e-07, 8.160770442049858e-07, 1.2241205611868491e-06, 8.16072049371812e-07, 8.160936940875482e-07, 8.160703844391965e-07, 8.160703844405551e-07, 8.160986891850031e-07, 8.160703844398758e-07, 1.2241155663034025e-06, 8.160720493745296e-07, 8.161070144935047e-07, 8.160803741245661e-07, 8.160953591105214e-07, 8.160870340547631e-07, 8.160720493697741e-07, 8.161020192853031e-07]
        print(self.states)

