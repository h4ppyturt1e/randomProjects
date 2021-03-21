from base_converter import convert_to_binary, convert_to_decimal
from typing import List, Tuple

real = 'day14.txt'
test = 'day14test.txt'

with open(real) as file:
    data = [x.rstrip() for x in file.readlines()]

mask_dicts = {}  # takes data and converts it into a Dict[mask: Dict[mem address: value in binary]
for line in data:
    if line[:4] == 'mask':
        cur_mask = line[7:]
        mem_dict = {}
        # if cur_mask in mask_dicts:
        #     print('DUPLICATE')
    else:
        mem = int(line[4:line.index(']')])
        value = convert_to_binary(line[line.index('=')+2:])
        if len(value) != 36:
            missing = 36 - len(value)
            value = '0' * missing + value
        mem_dict[mem] = value
        mask_dicts[cur_mask] = mem_dict
# print('mask_dicts: {}'.format(mask_dicts))

lomaskAddA = {}
for mask in mask_dicts:
    mask_instructions = [(i, mask[i]) for i in range(len(mask)) if mask[i] != 'X']
    for mem_add in mask_dicts[mask]:
        value = list(mask_dicts[mask][mem_add])
        for instruction in mask_instructions:
            i, x = instruction[0], instruction[1]
            value[i] = x
        lomaskAddA[mem_add] = convert_to_decimal(''.join(value), 2)

totalA = 0
for maskAdd in lomaskAddA:
    totalA += lomaskAddA[maskAdd]
print('Total in (a): {}'.format(totalA))

dict_memAdd = {}
for mask in mask_dicts:
    mask_instructions = list(enumerate(mask))
    # print(mask_instructions)
    for mem_add in mask_dicts[mask]:
        value = convert_to_decimal(mask_dicts[mask][mem_add], 2)
        mem_add = convert_to_binary(str(mem_add))
        mem_add = list('0' * (36-len(mem_add)) + mem_add)
        # print(mem_add, value)
        for instruction in mask_instructions:
            i, x = instruction[0], instruction[1]
            if x != '0':
                mem_add[i] = x
        dict_memAdd[''.join(mem_add)] = value
# print(dict_memAdd)
# print('\n')


def get_x_branches(mem_add):
    temp_mask_add = []
    new_mem_add = list(mem_add)
    if 'X' in new_mem_add:
        for i, x in list(enumerate(new_mem_add)):  # for each char in mem_add
            if x == 'X':
                new_mem_add[i] = 0
                testing = get_x_branches(new_mem_add)
                temp_mask_add += testing
                new_mem_add[i] = 1
                testing = get_x_branches(new_mem_add)
                temp_mask_add += testing
                return temp_mask_add
    else:
        temp_mask_add.append(''.join(str(x) for x in new_mem_add))
        return temp_mask_add


dict_multiAdd = {}
for mem_add in dict_memAdd:
    value = dict_memAdd[mem_add]
    multiAdd = get_x_branches(mem_add)
    for add in multiAdd:
        dict_multiAdd[add] = value

totalB = sum(dict_multiAdd.values())
print('Total in (b): {}'.format(totalB))
