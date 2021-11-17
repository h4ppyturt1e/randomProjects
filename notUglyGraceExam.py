def assign_colours(message, lower_cols_list, upper_cols_list):
    msg_len = len(message)
    while (len(lower_cols_list) < msg_len):
        lower_cols_list += lower_cols_list
    while (len(upper_cols_list) < msg_len):
        upper_cols_list += upper_cols_list
    
    lower_list = []
    upper_list = []
    space_list = []
    punctuation_list = []
    
    for i, char in enumerate(message):
        if char.isupper():
            upper_list.append((i, char))
        elif char.islower():
            lower_list.append((i, char))
        elif char.isspace():
            space_list.append((i, char))
        else:
            punctuation_list.append((i, char))
    
    temp_result = []
    
    for cur_char, color in zip(lower_list, lower_cols_list):
        i, char = cur_char[0], cur_char[1]
        temp_result.append((i, char, color))
    
    for cur_char, color in zip(upper_list, upper_cols_list):
        i, char = cur_char[0], cur_char[1]
        temp_result.append((i, char, color))
        
    for cur_char in space_list:    
        i, char = cur_char[0], cur_char[1]
        temp_result.append((i, char, "None"))
        
    for cur_char in punctuation_list:
        i, char = cur_char[0], cur_char[1]
        temp_result.append((i, char, "silver"))
    
    temp_result.sort()
    
    final_result = []
    
    for _, char, color in temp_result:
        final_result.append([char, color]) 
    
    return final_result
    
if __name__ == '__main__':
    temp_result = []
    
    ans = [['A', 'yellow'], [' ', 'None'], ['c', 'red'], ['a', 'green'], ['t', 'blue'], [' ', 'None'], ['h', 'red'], ['a', 'green'], ['t', 'blue']]
    print(f"=={ans}==")
    temp_result.append(assign_colours("A cat hat", ['red', 'green', 'blue'], ['yellow'])==ans)
    
    ans = [['H', 'lilac'], ['a', 'lilac'], ['p', 'purple'], ['p', 'pink'], ['y', 'white'], \
        [' ', 'None'], ['b', 'lilac'], ['i', 'purple'], ['r', 'pink'], ['t', 'white'], ['h', 'lilac'], ['d', 'purple'], ['a', 'pink'], ['y', 'white'], ['!', 'Silver']]
    print(f"=={ans}==")
    temp_result.append(assign_colours("Happy birthday!", ['lilac', 'purple', 'pink', 'white'], ['lilac', 'purple', 'pink', 'white'])==ans)
    
    ans = [['C', 'yellow'], ['o', 'blue'], ['n', 'turquoise'], ['g', 'black'], ['r', 'blue'], \
        ['a', 'turquoise'], ['t', 'black'], ['s', 'blue'], [' ', 'None'], ['o', 'turquoise'], ['n', 'black'], [' ', 'None'], ['G', 'yellow'], ['r', 'blue'], ['a', 'turquoise'], ['d', 'black'], ['u', 'blue'], ['a', 'turquoise'], ['t', 'black'], ['i', 'blue'], ['o', 'turquoise'], ['n', 'black'], ['!', 'Silver']]
    print(f"=={ans}==")
    temp_result.append(assign_colours("Congrats on Graduation!", ['blue', 'turquoise', 'black'], ['yellow'])==ans)
    
    ans = [['?', 'Silver'], ['W', 'red'], ['e', 'purple'], [' ', 'None'], ['a', 'black'], \
        ['r', 'purple'], ['e', 'black'], [' ', 'None'], ['h', 'purple'], ['a', 'black'], ['v', 'purple'], ['i', 'black'], ['n', 'purple'], ['g', 'black'], [' ', 'None'], ['t', 'purple'], ['w', 'black'], ['i', 'purple'], ['n', 'black'], ['s', 'purple'], ['?', 'Silver']]
    print(f"=={ans}==")
    temp_result.append(assign_colours("?We are having twins?", ['purple', 'black'], ['red', 'orange', 'yellow', 'green', 'blue'])==ans)    
    
    print()
    print(temp_result)
    print()
    print("Something's wrong..." if any([not x for x in temp_result]) else "Kanpeki da!")
    