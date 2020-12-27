path = "./Inputs/day8.txt"
# path = "./Inputs/day8Test.txt"


def part1():
    accumulator = 0

    with open(path) as f:
        instructions = [tuple(map(str, i.split(' '))) for i in f]

        i = 0
        while instructions[i][0] != '':
            instruction = instructions[i][0]
            value = int(instructions[i][1])
            instructions[i] = ('',) # clear the ones we've done

            if instruction == "acc":
                accumulator += value
                i += 1
            elif instruction == "jmp":
                i += value
            else:
                i += 1

    print("Part 1:")
    print(accumulator)


def part2():

    print("Part 2:")
    print("TODO")


part1()
part2()
