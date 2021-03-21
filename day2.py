# represents range for the number of characters allowed as [min, max]
MIN = 0
MAX = 1

# represents current line info as [range, letter, password]
RANGE = 0
CHAR = 1
PASS = 2

number_of_valid = 0
f = open('day2.txt', 'r')
for line in f:
    count = 0
    line = line.rstrip()
    line = line.split(' ')
    ranges = line[RANGE].split('-')
    cur_min = int(ranges[MIN])
    cur_max = int(ranges[MAX])
    cur_char = line[CHAR].rstrip(':')
    cur_pass = line[PASS]
    for i in range(len(cur_pass)):
        cur_letter = cur_pass[i]
        if cur_letter == cur_char:
            count += 1
    if cur_min <= count <= cur_max:
        number_of_valid += 1
f.close()

print("Number of valid passwords in (a):", number_of_valid)

number_of_valid = 0
f = open('day2.txt', 'r')
for line in f:
    count = 0
    line = line.rstrip()
    line = line.split(' ')
    ranges = line[RANGE].split('-')
    low_index = int(ranges[MIN])-1
    high_index = int(ranges[MAX])-1
    cur_char = line[CHAR].rstrip(':')
    cur_pass = line[PASS]
    if cur_pass[low_index] == cur_char and cur_pass[high_index] != cur_char:
        is_valid = True
    elif cur_pass[low_index] != cur_char and cur_pass[high_index] == cur_char:
        is_valid = True
    else:
        is_valid = False
    if is_valid:
        number_of_valid += 1
f.close()

print("Number of valid passwords in (b):", number_of_valid)