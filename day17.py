import time
from typing import Tuple, List
startTime = time.time()

test = 'day17test.txt'
real = 'day17.txt'

Position = Tuple[int, int, int]  # (x, y, z)

with open(real) as file:
    data = [[[c for c in cc] for cc in line.rstrip()] for line in file.readlines()]
    print(data)
dirList = [(x, y, z, w) for x in [-1, 0, 1] for y in [-1, 0, 1] for z in [-1, 0, 1] for w in [-1, 0, 1]
           if (x, y, z, w) != (0, 0, 0, 0)]
# print(dirList)


def check_around(x, y, z, w, setupData: List[List[str]]) -> int:
    count = 0
    for direc in dirList:
        dx, dy, dz, dw = x + direc[0], y + direc[1], z + direc[2], w + direc[3]
        try:
            if setupData[dx][dy][dz][dw] == '#':
                count += 1
        except IndexError:
            pass
    return count


def setup(startData) -> List[List[str]]:
    lengthW = len(startData)
    for i in range(lengthW):
        lengthX = len(startData[i])
        for j in range(lengthX):
            lengthY = len(startData[i][j])
            for k in range(lengthY):
                startData[i][j][k] = '.' + startData[i][j][k] + '.'

    lengthX = [len(startData[0][0][0]) * '.']
    for i in range(lengthW):
        for j in range(len(startData[i])):
            startData[i][j] = lengthX + startData[i][j] + lengthX

    lengthY = [[len(startData[0][0]) * '.' for x in range(len(startData[0][0]))]]
    for i in range(lengthW):
        startData[i] = lengthY + startData[i] + lengthY

    lengthZ = [lengthY * len(startData[0])]
    startData = lengthZ + startData + lengthZ
    # print('setup:\n', startData)
    return startData


def transform(startData) -> List[List[List[str]]]:
    setupData = setup(startData)
    xRange, yRange, zRange, wRange = len(setupData), len(setupData[0]), len(setupData[0][0]), len(setupData[0][0][0])
    # print(xRange, yRange, zRange, wRange)
    endData = [[['.' * wRange for z in range(zRange)] for y in range(yRange)] for x in range(xRange)]
    # print('temp:\n', endData)
    for x in range(xRange):
        for y in range(yRange):
            for z in range(zRange):
                tempList = list(setupData[x][y][z])
                for w in range(wRange):
                    # print('xyzw:', x, y, z, w)
                    count = check_around(x, y, z, w, setupData)
                    char = tempList[w]
                    if char == '#' and count not in [2, 3]:
                        tempList[w] = '.'
                    elif char == '.' and count == 3:
                        tempList[w] = '#'
                    # else:
                    #     tempList[z] = 'x'
                    # print(tempList)
                endData[x][y][z] = ''.join(tempList)
                # print(endData)
                # print('\n')

    print('endData:\n', endData)
    return endData


def solveA(startData, maxCycles) -> int:
    cycle = 0
    count = 0
    while cycle < maxCycles:
        if cycle == 0:
            data = transform(startData)
        else:
            data = transform(data)
        cycle += 1
    for x in range(len(data)):
        for y in range(len(data[x])):
            for z in range(len(data[x][y])):
                count += data[x][y][z].count('#')
    return count


# testData = setup(data)
# transform(data)
print('Part (a): {}'.format(solveA(data, 6)))
totalTime = 'Finished in {} secs.'.format(time.time() - startTime)
print(totalTime)
