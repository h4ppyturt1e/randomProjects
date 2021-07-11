
def passwords():
    words = ['about', 'after', 'again', 'below', 'could', 'every', 'first', 'found', 'great', 'house', 'large', 'learn',
             'never', 'other', 'place', 'plant', 'point', 'right', 'small', 'sound', 'spell', 'still', 'study', 'their',
             'there', 'these', 'thing', 'think', 'three', 'water', 'where', 'which', 'world', 'would', 'write', 'stop']

    first_letters = input("First letters: ").split()
    third_letters = input("Third letters: ").split()
    fifth_letters = input("Fifth letters: ").split()

    possible_words_first, possible_words_third, possible_words_fifth = [], [], []
    [[possible_words_first.append(word) for word in words if word[0] == letter] for letter in first_letters]
    print(possible_words_first)
    [[possible_words_third.append(word) for word in possible_words_first if word[2] == letter] for letter in third_letters]
    if len(possible_words_third) >= 2:
        [[possible_words_fifth.append(word) for word in possible_words_third if word[4] == letter] for letter in fifth_letters]
        print("Answer:\n{}".format(possible_words_fifth))
    else:
        print("Answer:\n{}".format(possible_words_third))


def complicated_wires():
    # led,red,blue,star -> instruction
    # 1001,b
    with open("complicated_wires_cheatsheet.csv") as f:
        data = f.readlines()
    print(data)
    prompt = input()


def main():
    complicated_wires()
    # while True:
    #     passwords()


if __name__ == "__main__":
    main()