from typing import List
import time
real = 'day11.txt'
test = 'day11test.txt'

# ['L.LL.LL.LL',
#  'LLLLLLL.LL',
#  'L.L.L..L..',
#  'LLLL.LL.LL',
#  'L.LL.LL.LL',
#  'L.LLLLL.LL',
#  '..L.L.....',
#  'LLLLLLLLLL',
#  'L.LLLLLL.L',
#  'L.LLLLL.LL']

# direction dictionary with {Direction: (y-shift, x-shift)}
dir_dict = {'N': (0, -1), 'NE': (1, -1), 'E': (1, 0), 'SE': (1, 1),
            'S': (0, 1), 'SW': (-1, 1), 'W': (-1, 0), 'NW': (-1, -1)}


with open(real) as file:
    given_data = [x.rstrip() for x in file.readlines()]
max_x = len(given_data[0])
max_y = len(given_data)
print(max_x, max_y)


def check_around(data, x, y) -> int:
    num_occupied = 0
    for direc in dir_dict:
        dx = x + dir_dict[direc][0]
        dy = y + dir_dict[direc][1]
        # print(direc, dx, dy)
        try:
            if dx >= 0 and dy >= 0 and data[dy][dx] == '#':
                num_occupied += 1
        except IndexError:
            pass
    return num_occupied


def check_cardinal(data, x, y) -> int:
    num_occupied = 0
    for direc in dir_dict:
        dx, dy = dir_dict[direc][0], dir_dict[direc][1]
        cur_x, cur_y = x + dx, y + dy
        keep_going = True
        while (0 <= cur_x < max_x) and (0 <= cur_y < max_y) and keep_going:
            try:
                cur_seat = data[cur_y][cur_x]
                if cur_seat == '#':
                    num_occupied += 1
                    keep_going = False
                elif cur_seat == 'L':
                    keep_going = False
            except IndexError:
                keep_going = False
            cur_x, cur_y = cur_x + dx, cur_y + dy
    return num_occupied


def transform(check_type, data: List[str], max_occupied: int) -> List[str]:
    new_data = []
    for y in range(max_y):
        line = data[y]
        new_line = ''
        for x in range(max_x):
            if line[x] == '.':
                new_line += '.'
            elif line[x] == 'L':
                if check_type(data, x, y) == 0:
                    new_line += '#'
                else:
                    new_line += 'L'
            elif line[x] == '#':
                if check_type(data, x, y) >= max_occupied:
                    new_line += 'L'
                else:
                    new_line += '#'
        new_data.append(new_line)
    return new_data


def get_stationary_matrix(part: str, data: List[str], max_occupied: int) -> List[str]:
    keep_going = True
    if part == 'a':
        check_type = check_around
    elif part == 'b':
        check_type = check_cardinal
    while keep_going:
        new_data = transform(check_type, data, max_occupied)
        # print('\n')
        if new_data == data:
            return new_data
        else:
            data = new_data


def solve():
    start = time.time()
    count_a = 0
    count_b = 0
    joined_data_a = ''.join(get_stationary_matrix('a', given_data, 4))
    for i in range(len(joined_data_a)):
        if joined_data_a[i] == '#':
            count_a += 1
    joined_data_b = ''.join(get_stationary_matrix('b', given_data, 5))
    for i in range(len(joined_data_b)):
        if joined_data_b[i] == '#':
            count_b += 1
    print('(a): {} occupied seats\n(b): {} occupied seats\nSolved in {} seconds'.format(count_a, count_b, time.time() - start))
    return count_a, count_b, time.time() - start


solve()
