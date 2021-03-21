from typing import List, Dict, Tuple
import time

input_file = 'day7.txt'
test_file = 'day7test.txt'


# BagInfo tuple
BagInfo = Tuple[int, str]
NUM = 0
COLOR = 1
# Dictionary of bags
BagDict = Dict[str, List[BagInfo]]
#   0       1      2      3    4  5    6   7    8  9      10     11  12   13     14    15  16    17       18     19
# light turquoise bags contain 5 posh red bags, 1 dim chartreuse bag, 3 vibrant beige bags, 2 mirrored lavender bags.
# ['light', 'red', 'bags', 'contain', '1', 'bright', 'white', 'bag,', '2', 'muted', 'yellow', 'bags.']


def data_to_dict(filename: str) -> BagDict:
    """ Creates a dictionary of bag information for each bag in the data """
    bag_dict = {}
    with open(filename) as f:
        for line in f:
            line = line.split()
            outer_bag = line[0] + line[1]
            list_inner_bags = []
            if line[4] != 'no':
                for i in range(5, 21, 4):
                    if i < len(line):
                        num_bags = int(line[i-1])
                        inner_colour = line[i] + line[i+1]
                        list_inner_bags.append((num_bags, inner_colour))
            bag_dict[outer_bag] = list_inner_bags
    return bag_dict


def can_hold(checked_bag: str, bag_dict: BagDict) -> BagDict:
    eligible_bags = {}
    for outer_bag in bag_dict:
        for i in range(len(bag_dict[outer_bag])):
            if bag_dict[outer_bag][i][1] == checked_bag:   # inner_name of each element of each bag in bag_dict
                eligible_bags[outer_bag] = bag_dict[outer_bag]
    return eligible_bags


def get_total_bags(bag_dict: BagDict, checked_bag: str) -> List:
    total_bags = []
    eligible_bags = can_hold(checked_bag, bag_dict)
    list_eligible = [bag for bag in eligible_bags]
    total_bags += list_eligible
    for bag in list_eligible:
        total_bags += get_total_bags(bag_dict, bag)
    return total_bags


def part_a(filename: str, checked_bag: str) -> int:
    start_time = time.time()
    bag_dict = data_to_dict(filename)
    total_bags = get_total_bags(bag_dict, checked_bag)
    unique_bags = set(total_bags)
    print('For {}, part (a): {}, solved in {} seconds'.format(filename, len(unique_bags), time.time() - start_time))
    return len(unique_bags)


def get_bag_cardinality(bag_dict: BagDict, checked_bag: str) -> int:
    # 'lightred': [(1, 'brightwhite'), (2, 'mutedyellow')]
    cardinality = 0
    contents = bag_dict[checked_bag]
    for color in contents:
        cur_num = color[NUM]
        cur_color = color[COLOR]
        cur_cardinality = get_bag_cardinality(bag_dict, cur_color)
        cardinality += cur_num + cur_cardinality * cur_num
    return cardinality


def part_b(filename: str, checked_bag: str) -> int:
    start_time = time.time()
    bag_dict = data_to_dict(filename)
    total_bags = get_bag_cardinality(bag_dict, checked_bag)
    print('For {}, part (b): {}, solved in {} seconds'.format(filename, total_bags, time.time() - start_time))
    return total_bags


part_a(test_file, 'shinygold')
part_b(test_file, 'shinygold')

part_a(input_file, 'shinygold')
part_b(input_file, 'shinygold')
