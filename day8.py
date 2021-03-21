from typing import List

test_data = 'day8test.txt'
input_data = 'day8.txt'


def data_to_lines(filename: str) -> List[str]:
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]

# ['nop +0', 'acc +1', 'jmp +4', 'acc +3', 'jmp -3', 'acc -99', 'acc +1', 'jmp -4', 'acc +6']


def play_game(lines) -> (int, bool):  # outputs new index
    score = 0
    index = 0
    cur_line = lines[index]
    lines_passed = []
    program_terminated = False
    while index not in lines_passed:
        cmd = cur_line[:3]
        value = cur_line[5:]
        operator = cur_line[4]
        lines_passed.append(index)
        if index == len(lines)-1:
            program_terminated = True
        if cmd == 'nop':
            index += 1
        elif cmd == 'acc':
            index += 1
            if operator == '+':
                score += int(value)
            else:
                score -= int(value)
        elif cmd == 'jmp':
            if operator == '+':
                index += int(value)
            else:
                index -= int(value)
        if index < len(lines):
            cur_line = lines[index]
        else:
            lines_passed.append(index)
    return score, program_terminated


def switcheroo(lines: List[str]) -> List[List[str]]:
    index = 0
    lines = tuple(lines)
    lonew_lines = []
    for line in lines:
        test_lines = list(lines)
        cmd = line[:3]
        line_data = line[3:]
        if cmd == 'jmp':
            test_lines[index] = 'nop' + line_data
            lonew_lines.append(test_lines)
        elif cmd == 'nop':
            test_lines[index] = 'jmp' + line_data
            lonew_lines.append(test_lines)
        index += 1
    return lonew_lines


def part_b(filename: str) -> int:
    lololines = switcheroo(data_to_lines(filename))
    for loline in lololines:
        game_result = play_game(loline)
        if game_result[1]:
            print(game_result[0])
            return game_result[0]


part_b(input_data)

string = 'test'

string.capitalize()

print(string)