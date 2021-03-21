import time
startTime = time.time()

test = 'day18test.txt'
real = 'day18.txt'
val = 'day18val.txt'


def parse(line):
    brackets = ["(", ")"]
    result = []
    anotherList = []
    count = 0
    for char in line:
        if char not in brackets:
            if count == 0:
                result.append(char)
            else:
                anotherList.append(char)
        elif char == "(":
            count += 1
            if count > 1:
                anotherList.append(char)
        elif char == ")":
            if count > 1:
                anotherList.append(char)
            count -= 1
            if anotherList != [] and count == 0:
                result.append(parse(anotherList))
                anotherList = []

    # print(result)
    return result


def solve(parsedList) -> int:
    result = 0
    op = "+"
    for x in parsedList:
        if isinstance(x, list):
            result = eval(str(result) + op + str(solve(x)))
        elif x.isdigit():
            result = eval(str(result) + op + x)
        elif not x.isdigit():
            op = x
    # print(result)
    return result


def solveB(parsedList):
    result, temp = [], []
    for e in parsedList:
        if e != "*":
            if len(e) > 1:
                temp.append(solveB(e))
            else:
                temp.append(e)
        elif e == "*":
            if len(temp) == 1:
                result.append(temp[0])
            else:
                result.append(temp)
            temp = []
            result.append("*")
    if len(temp) == 1:
        result.append(temp[0])
    else:
        result.append(temp)
    return str(solve(result))


with open(val) as file:
    data = [line.rstrip() for line in file.readlines()]
    data = [[char for char in line if char != ' '] for line in data]
    data = [(parse(line)) for line in data]
    # print(data)
    totalA = sum([solve(line) for line in data])
    totalB = sum([int(solveB(line)) for line in data])


print(totalA)
print(totalB)
print(str(time.time()-startTime) + "seconds")
