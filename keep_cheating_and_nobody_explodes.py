
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
    wire_dict = {'1001': 'b', '1100': 'b', '1101': 'b', '0000': 'c', '0001': 'c',
                 '0101': 'c', '0011': 'd', '1000': 'd', '1111': 'd', '0111': 'p',
                 '1010': 'p', '1011': 'p', '0010': 's', '0100': 's', '0110': 's',
                 '1110': 's'}

    prompt = input("Enter configuration here\n")
    config_list = ['0', '0', '0', '0']

    if "led" in prompt:
        config_list[0] = '1'
    if "red" in prompt:
        config_list[1] = '1'
    if "blue" in prompt:
        config_list[2] = '1'
    if "star" in prompt:
        config_list[3] = '1'
    config = "".join(config_list)

    result = wire_dict[config]
    print(result)
    return result


def main():
    vowels = ['a', 'e', 'i', 'o', 'u']

    serial_num = input("Serial number? ").split()
    has_vowels = any([letter.lower() in vowels for letter in serial_num])
    is_odd = bool(int(serial_num[-1]) % 2)
    num_batteries = int(input("Number of batteries? "))
    parallel_port = True if input("Has parallel port? ").lower() in ["yes", "y"] else False
    print()



    complicated_wires()
    # while True:
    #     passwords()


if __name__ == "__main__":
    main()


