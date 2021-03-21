from typing import List, Tuple
from day6b import part_b

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

filename = 'day6.txt'
filename2 = 'day6test.txt'

# (group as a str, number of members in group)
GroupInfo = Tuple[str, int]
STR = 0
MEMBERS = 1


def data_to_grp_tuple(file_name: str) -> List[GroupInfo]:
    with open(file_name, 'r') as f:
        grp_list = []
        cur_grp = ''
        grp_len = 0
        for line in f:
            line = line.rstrip()
            if line != '':
                cur_grp += line
                grp_len += 1
            else:
                group_info = (cur_grp, grp_len)
                grp_list.append(group_info)
                cur_grp = ''
                grp_len = 0
        print('Number of groups:', len(grp_list))
    return grp_list


def count_answers_a(grp_str: str) -> int:
    unique_answers = []
    for char in grp_str:
        if (char in alphabet_list) and \
           (char not in unique_answers):
            unique_answers.append(char)
    return len(unique_answers)


def sum_answers_a(grp_list: List[GroupInfo]) -> int:
    sum_answers = 0
    for grp in grp_list:
        cur_answers = count_answers_a(grp[STR])
        sum_answers += cur_answers
    return sum_answers


def part_a(file_name: str) -> int:
    grp_list = data_to_grp_tuple(file_name)
    total = sum_answers_a(grp_list)
    print('Sum of total count on each group for (a): ', total)
    return total


part_a(filename)
part_b(filename)
