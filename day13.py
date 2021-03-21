from typing import List
import time

real = 'day13.txt'
test = 'day13test.txt'

with open(real) as file:
    data = [x.rstrip() for x in file.readlines()]

# data into usable lists
timestamp = int(data[0])
bus_list = data[1].split(',')
# print("timestamp: {}\nbus_list: {}".format(timestamp, bus_list))

# list of available buses (not an x)
av_buses = [int(item) for item in bus_list if item.isdigit()]
print('av_buses: {}'.format(av_buses))

# list of timestamps of buses in base current time
lotimestamps = [timestamp % bus_id for bus_id in [int(item) for item in bus_list if item.isdigit()]]
print('lotimestamps: {}'.format(lotimestamps))

# list of buses that have timestamps after current time
# nearest = [(av_buses[i] - lotimestamps[i], av_buses[i]) for i in range(len(av_buses)) if
#            lotimestamps[i] > (av_buses[i] - lotimestamps[i])]
# print('nearest: {}\n'.format(nearest))
# print('Part(a): {}\n'.format(min(nearest)[0] * min(nearest)[1]))

# index of bus_id in the given bus_list
bus_index = [bus_list.index(str(bus_id)) for bus_id in bus_list if bus_id.isdigit()]
print('bus_index: {}'.format(bus_index))

mod_pair = [(bus_index[-1] - bus_index[i], av_buses[i]) for i in range(len(av_buses))]
print('mod_pair: {}'.format(mod_pair))

# mod_pair = [(9, 10), (9, 11), (0, 13)]
new_mod = 1
for mod in mod_pair:
    new_mod *= mod[1]
print(new_mod)

total = 0
for mod in mod_pair:
    b = mod[0]
    cur_mod = mod[1]
    n = int(new_mod / cur_mod)
    x = n % cur_mod
    for i in range(cur_mod+1):
        if (x * i) % cur_mod == 1:
            bnx = b * n * i
            break
    total += bnx
print(total, (total % new_mod) - mod_pair[0][0])
