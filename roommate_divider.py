
with open("roommate_shared_bill.txt") as f:
    data = [x.strip().split(" - ") for x in f.readlines()]
    
    names = {}
    
    curPerson = ""
    for line in data:
        if len(line) == 1:
            curPerson = line[0]
            names[curPerson] = []
        else:
            names[curPerson].append(line)
    
    print(names)
    print()
    
    nameDebt = {}
    
    curTotal = 0
    for person in names:
        print(person)
        for item in names[person]:
            print(item)
            curTotal += float(item[1])
        
        print()
        print(f"Total for {person}: {curTotal:.2f}")
        print()
        
        nameDebt[person] = curTotal
        curTotal = 0
    
    total = 0
    for person in nameDebt:
        total += nameDebt[person]
    average = total / len(nameDebt)
    
    for person in nameDebt:
        nameDebt[person] -= average
        if nameDebt[person] < 0:
            print(f"{person} owes ${abs(nameDebt[person]):.2f}")   
    