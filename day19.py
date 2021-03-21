import numpy


real = "day19.txt"

with open(real) as f:
    data = [line.rstrip() for line in f.readlines()]
    rules, messages = data[:data.index("")], data[data.index(""):]
    [print(x) for x in rules]
    [print(x) for x in messages]