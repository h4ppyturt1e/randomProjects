from typing import List, Dict

# FBFBBFFRLR: row 44, column 5, seat ID 357.
# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820.

filename = 'day5.txt'


def file_to_lolines(filename: 'str') -> List[str]:
    lolines = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            lolines.append(line)
    return lolines


def get_row(given_handle: str) -> int:
    handle = given_handle[:7]
    length = len(handle)
    row_max = 127
    row_min = 0
    for i in range(length):
        char = handle[i]
        power = length - i - 1
        diff = 2 ** power
        if char == 'F':
            row_max -= diff
        elif char == 'B':
            row_min += diff
    return row_max


def get_column(given_handle: str) -> int:
    handle = given_handle[7:]
    length = len(handle)
    column_max = 7
    column_min = 0
    for i in range(length):
        char = handle[i]
        power = length - i - 1
        diff = 2 ** power
        if char == 'L':
            column_max -= diff
        elif char == 'R':
            column_min += diff
    return column_max


def get_seat_id(given_handle: str) -> int:
    row = get_row(given_handle)
    column = get_column(given_handle)
    seat_id = row * 8 + column
    return seat_id


def lolines_to_lo_seat_ids(lolines: List[str]) -> List[int]:
    lo_seat_ids = []
    for handle in lolines:
        seat_id = get_seat_id(handle)
        lo_seat_ids.append(seat_id)
    return lo_seat_ids


def get_info(filename: str) -> (List[str], List[int], Dict[int, str]):
    seat_id_to_handle = {}
    lolines = file_to_lolines(filename)
    lo_seat_ids = lolines_to_lo_seat_ids(lolines)
    for i in range(len(lolines)):
        seat_id = lo_seat_ids[i]
        handle = lolines[i]
        seat_id_to_handle[seat_id] = handle
    return lolines, lo_seat_ids, seat_id_to_handle


def part_a(filename: str) -> (int, str):
    info = get_info(filename)
    lo_seat_ids = info[1]
    seat_id_to_handle = info[2]
    lo_seat_ids.sort()
    highest_seat_id = lo_seat_ids[-1]
    highest_handle = seat_id_to_handle[highest_seat_id]
    print('Highest seat id:', highest_seat_id)
    return highest_seat_id, highest_handle


def part_b(filename):
    info = get_info(filename)
    lo_seat_ids = info[1]
    lo_seat_ids.sort()
    current = lo_seat_ids[0]
    not_found = True
    i = 0
    while not_found:
        if lo_seat_ids[i] != current:
            print('The missing seat number is:', current)
            not_found = False
        else:
            current += 1
            i += 1


part_a(filename)
part_b(filename)