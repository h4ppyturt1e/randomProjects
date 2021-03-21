import time

test1 = '0,3,6'  # 436 -> 0 3 6 0 3 3 1 0 4 0
test2 = '2,1,3'  # 10
test3 = '3,1,2'  # 1836
real = '0,1,4,13,15,12,16'


def get_nth(data, max_turn) -> int:
    x_list = [x for i, x in reversed(list(enumerate(data.split(','))))]  # 0 3 6 0 3 3 1 0 4 0
    # print('Data size: {}'.format(max_turn))
    for turn in range(len(x_list), max_turn):       # starts iterating from cur turn up to max turn (2020)
        last_x = x_list[0]                          # takes the second last element (technically index 1 bc reversed)
        try:                                        # tries checking if last x has already been mentioned
            diff = x_list[1:].index(last_x) + 1     # gets diff of index where last x was last seen
            x_list = [str(diff)] + x_list
        except ValueError:                          # if not then assign 0 since first time spoken
            x_list = ['0'] + x_list
    return x_list[0]


def play(data, max_turn) -> int:  # [0 3 6] 0 3 3 1 0 4 0
    data = [int(x) for x in data.split(',')]
    x_dict = {}
    last_x_dict = {}
    last_x = data[-1]
    # print('Data size: {}'.format(max_turn))
    for i in range(max_turn):  # checks values after existing
        if i < len(data):
            x_dict[data[i]] = i
        else:
            try:
                if last_x_dict[last_x] > -1:
                    new_x = x_dict[last_x] - last_x_dict[last_x]
            except KeyError:
                new_x = 0
            try:
                new_x_last_i = x_dict[new_x]
            except KeyError:
                new_x_last_i = i
            last_x_dict[new_x] = new_x_last_i
            x_dict[new_x] = i
            last_x = new_x
    return new_x


data, max_turn = test1, 100000
print('Data size: {}'.format(max_turn))
start = time.time()
x = get_nth(data, max_turn)
print('Pure recursion: {}'.format(x))
xTime = time.time() - start
print(xTime)
print('\n')
start = time.time()
y = play(data, max_turn)
print('Dynamic programming: {}'.format(y))
yTime = time.time() - start
print(yTime)
print('\n')
print('Difference: {}% faster'.format(xTime/yTime * 100))
