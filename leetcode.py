class DinnerPlates:

    def __init__(self, capacity: int):
        self.maxCap = capacity
        self.stacks = []
        self.unfilledLeftmost = [0]

    def probeNextEmptyStack(self) -> None:
        for i in range(self.unfilledLeftmost[0], len(self.stacks)):
            if len(self.stacks[i]) < self.maxCap:
                self.unfilledLeftmost[0] = i
                return
        self.unfilledLeftmost[0] = len(self.stacks)
        self.stacks.append([])

    def push(self, val: int) -> None:
        # print("PUSHING:", val)
        if self.maxCap == 1:
            if self.unfilledLeftmost[0] >= len(self.stacks):
                self.stacks.append(val)
            else:
                if self.stacks[self.unfilledLeftmost[0]] == None:
                    self.stacks[self.unfilledLeftmost[0]] = val
                    if len(self.unfilledLeftmost) > 1:
                        self.unfilledLeftmost = self.unfilledLeftmost[1:]
                    else:
                        self.unfilledLeftmost[0] += 1
            self.unfilledLeftmost[0] += 1
        else:
            if self.stacks == []:
                self.stacks.append([val])

            else:
                if len(self.unfilledLeftmost) <= 1 or self.unfilledLeftmost[0] >= len(self.stacks):
                    self.stacks.append([])
                
                if len(self.stacks[self.unfilledLeftmost[0]]) < self.maxCap:
                    self.stacks[self.unfilledLeftmost[0]].append(val)
                    if len(self.stacks[self.unfilledLeftmost[0]]) == self.maxCap:
                        if len(self.unfilledLeftmost) > 1:
                            self.unfilledLeftmost = self.unfilledLeftmost[1:]
                        else:
                            self.unfilledLeftmost[0] += 1

                else:  # stack full, find next stack
                    if len(self.unfilledLeftmost) > 1:
                        self.unfilledLeftmost = self.unfilledLeftmost[1:]
                    else:
                        self.unfilledLeftmost[0] += 1
                    self.stacks[self.unfilledLeftmost[0]].append(val)
            # print(self.stacks)

    def pop(self) -> int:
        if self.maxCap == 1:
            if self.stacks == []:
                return -1
            if self.unfilledLeftmost[0] != 0:
                self.unfilledLeftmost[0] -= 1
            removed = self.stacks.pop()
            self.cleanEmptyStacks()
            return removed
        else:
            for i in range(len(self.stacks)-1, -1, -1):
                if len(self.stacks[i]) > 0:
                    removed = self.remove(i)
                    self.cleanEmptyStacks()
                    if self.unfilledLeftmost[0] != 0:
                        self.unfilledLeftmost[0] -= 1
                    return removed

            # print(self.stacks)
            return -1

    def popAtStack(self, index: int) -> int:
        if self.maxCap == 1:
            if index >= len(self.stacks):
                return -1

            removed = self.stacks[index]
            self.stacks[index] = None
            self.unfilledLeftmost.append(index)
            self.unfilledLeftmost.sort()
        else:
            if self.unfilledLeftmost[0] > index:
                self.unfilledLeftmost.append(index)
                self.unfilledLeftmost.sort()
            if index >= len(self.stacks) or self.stacks[index] == []:
                # print(self.stacks)
                return -1

            removed = self.remove(index)
        if index == (len(self.stacks) - 1):
            # print(index, len(self.stacks)-1)
            self.cleanEmptyStacks()
        return removed

    def cleanEmptyStacks(self) -> None:
        n = 0
        for i in range(len(self.stacks)-1, -1, -1):
            if self.stacks[i] == [] or self.stacks[i] == None:
                n += 1
            else:
                break
        if n > 0:
            self.stacks = self.stacks[:-n]
        # print(self.stacks)

    def remove(self, index) -> int:
        # print(self.stacks)
        removed = self.stacks[index][-1]
        # print(f"REMOVED: {removed}")
        self.stacks[index] = self.stacks[index][:-1]
        # print(self.stacks)
        return removed

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)


# testList = (["DinnerPlates", "push", "push", "popAtStack", "pop", "push", "push", "pop", "pop"],
#             [[1], [1], [2], [1], [], [1], [2], [], []])

testList = (["DinnerPlates", "push", "push", "push", "push", "push", "popAtStack", "push", "push", "popAtStack", "popAtStack", "pop", "pop", "pop", "pop", "pop"],
            [[2], [1], [2], [3], [4], [5], [0], [20], [21], [0], [2], [], [], [], [], []])

