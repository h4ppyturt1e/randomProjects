from typing import List, Tuple
file_name = 'day4.txt'

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

#        (value, units) for example (150, 'cm')
Height = Tuple[int, str]
VAL_HEIGHT = 0
UNIT = 1


#    (byr, iyr, eyr, Height(value, units), hcl, ecl, pid, is_9)
Passport = Tuple[int, int, int, Height, str, str, int, bool]
BYR = 0
IYR = 1
EYR = 2
HEIGHT = 3
HCL = 4
ECL = 5
PID = 6
IS_9 = 7

def data_to_lopassports(filename: str) -> List[Passport]:
    lopassports = []
    lodata = []
    cur_data = ''
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            if line != '':
                if cur_data == '':
                    cur_data = line
                else:
                    cur_data += ' ' + line
            else:
                cur_data = cur_data.split(' ')
                lodata.append(cur_data)
                cur_data = ''
    for passport in lodata:
        byr = -1
        iyr = -1
        eyr = -1
        hgt = (-1, '-')
        hcl = '-'
        ecl = '-'
        pid = -1
        is_9 = False
        for info in passport:
            data_type = info[0:3]
            if data_type == 'byr':
                byr = 1
                if info[4:].isdigit():
                    byr = int(info[4:])
            if data_type == 'iyr':
                iyr = 1
                if info[4:].isdigit():
                    iyr = int(info[4:])
            if data_type == 'eyr':
                eyr = 1
                if info[4:].isdigit():
                    eyr = int(info[4:])
            if data_type == 'hgt':
                hgt_info = info[4:]
                hgt_value = ''
                hgt_unit = ''
                for i in range(len(hgt_info)):
                    if hgt_info[i].isdigit():
                        hgt_value += hgt_info[i]
                    else:
                        hgt_unit += hgt_info[i]
                hgt_value = int(hgt_value)
                hgt = (hgt_value, hgt_unit)
            if data_type == 'hcl':
                hcl = info[4:]
            if data_type == 'ecl':
                ecl = info[4:]
            if data_type == 'pid':
                pid = 1
                if info[4:].isdigit():
                    pid = int(info[4:])
                    if len(info[4:]) == 9:
                        is_9 = True
        passport = (byr, iyr, eyr, hgt, hcl, ecl, pid, is_9)
        lopassports.append(passport)
    print(lopassports)
    return lopassports


def check_fields(passport: Passport) -> bool:
    # (1955, 2014, 2030, (187, 'cm'), '#5637d2', 'grn', 862655087)
    is_valid = True
    for i in range(len(passport)):
        cur_data = passport[i]
        if i == 3:
            if (cur_data[VAL_HEIGHT] == -1) or (cur_data[UNIT] == '-'):
                is_valid = False
        else:
            if cur_data == -1 or cur_data == '-':
                is_valid = False
    return is_valid


def part_a(filename) -> (List[Passport], int):
    valid_passports = []
    lopassports = data_to_lopassports(filename)
    for passport in lopassports:
        if check_fields(passport):
            valid_passports.append(passport)
    print('List: {}\nNumber of valid passports in (a): {}'.format(valid_passports, len(valid_passports)))
    return valid_passports, len(valid_passports)


def check_info(passport: Passport) -> bool:
    valid_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    valid_hair_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    is_valid = True
    if passport[HEIGHT][UNIT] == 'cm':
        if not (150 <= passport[HEIGHT][VAL_HEIGHT] <= 193):
            is_valid = False
    if passport[HEIGHT][UNIT] == 'in':
        if not (59 <= passport[HEIGHT][VAL_HEIGHT] <= 76):
            is_valid = False
    if passport[HEIGHT][UNIT] == '' or passport[HEIGHT][UNIT] == '-':
        is_valid = False
    if is_valid:
        if not (1920 <= passport[BYR] <= 2002 and
                2010 <= passport[IYR] <= 2020 and
                2020 <= passport[EYR] <= 2030 and
                passport[IS_9] and
                passport[ECL] in valid_eye_colors):
            is_valid = False
    if passport[HCL][0] == '#':
        for i in range(1, len(passport[HCL])):
            if not (passport[HCL][i] in valid_hair_chars):
                is_valid = False
    if passport[HCL][0] != '#':
        is_valid = False
    if len(passport[HCL][1:]) != 6:
        is_valid = False
    return is_valid


def part_b(filename) -> int:
    lopassports = data_to_lopassports(filename)
    count = 0
    for passport in lopassports:
        if check_info(passport):
            count += 1
    print('Number of valid passports in (b):', count)
    return count


part_a(file_name)
part_b(file_name)