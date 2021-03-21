from typing import List, Tuple

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

filename = 'day6.txt'
filename2 = 'day6test.txt'

# GroupInfo(member_list, num_members)
GroupInfo = Tuple[List[str], int]
MEMBERS = 0
COUNT = 1


def data_to_grp_tuple(file_name: str) -> List[GroupInfo]:
    with open(file_name, 'r') as f:
        grp_list = []
        cur_grp = []
        grp_len = 0
        for line in f:
            line = line.rstrip()
            if line != '':
                cur_grp.append(line)
                grp_len += 1
            else:
                group_info = (cur_grp, grp_len)
                grp_list.append(group_info)
                cur_grp = []
                grp_len = 0
    return grp_list


def count_answers_b(grp: GroupInfo) -> int:
    # (['a', 'b', 'c'], 3)
    count = 0
    for letter in alphabet_list:
        is_valid = True
        for member in grp[MEMBERS]:  # ['a', 'b', 'c']
            if letter not in member:
                is_valid = False
        if is_valid:
            count += 1
    return count


def part_b(file_name: str) -> int:
    grp_list = data_to_grp_tuple(file_name)
    total = 0
    for grp in grp_list:
        total += count_answers_b(grp)
    print('Sum of total count on each group for (b): ', total)
    return total