testList = (["DinnerPlates","push","push","push","push","push","push","push","push","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","push","push","push","push","push","push","push","push","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop"],
[[2],[472],[106],[497],[498],[73],[115],[437],[461],[3],[3],[1],[3],[0],[2],[2],[1],[1],[3],[197],[239],[129],[449],[460],[240],[386],[343],[],[],[],[],[],[],[],[],[],[]])

# testList = (["DinnerPlates", "push", "push", "push", "push", "push", "push", "push", "push", "popAtStack", "popAtStack", "popAtStack", "popAtStack", "push", "push", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"],
#             [[2], [471], [177], [1], [29], [333], [154], [130], [333], [1], [0], [2], [0], [165], [383], [267], [367], [53], [373], [388], [249], [], [], [], []])

# testList = (["DinnerPlates", "push", "push", "push", "popAtStack", "push", "pop", "pop", "pop", "pop"],
#             [[1], [1], [2], [0], [0], [7], [], [], [], []])

# testList = (["DinnerPlates","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","popAtStack","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","popAtStack","push","push","push","push","push","push","push","popAtStack","push","push","push","push","push","push","push","push","popAtStack","push","push","push","push","push","push","push","push","push","push","push","push","push","popAtStack","push","push","push","push","popAtStack","push","push","push","push","push","push","push","push","push","push","push","push","push","popAtStack","push","push","push","push","push","popAtStack","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","popAtStack","push","popAtStack","push","push","push","push","push","push","popAtStack","push","push","popAtStack","push","push","popAtStack","push","popAtStack","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","popAtStack","push","push","push","push","push","push","push","push","push","push","push","push","push","popAtStack","push","push","popAtStack","push","push","push","push","push","push","push","push","push","push","push","push","push","push","popAtStack","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","popAtStack","push","push","push","popAtStack"],
#             [[1], [3333], [6171], [2289], [5635], [7054], [5338], [2466], [2642], [5612], [8830], [6311], [2733], [8866], [9379], [158], [4218], [6375], [6554], [6214], [8452], [4982], [1525], [5926], [8457], [3039], [7854], [2295], [795], [2341], [3376], [8662], [6847], [6702], [1948], [4755], [1186], [4231], [4598], [6436], [2735], [1325], [7318], [8866], [647], [9148], [2463], [6951], [9896], [7692], [4276], [945], [843], [2390], [7955], [2524], [7761], [4321], [6975], [4543], [2750], [6775], [1038], [1335], [908], [5876], [1594], [7822], [2624], [597], [4863], [1771], [2361], [5258], [7382], [2364], [891], [37], [7485], [1241], [2921], [8632], [1617], [1959], [6382], [7265], [4459], [2599], [719], [4801], [4574], [5873], [3711], [3908], [3424], [633], [2394], [6438], [7287], [1565], [8819], [7506], [2220], [9838], [9895], [713], [2802], [7265], [4966], [8552], [2154], [4725], [520], [5003], [7070], [4365], [52], [8565], [62], [2969], [4709], [8728], [9529], [5332], [8108], [1436], [1665], [1251], [6642], [906], [8478], [3451], [4911], [1175], [3030], [8093], [1259], [2189], [3360], [8398], [7734], [7181], [8760], [9679], [6567], [482], [9913], [9338], [9573], [804], [9015], [8877], [3095], [8221], [9910], [7269], [9053], [5310], [3360], [2008], [1983], [4101], [509], [4474], [6315], [4650], [2627], [8068], [9534], [3212], [1180], [8063], [996], [6337], [8941], [3721], [747], [5167], [3151], [9316], [8642], [3895], [6215], [5343], [8355], [2367], [4413], [6495], [3892], [1125], [3720], [9062], [2777], [4620], [6922], [7139], [4327], [6925], [6778], [3648], [719], [1564], [3754], [8904], [4438], [6744], [778], [6300], [9134], [1687], [8637], [8963], [2786], [1292], [1688], [997], [1708], [824], [9715], [6150], [9454], [2551], [831], [769], [9646], [423], [5131], [6880], [2742], [9735], [9535], [127]])

# testList = (["DinnerPlates", "push", "push", "push", "popAtStack", "pop", "pop"],
#             [[1], [1], [2], [3], [1], [], []])

test = zip(testList[0], testList[1])

result = []
for op, val in test:
    print()
    if op == "DinnerPlates":
        D = DinnerPlates(val[0])
        print(f"maxCap: {val[0]}")
    elif op == "push":
        print(f"PUSH: {val}")
        D.push(val[0])
        result.append(None)
    elif op == "pop":
        print(f"POP: {val}")
        result.append(D.pop())
    elif op == "popAtStack":
        print(f"POP AT STACK: {val}")
        result.append(D.popAtStack(val[0]))
    print(f"unfilledLeftmost: {D.unfilledLeftmost}")
    print(D.stacks)


print(result)
