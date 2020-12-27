path = "./Inputs/day7.txt"
# path = "./Inputs/day7Test.txt"
# path = "./Inputs/day7Test2.txt"
# path = "./Inputs/day7Test3.txt"

allBagsPt1 = {}
allBagsPt2 = {}


def part1():
    count = 0

    with open(path) as file:
        # build a dictionary to hold all values; key = outer bag, value = list of inner bags
        for line in file.readlines():
            line = line.rstrip('s.\n')

            # massage the string to get each colored bag mentioned
            splits = line.split('bag')  # split line on word 'bag'
            splits = list(map(str.strip, splits))
            splits = list(filter(None, splits))

            allBagsPt1[splits[0]] = []  # add the dict key (outer bag)

            # add inner bags as dict values
            for bag in splits[1:]:  # skip first which was the key
                bagColor = bag.split()[-2:]  # inner bag color is last 2 words
                name = " ".join(map(str, bagColor))
                allBagsPt1[splits[0]].append(name)

        for mainBag in allBagsPt1:
            if containsBag(mainBag):
                count += 1

    print("Part 1:")
    print(count)


def part2():
    count = 0

    with open(path) as file:

        # build a dictionary to hold all values; key = outer bag, value = list of inner bags
        for line in file.readlines():
            line = line.rstrip('s.\n')

            # massage the string to get each colored bag mentioned
            splits = line.split('bag')  # split line on word 'bag'
            splits = list(map(str.strip, splits))
            splits = list(filter(None, splits))

            allBagsPt2[splits[0]] = []  # add the dict key (outer bag)

            # add inner bags as dict values
            for bag in splits[1:]:  # skip first which was the key
                bagColor = bag.split()[-3:]  # amount + color = last 3 words
                name = " ".join(map(str, bagColor))
                allBagsPt2[splits[0]].append(name)

        count = countBags('shiny gold')

        print("Part 2:")
        print(count)


# Part1
# checks bags until a 'shiny gold' bag is found
def containsBag(bag):
    if 'shiny gold' in allBagsPt1[bag]:
        return True
    else:
        for childBag in allBagsPt1[bag]:
            if childBag != 'no other':
                found = containsBag(childBag)
                if found:
                    return True

# Part2
# counts bags within passed bag
def countBags(bag):
    if 'no' in allBagsPt2[bag][0]:
        return 0

    # child bag count
    count = 0

    for childBag in allBagsPt2[bag]:
        numBags = int(childBag.split(' ', 1)[0])
        color = " ".join(map(str, childBag.split()[-2:]))
        count += numBags + (numBags * countBags(color))

    return count


part1()
part2()
