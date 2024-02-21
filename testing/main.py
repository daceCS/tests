import random
import numpy
import sys

answer = "words"
outputs = []


def generate_string():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    random_string = ""
    for i in range(5):
        random_string += random.choice(alphabet)

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
    return output_string[:10]


def generate_score(input_arr):
    arr = []
    score = 0
    for j in input_arr:
        arr.append(j[1])
    arr = arr[:5]
    for i in arr:
        score += i
    return score


high = rand_string = generate_string()

for i in range(10000000):
    print(i)
    rand_string = generate_string()
    output1 = generate_output(rand_string)
    score = generate_score(output1)
    if score > generate_score(generate_output(high)):
        high = rand_string
    if rand_string == answer:
        break



print(high)
print(generate_score(generate_output(high)))

print(answer)
