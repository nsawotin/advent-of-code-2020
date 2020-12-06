path = "./Inputs/day1.txt"
# path = "./Inputs/day1Test.txt";


def part1():
    file = open(path, "r")
    lines = file.readlines()

    i = j = 0
    found = False
    while i < len(lines) and not found:
        num1 = int(lines[i])

        while j < len(lines) and not found:
            num2 = int(lines[j])
            if num1 + num2 == 2020:
                print("Part 1:")
                print(num1*num2)
                found = True
            j += 1

        i += 1
        j = 0

    file.close()


def part2():
    file = open(path, "r")
    lines = file.readlines()

    i = j = k = 0
    found = False
    while i < len(lines) and not found:
        num1 = int(lines[i])

        while j < len(lines) and not found:
            num2 = int(lines[j])

            while k < len(lines) and not found:
                num3 = int(lines[k])

                if num1 + num2 + num3 == 2020:
                    print("Part 2:")
                    print(num1*num2*num3)
                    found = True
                k += 1
            j += 1
            k = 0
        i += 1
        j = 0

    file.close()


part1()
part2()
