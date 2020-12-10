path = "./Inputs/day3.txt"
# path = "./Inputs/day3Test.txt"


def part1():
    trees = 0
    index = 3
    fullTreeGrid = []

    # read input file into a list
    with open(path) as file:
        initialTreeGrid = [list(line.strip()) for line in file]

    # since the "same pattern repeats to the right many times", extend each row to handle this
    for row in initialTreeGrid:
        # get the approximate repeat-length of the pattern
        repeatToRight = int(len(initialTreeGrid) / int(len(row)/index))
        if(repeatToRight > 0):
            row = row * repeatToRight
        fullTreeGrid.append(row)

    # count the trees
    for row in fullTreeGrid[1:]:  # the [1:] skips the first row
        if(row[index] == '#'):
            trees += 1

        index += 3

    print("Part 1:")
    print(trees)


def part2():
    # read input file into a list
    with open(path) as file:
        initialTreeGrid = [list(line.strip()) for line in file]

    answer = countTrees(initialTreeGrid, 3, 1) * countTrees(initialTreeGrid, 1, 1) * countTrees(
        initialTreeGrid, 5, 1) * countTrees(initialTreeGrid, 7, 1) * countTrees(initialTreeGrid, 1, 2)

    print("Part 2:")
    print(answer)


def countTrees(initialTreeGrid, right, down):
    trees = 0
    right1 = right
    down1 = down
    fullTreeGrid = []

    # since the "same pattern repeats to the right many times", extend each row to handle this
    for row in initialTreeGrid:
        # get the approximate repeat-length of the pattern
        # add 1 to account for rounding
        repeatToRight = int(len(initialTreeGrid) / int(len(row)/right1)) + 1

        if(repeatToRight > 0):
            row = row * repeatToRight
        fullTreeGrid.append(row)

    # count the trees
    for idx, row in enumerate(fullTreeGrid):
        if(idx == down):
            if(row[right] == '#'):
                trees += 1

            right += right1
            down += down1

    return trees


part1()
part2()
