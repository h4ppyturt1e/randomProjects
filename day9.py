from typing import List

test_data = 'day9test.txt'
input_data = 'day9.txt'


def data_to_lonumbers(filename: str) -> List[int]:
    with open(filename) as f:
        lonumbers = [int(line) for line in f.readlines()]
    print(lonumbers)
    return lonumbers


def check_for_sum(snippet: List[int]) -> bool:
    is_valid = False
    for i in snippet[:-1]:
        for i2 in snippet[:-1]:
            if i + i2 == snippet[-1] and i != i2:
                is_valid = True
    return is_valid


def part_a(preamble: int, filename: str) -> (int, List[int]):
    lonumbers = data_to_lonumbers(filename)
    length = len(lonumbers)
    start_index = 0
    end_index = preamble + 1
    for i in range(length):
        cur_snippet = lonumbers[start_index: end_index]
        if i <= end_index and not check_for_sum(cur_snippet):
            print(cur_snippet)
            print('The number in (a) is {}'.format(cur_snippet[-1]))
            return cur_snippet[-1], lonumbers
        else:
            start_index += 1
            end_index += 1


def part_b(preamble: int, filename: str) -> int:
    invalid_number = part_a(preamble, filename)
    lonumbers = invalid_number[1]
    print('Invalid number: {}!'.format(invalid_number[0]))
    for number in lonumbers:
        contiguous_range = [number]
        start_index = lonumbers.index(number)
        for i in range(start_index, len(lonumbers)):
            if start_index != i:
                contiguous_range.append(lonumbers[i])
            total = sum(contiguous_range)
            if total > invalid_number[0]:
                break
            elif total == invalid_number[0]:
                print(contiguous_range)
                contiguous_range.sort()
                sum_bounds = contiguous_range[0] + contiguous_range[-1]
                print('Sum of bounds of contiguous numbers in (b): {}!'.format(sum_bounds))
                return sum_bounds


part_b(5, test_data)
print('\n')
# part_b(25, input_data)
