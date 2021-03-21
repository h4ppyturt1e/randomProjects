
# length of each line -> 31
# number of lines -> 323

# Right 1, down 1. -> 63
# Right 3, down 1. -> 181
# Right 5, down 1. -> 55
# Right 7, down 1. -> 67
# Right 1, down 2. -> 31

locommands = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
RIGHT = 0
DOWN = 1
def tree_checker(file_name: str) -> int:
    print(file_name)
    product = 1
    for command in locommands:
        print(command)
        move_right = command[RIGHT]
        move_down = command[DOWN]
        index = 0
        count = 0
        f = open(file_name, 'r')
        len_check = f.readline().rstrip()
        length = len(len_check)
        for line in f:
            if move_down > 1:
                for down in range(move_down-1):
                    line = f.readline()
            line = line.rstrip()
            index += move_right
            # print(index)
            if index >= length:
                modulo_index = index % length
            else:
                modulo_index = index
            if line[modulo_index] == "#":
                count += 1
        print('trees hit:', count)
        product *= count
        f.close()
    print('product:', product)
    return product

tree_checker('day3test.txt')
print('\n')
tree_checker('day3.txt')
