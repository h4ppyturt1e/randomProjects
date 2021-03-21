from typing import List
from math import factorial

data = 'day10.txt'
test_data = 'day10test.txt'


def data_to_lonumbers(filename: str) -> List[int]:
    """takes the data and sorts it """
    with open(filename) as f:
        lonumbers = [int(line.rstrip()) for line in f.readlines()]
    lonumbers.append(0)
    lonumbers.sort()
    lonumbers.append(lonumbers[-1]+3)
    return lonumbers


def part_a(filename: str) -> (int, int):
    lonumbers = data_to_lonumbers(filename)
    count_1 = 0
    count_3 = 0
    for i in range(len(lonumbers)-1):
        diff = lonumbers[i+1] - lonumbers[i]
        if diff == 1:
            count_1 += 1
        elif diff == 3:
            count_3 += 1
    print(count_1, count_3, count_1 * count_3)
    return count_1, count_3


def part_b(filename: str) -> int:
    lonumbers = data_to_lonumbers(filename)
    paths = [0] * (max(lonumbers) + 1)
    paths[0] = 1
    for index in range(1, max(lonumbers) + 1):
        for x in range(1, 4):
            if index - x in lonumbers:
                paths[index] += paths[index - x]
    print('paths:', paths)
    return paths[-1]


tested_file = data
print(part_a(tested_file), part_b(tested_file))
