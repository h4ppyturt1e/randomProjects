def passwords():
    words = ['about', 'after', 'again', 'below', 'could', 'every', 'first', 'found', 'great', 'house', 'large', 'learn',
             'never', 'other', 'place', 'plant', 'point', 'right', 'small', 'sound', 'spell', 'still', 'study', 'their',
             'there', 'these', 'thing', 'think', 'three', 'water', 'where', 'which', 'world', 'would', 'write']

    first_letters = input("First letters: ").split()
    possible_words_first, possible_words_fourth = [], []

    [[possible_words_first.append(word) for word in words if word[0] == letter] for letter in first_letters]
    print(possible_words_first)
    fourth_letters = input("Third letters: ").split()
    [[possible_words_fourth.append(word) for word in possible_words_first if word[2] == letter] for letter in
     fourth_letters]
    print("Answer:\n{}".format(possible_words_fourth))


def complicated_wires(is_odd, has_parallel, num_batteries):
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


def words_game():
    position_dict = {1: 'top left', 2: 'middle left', 3: 'bottom left',
                     4: 'top right', 5: 'middle right', 6: 'bottom right'}
    label_dict = {'yes': '2', 'first': '4', 'display': '6', 'okay': '4', 'says': '6',
                  'nothing': '2', '_': '3', 'blank': '5', 'no': '6', 'led': '2', 'lead': '6',
                  'read': '5', 'red': '5', 'reed': '3', 'leed': '3', 'hold_on': '6', 'you': '5',
                  'you_are': '6', 'your': '5', 'youre': '5', 'ur': '1', 'there': '6', 'theyre': '3',
                  'their': '5', 'they_are': '2', 'see': '6', 'c': '4', 'cee': '6'}
    order_dict = {"BLANK": "WAIT, RIGHT, OKAY, MIDDLE, BLANK, PRESS, READY, NOTHING, NO, WHAT, LEFT, UHHH, YES, FIRST",
                  "DONE": "SURE, UH HUH, NEXT, WHAT?, YOUR, UR, YOU'RE, HOLD, LIKE, YOU, U, YOU ARE, UH UH, DONE",
                  "FIRST": "LEFT, OKAY, YES, MIDDLE, NO, RIGHT, NOTHING, UHHH, WAIT, READY, BLANK, WHAT, PRESS, FIRST",
                  "HOLD": "YOU ARE, U, DONE, UH UH, YOU, UR, SURE, WHAT?, YOU'RE, NEXT, HOLD, UH HUH, YOUR, LIKE",
                  "LEFT": "RIGHT, LEFT, FIRST, NO, MIDDLE, YES, BLANK, WHAT, UHHH, WAIT, PRESS, READY, OKAY, NOTHING",
                  "LIKE": "YOU'RE, NEXT, U, UR, HOLD, DONE, UH UH, WHAT?, UH HUH, YOU, LIKE, SURE, YOU ARE, YOUR",
                  "MIDDLE": "BLANK, READY, OKAY, WHAT, NOTHING, PRESS, NO, WAIT, LEFT, MIDDLE, RIGHT, FIRST, UHHH, YES",
                  "NEXT": "WHAT?, UH HUH, UH UH, YOUR, HOLD, SURE, NEXT, LIKE, DONE, YOU ARE, UR, YOU'RE, U, YOU",
                  "NO": "BLANK, UHHH, WAIT, FIRST, WHAT, READY, RIGHT, YES, NOTHING, LEFT, PRESS, OKAY, NO, MIDDLE",
                  "NOTHING": "UHHH, RIGHT, OKAY, MIDDLE, YES, BLANK, NO, PRESS, LEFT, WHAT, WAIT, FIRST, NOTHING, READY",
                  "OKAY": "MIDDLE, NO, FIRST, YES, UHHH, NOTHING, WAIT, OKAY, LEFT, READY, BLANK, PRESS, WHAT, RIGHT",
                  "PRESS": "RIGHT, MIDDLE, YES, READY, PRESS, OKAY, NOTHING, UHHH, BLANK, LEFT, FIRST, WHAT, NO, WAIT",
                  "READY": "YES, OKAY, WHAT, MIDDLE, LEFT, PRESS, RIGHT, BLANK, READY, NO, FIRST, UHHH, NOTHING, WAIT",
                  "RIGHT": "YES, NOTHING, READY, PRESS, NO, WAIT, WHAT, RIGHT, MIDDLE, LEFT, UHHH, BLANK, OKAY, FIRST",
                  "SURE": "YOU ARE, DONE, LIKE, YOU'RE, YOU, HOLD, UH HUH, UR, SURE, U, WHAT?, NEXT, YOUR, UH UH",
                  "U": "UH HUH, SURE, NEXT, WHAT?, YOU'RE, UR, UH UH, DONE, U, YOU, LIKE, HOLD, YOU ARE, YOUR",
                  "UH HUH": "UH HUH, YOUR, YOU ARE, YOU, DONE, HOLD, UH UH, NEXT, SURE, LIKE, YOU'RE, UR, U, WHAT?",
                  "UH UH": "UR, U, YOU ARE, YOU'RE, NEXT, UH UH, DONE, YOU, UH HUH, LIKE, YOUR, SURE, HOLD, WHAT?",
                  "UHHH": "READY, NOTHING, LEFT, WHAT, OKAY, YES, RIGHT, NO, PRESS, BLANK, UHHH, MIDDLE, WAIT, FIRST",
                  "UR": "DONE, U, UR, UH HUH, WHAT?, SURE, YOUR, HOLD, YOU'RE, LIKE, NEXT, UH UH, YOU ARE, YOU",
                  "WAIT": "UHHH, NO, BLANK, OKAY, YES, LEFT, FIRST, PRESS, WHAT, WAIT, NOTHING, READY, RIGHT, MIDDLE",
                  "WHAT": "UHHH, WHAT, LEFT, NOTHING, READY, BLANK, MIDDLE, NO, OKAY, FIRST, WAIT, YES, PRESS, RIGHT",
                  "WHAT?": "YOU, HOLD, YOU'RE, YOUR, U, DONE, UH UH, LIKE, YOU ARE, UH HUH, UR, NEXT, WHAT?, SURE",
                  "YES": "OKAY, RIGHT, UHHH, MIDDLE, FIRST, WHAT, PRESS, READY, NOTHING, YES, LEFT, BLANK, NO, WAIT",
                  "YOU ARE": "YOUR, NEXT, LIKE, UH HUH, WHAT?, DONE, UH UH, HOLD, YOU, U, YOU'RE, SURE, UR, YOU ARE",
                  "YOU": "SURE, YOU ARE, YOUR, YOU'RE, NEXT, UH HUH, UR, HOLD, WHAT?, YOU, UH UH, LIKE, DONE, U",
                  "YOURE": "YOU, YOU'RE, UR, NEXT, UH UH, YOU ARE, U, YOUR, WHAT?, UH HUH, SURE, DONE, LIKE, HOLD",
                  "YOUR": "UH UH, YOU ARE, UH HUH, YOUR, NEXT, UR, SURE, U, YOU'RE, YOU, WHAT?, HOLD, LIKE, DONE"}

    while True:
        try:
            position = position_dict[int(label_dict[input("Enter given word ").lower()])]
            print(position)
            order = order_dict[input("Enter word: ").upper()]
            print(order)
        except KeyError:
            print("Typo, try again.")
            words_game()


def morse_translator():
    morse_dict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
                  '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
                  '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
                  '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
                  '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
                  '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--':
                  '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
                  '---..': '8', '----.': '9'}
    result = ""

    prompt = input("Enter morse code separated by whitespace: ").split()
    for item in prompt:
        try:
            result += morse_dict[item]
        except KeyError:
            print("Unknown morse. Try again.")

    print(result)


def main():
    # TODD: GET PARSING BOMB DATA WORKING, MAKE GAME CHOOSER SIMPLER
    """
    vowels = ['a', 'e', 'i', 'o', 'u']

    serial_num = input("Serial number? ").split()
    has_vowels = any([letter.lower() in vowels for letter in serial_num])
    is_odd = bool(int(serial_num[-1]) % 2)
    num_batteries = int(input("Number of batteries? "))
    has_parallel = True if input("Has parallel port? ").lower() in ["yes", "y"] else False
    print()
    """
    morse_translator()


if __name__ == "__main__":
    main()
