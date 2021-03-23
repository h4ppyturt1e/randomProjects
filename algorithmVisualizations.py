from typing import List


# Ryan Nicholas Permana, #V00959956

"""
Part 1: a Simple Algorithm

a1 and a2 - array of 6 integers each
i - variable for iteration
comp - variable for comparing two integers
count - variable that keeps track of instances of a1[i] > a2[i]
"""


def simpleAlgorithm(a1, a2) -> int:
    i = 0
    count = 0
    while i < 6:
        input()
        print("Current i: " + str(i))
        print("Current a1: {}\n"
              "Current a2: {}\n".format(a1[i], a2[i]))
        input("Is {} larger than {}?\n"
              "============================".format(a1[i], a2[i]))
        comp = a1[i] - a2[i]
        if comp > 0:
            count = count + 1
            print("Yep!, A1 > A2")
            print("Count is now: " + str(count))
        else:
            print("Nope!")
            print("Count remains as: " + str(count))
        print("============================")

        i = i + 1

    return count


"""
Part 2: Sorting algorithms (Selection sort)
"""


def selectionSort(resultArray, checkedArray) -> List[int]:
    print("=======================================")
    print("resultArray: {}\n"
          "checkedArray: {}\n".format(resultArray, checkedArray))
    input("Is the checkedArray empty?\n"
          "If not, what is the minimum value?\n"
          "=======================================")

    if checkedArray == []:
        print("Since the checkedArray is empty,\n"
              "we know that the algorithm has\n"
              "finished sorting.")
        return resultArray
    else:
        minValue = checkedArray[0]
        for num in checkedArray:
            if num < minValue:
                minValue = num

        print("Minimum value in checkedArray is: " + str(minValue))
        input("Moved minimum value to resultArray.")
        checkedArray.remove(minValue)
        resultArray.append(minValue)
        # print("=======================================")
        return selectionSort(resultArray, checkedArray)


def main():
    first = [9, 9, 0, 7, 1, 3]
    second = [9, 5, 9, 9, 5, 6]
    input("Simple algorithm visualisation:\n")
    print("Here are the arrays:")
    print("============================")
    print("Array a1: {}".format(first))
    print("Array a2: {}".format(second))
    print("============================")

    input("Number of occurrences where\n"
          "A1 > A2 is {}.\n"
          "============================".format(simpleAlgorithm(first, second)))

    givenArray = [20, 4, 3, 9, 10, 2, 49, 4]
    input("Selection sort algorithm visualisation:")
    print("=======================================\n"
          "Sorted array: {}\n"
          "=======================================".format(selectionSort([], givenArray)))


if __name__ == '__main__':
    main()
