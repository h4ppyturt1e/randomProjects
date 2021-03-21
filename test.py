from typing import List


def getInput(f) -> (List[List[int]]):
    first = [int(x) for x in f.readline().rstrip().split()]
    days, cells = first[0], first[1]
    plantArrayList = []
    for x in range(days):
        plants = [int(x) for x in f.readline().rstrip().split()]
        plantArrayList.append(plants)
    return plantArrayList


def main():
    f = open('test.txt')

    attempts = int(f.readline().rstrip())
    health = 0
    loTests = []
    for x in range(attempts):
        loTests.append(getInput(f))
    [print(test) for test in loTests]

    f.close()


main()
