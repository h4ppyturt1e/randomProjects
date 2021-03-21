import time

lonumbers = []
f = open('day1.txt', 'r')
for line in f:
    line = int(line.rstrip())
    lonumbers.append(line)

f.close()


def bla():
    start_time = time.time()
    for num in lonumbers:
        for num2 in lonumbers:
            for num3 in lonumbers:
                if num + num2 + num3 == 2020:
                    print(num, num2, num3)
                    print(num * num2 * num3)
                    print((time.time() - start_time, 'seconds'))
                    return "YES"

bla()