def is_valid_word(word):
    with open("WordleHVAI/words.txt") as f:
        word_array = f.read().splitlines()
        print(word_array)

        if word in word_array:
            return True
        else:
            return False


print(is_valid_word("kankr"))
