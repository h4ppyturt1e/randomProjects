from typing import List
import time
real = 'day12.txt'
test = 'day12test.txt'

with open(real) as file:
    data = [x.rstrip() for x in file.readlines()]

card_to_num = {'N': 0, 'E': 1, 'S': 2, 'W': 3}  # cardinal direction to assigned number value
num_to_card = {0: 'N', 1: 'E', 2: 'S', 3: 'W'}  # assigned number value to cardinal direction
value_dict = {90: 1, 180: 2, 270: 3, 360: 4}
move_dir_to_coords = {}


def decrypt_command(facing: int, line: str) -> (int, str, int):  # returns (facing, direction, value)
    action = line[0]
    value = int(line[1:])
    if action in ['L', 'R']:
        d_num = value_dict[value]  # takes degree change into assigned number value change
        if action == 'L':
            facing = (facing - d_num) % 4
            return facing, None, None
        elif action == 'R':
            facing = (facing + d_num) % 4
            return facing, None, None
    elif action == 'F':
        direction = num_to_card[facing]
        return facing, direction, value
    else:
        return facing, action, value


def start_moving(start_dir: str):
    facing = card_to_num[start_dir]
    x = 0
    y = 0
    locommands = []
    for line in data:
        # print(line)
        command = decrypt_command(facing, line)
        # print(command)
        locommands.append(command)
        facing = command[0]
    for command in locommands:
        move_dir = command[1]
        move_distance = command[2]
        if move_dir in ['N', 'E', 'S', 'W']:
            if move_dir == 'N':
                y += move_distance
            elif move_dir == 'E':
                x += move_distance
            elif move_dir == 'S':
                y -= move_distance
            elif move_dir == 'W':
                x -= move_distance
    print('x: {}, y: {}'.format(x, y))
    return x, y


def decrypt_command_b(x: int, y: int, line: str) -> (int, int):
    action = line[0]
    value = int(line[1:])
    if action in ['N', 'E', 'S', 'W']:
        if action == 'N':
            return x, y-value, False
        elif action == 'E':
            return x+value, y, False
        elif action == 'S':
            return x, y+value, False
        elif action == 'W':
            return x-value, y, False
    elif action in ['L', 'R']:
        direc = value_dict[value]
        cur_x, cur_y = x, y
        if action == 'L':
            for times in range(direc):
                x, y = cur_y, -cur_x
                cur_x, cur_y = x, y  # I FORGOT THIS
        elif action == 'R':
            for times in range(direc):
                x, y = -cur_y, cur_x
                cur_x, cur_y = x, y  # AND THIS
        return x, y, False
    elif action == 'F':
        return x * value, y * value, True


def start_moving_b(x: int, y: int):
    ship_x = 0
    ship_y = 0
    for line in data:
        print(line)
        command = decrypt_command_b(x, y, line)
        print(command)
        if command[2]:
            ship_x, ship_y = (ship_x + command[0]), (ship_y + command[1])
        else:
            x, y = command[0], command[1]
        print('WP', x, y, '\n')
        print(ship_x, ship_y)
    print('x: {}, y: {}'.format(ship_x, ship_y))
    return ship_x, ship_y


def solve():
    start = time.time()
    final_pos = start_moving('E')
    print('Part (a):', abs(final_pos[0]) + abs(final_pos[1]))
    final_pos_b = start_moving_b(10, -1)
    print('Part (b):', abs(final_pos_b[0]) + abs(final_pos_b[1]))
    print(time.time() - start, 'seconds')


solve()
