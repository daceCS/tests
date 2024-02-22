import random


def read_random_word():
    with open("WordleHVAI/words.txt") as f:
        word_array = f.read().splitlines()
        return random.choice(word_array)


def is_valid_word(word):
    with open("WordleHVAI/words.txt") as f:
        word_array = f.read().splitlines()

        if word in word_array:
            return True
        else:
            return False


answer = read_random_word()
loops = 0
total = 0
alphabet = ['a',
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
weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


def assign_value(arr):
    for i in arr:
        for j in range(len(alphabet)):
            if i[0] == alphabet[j]:
                weights[j] = (weights[j] + i[1]) / total


def generate_string():
    global loops, weights, alphabet, total

    random_string = ""
    if loops < 40000:
        for i in range(5):
            letter = random.choices(alphabet, k=1)
            random_string += str(letter)[2]
            loops += 1
            total += 1
    else:
        for i in range(5):
            letter = random.choices(alphabet, weights=weights, k=1)
            random_string += str(letter)[2]
            loops += 1
            total += 1
    return random_string


def generate_text_output(guess):
    output_string = ""
    for attempt in range(1, 7):

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
                output_string.append([guess[i], 30])
            elif guess[i] in answer:
                output_string.append([guess[i], 3])
            else:
                output_string.append([guess[i], 2])
    return output_string[:5]


def generate_score(input_arr):
    arr = []
    score = 0
    for j in input_arr:
        arr.append(j[1])
    arr = arr[:5]
    for index in arr:
        score += index
    return score


def run_training():
    global answer, loops
    best = generate_string()

    runs = 40040
    i = 0

    while i < runs:

        rand_string = generate_string()

        # if is_valid_word(rand_string) is True:
        if i < 40000:
            output1 = generate_output(rand_string)
            score = generate_score(output1)
            assign_value(output1)
            if score > generate_score(generate_output(best)):
                best = rand_string
            i += 1
        elif i >= 40000:
            output1 = generate_output(rand_string)
            score = generate_score(output1)
            assign_value(output1)
            if is_valid_word(rand_string) is True:
                if score > generate_score(generate_output(best)):
                    best = rand_string
                i += 1

        if best == answer:
            break

    print(answer)
    print(best)
    print(i)
    answer = read_random_word()
    loops = 0
    return


for i in range(5):
    run_training()
    print(i)
    print(weights)


textfile = open("/Users/David/PycharmProjects/testing/policies.txt", 'w')
content = str(weights)
textfile.writelines(content)