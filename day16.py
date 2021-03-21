import time
start = time.time()
real = 'day16.txt'
testa = 'day16testa.txt'
testb = 'day16testb.txt'

with open(real) as file:
    rulesList = []
    nearbyTickets = []
    [rulesList.append((x.rstrip().split(': ')[0], x.rstrip().split(': ')[1].split(' or '))) if ': ' in x
     else nearbyTickets.append(x.rstrip().split(',')) for x in file.readlines() if x != '\n']
    rulesList = {rule[0]: rule[1] for rule in rulesList}
    myTicket, nearbyTickets = ([list(map(int, x)) if x[0].isdigit() else x for x in nearbyTickets][1:2].pop(0),
                               [list(map(int, x)) if x[0].isdigit() else x for x in nearbyTickets][3:])

ruleDict = {rule: [num for ruleRange in [tuple(map(int, numRange.split('-'))) for numRange in rulesList[rule]] for num
                   in range(ruleRange[0], ruleRange[1]+1)] for rule in rulesList}

validNums = list(set(sum([ruleDict[rule] for rule in ruleDict], [])))
sumA = sum([num for ticket in nearbyTickets for num in ticket if num not in validNums])

sievedTickets = [[ticket[i] if ticket[i] in validNums else -1 for i in range(len(ticket))] for ticket in nearbyTickets]

columnList = [[ticket[i] for ticket in sievedTickets] for i in range(len(ruleDict))]

columnRuleList = {i: [] for i in range(len(columnList))}
for i in range(len(columnList)):
    for rule in ruleDict:
        validNums = ruleDict[rule]
        if not any([False if x in validNums else True for x in [n for n in columnList[i] if n != -1]]):
            columnRuleList[i] += [rule]

seen = []
seenDict = {i: [] for i in range(len(ruleDict))}
while len(seen) != len(ruleDict):
    for i in columnRuleList:
        if len(columnRuleList[i]) == 1 and columnRuleList[i][0] not in seen:
            appended = ''.join(columnRuleList[i])
            seen.append(appended)
            seenDict[i] = appended
        else:
            for j in range(len(columnRuleList[i])):
                try:
                    if columnRuleList[i][j] in seen:
                        columnRuleList[i].pop(j)
                except IndexError:
                    pass

reversedSeenDict = {seenDict[i]: i for i in seenDict}
departureIndexList = [reversedSeenDict[rule] for rule in [x for x in reversedSeenDict if 'departure' in x]]

totalB = 1
for i in departureIndexList:
    totalB *= myTicket[i]

# print('rulesList:', rulesList)
# print('ruleDict:', ruleDict)
# print('sievedTickets:', sievedTickets)
# print('columnList:', columnList)
# print('columnRuleList:', columnRuleList)
# print('myTicket:', myTicket)
# print('seenDict:', seenDict)
# print('departureIndexList', departureIndexList)
totA = time.time() - start
print('Part(a): {}\nPart(b): {}\nFinished in {} secs'.format(sumA, totalB, totA))

