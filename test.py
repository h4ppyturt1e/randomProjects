words = ['about', 'after', 'again', 'below', 'could', 'every', 'first', 'found', 'great', 'house', 'large', 'learn',
         'never', 'other', 'place', 'plant', 'point', 'right', 'small', 'sound', 'spell', 'still', 'study', 'their',
         'there', 'these', 'thing', 'think', 'three', 'water', 'where', 'which', 'world', 'would', 'write']

tuple_list = []
for i in range(5):
    for j in range(5):
        l = [word[i] + word[j] for word in words]
        s = set(l)
        diff = len(l) - len(s)
        tuple_list.append((diff, i+1, j+1))

tuple_list.sort()

[print(item) for item in tuple_list]
print("\nBest combination:\n====================")
print(tuple_list[0])


