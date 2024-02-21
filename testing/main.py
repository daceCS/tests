import random
import numpy
import sys
import operator

def read_random_word():
    with open("words.txt") as f:
        word_array = f.read().splitlines()
        return random.choice(word_array)

answer = read_random_word()
outputs = []
loops = 0
dictionary = []
alphabet = [['a', 0],
            ['b', 0],
            ['c', 0],
            ['d', 0],
            ['e', 0],
            ['f', 0],
            ['g', 0],
            ['h', 0],
            ['i', 0],
            ['j', 0],
            ['k', 0],
            ['l', 0],
            ['m', 0],
            ['n', 0],
            ['o', 0],
            ['p', 0],
            ['q', 0],
            ['r', 0],
            ['s', 0],
            ['t', 0],
            ['u', 0],
            ['v', 0],
            ['w', 0],
            ['x', 0],
            ['y', 0],
            ['z', 0]]


def assign_value(arr):
    for i in arr:
        for j in alphabet:
            if i[0] == j[0]:
               j[1] = (j[1] + i[1])/loops


def generate_string():
    global loops
    random_string = ""
    if loops < 1000:
        for i in range(5):
            letter = alphabet[random.randint(0, 25)][0]
            random_string += letter
            loops += 1

    else:
        for i in range(5):
            letter = alphabet[random.randint(0, 4)][0]
            random_string += letter
            loops += 1



    return random_string


def generate_text_output(guess):
    output_string = ""
    for attempt in range(1, 7):

        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

        for i in range(min(len(guess), 5)):
            if guess[i] == answer[i]:
                output_string += "!"
            elif guess[i] in answer:
                output_string += "o"
            else:
                output_string += "x"
    return output_string[:5]


def generate_output(guess):
    output_string = []
    for attempt in range(1, 7):

        for i in range(min(len(guess), 5)):
            if guess[i] == answer[i]:
                output_string.append([guess[i], 1])
            elif guess[i] in answer:
                output_string.append([guess[i], 0])
            else:
                output_string.append([guess[i], -1])
    return output_string[:5]


def generate_score(input_arr):
    arr = []
    score = 0
    for j in input_arr:
        arr.append(j[1])
    arr = arr[:5]
    for i in arr:
        score += i
    return score



for i in range(10000):
    rand_string = generate_string()
    output1 = generate_output(rand_string)
    score = generate_score(output1)
    assign_value(output1)
    alphabet = sorted(alphabet, key=lambda x: x[1], reverse=True)
    if rand_string == answer:

        break


print(answer)
print(alphabet)


