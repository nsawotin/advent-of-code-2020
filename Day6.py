path = "./Inputs/day6.txt"
# path = "./Inputs/day6Test.txt"


def part1():
    count = 0
    anyoneYes = []

    with open(path) as file:
        for line in file.readlines():
            line = line.rstrip('\n')

            if line:
                anyoneYes.extend(list(line))
            else:
                # end of group
                count += len(set(anyoneYes))  # set only stores unique values
                anyoneYes = []

    # do last group
    count += len(set(anyoneYes))

    print("Part 1:")
    print(count)


def part2():
    count = 0
    everyoneYes = []
    startGroup = True

    with open(path) as file:
        for line in file.readlines():
            line = line.rstrip('\n')

            if line and startGroup == True:
                # process first person in group
                everyoneYes.extend(list(line))
                startGroup = False
            elif line:
                # remove any from everyoneYes that weren't yes for next person
                for p in set(everyoneYes) - set(list(line)):
                    everyoneYes.remove(p)
                    continue
            else:
                # end of group
                count += len(set(everyoneYes))
                everyoneYes = []
                startGroup = True

    # do last group
    count += len(set(everyoneYes))

    print("Part 2:")
    print(count)


part1()
part2()
