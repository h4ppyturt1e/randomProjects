from typing import Tuple
from itertools import combinations
"""
Shoppee Code League Programming question - Divisors
4 2
1 3 2 4
N engineers arranged in tables

K groups

dividers between groups

noise(l,r) is noise value of workers l to r

Ai is singular worker noise

Prints out minimum noise level possible
"""

first = [int(x) for x in input().split()]
n, dividers = first[0], first[1]-1

engineers = [int(x) for x in input().split()]

# print(n, dividers)
# print(engineers)


indexList = [i for i in range(n) if i != 0]
seenIndexList = []


def getDivisionIndexList(iList, k):
    divList = [list(x) for x in list(combinations(iList, k))]
    for i in range(len(divList)):
        for j in range(len(divList[i])):
            divList[i][j] += j
    return divList


divisionIndexList = getDivisionIndexList(indexList, dividers)
# print(divisionIndexList)


possibleDivisions = []
for divisors in divisionIndexList:
    tempList = [x for x in engineers]
    # print(divisors)
    for i in divisors:
        tempList.insert(i, -1)
    possibleDivisions.append(tempList)

# print(possibleDivisions)

omegaGroupList = []
groupList = []
for divisions in possibleDivisions:
    curDiv = [x for x in divisions]
    group = []
    i = 0
    while len(groupList) != dividers + 1:
        if i < len(curDiv) and curDiv[i] != -1:
            group.append(curDiv[i])
            i += 1
        elif -1 in curDiv:
            curDiv.remove(-1)
            groupList.append(group)
            group = []
        else:
            groupList.append(group)
            group = []
    omegaGroupList.append(groupList)
    groupList = []

# print(omegaGroupList)


noiseFactorList = []

for grouping in omegaGroupList:
    total = 0
    for branch in grouping:
        total += len(branch) * sum(branch)
    noiseFactorList.append(total)

# print(noiseFactorList)

print(min(noiseFactorList))

