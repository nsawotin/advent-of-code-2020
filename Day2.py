path = "./Inputs/day2.txt"
#path = "./Inputs/day2Test.txt"


def part1():
    file = open(path, "r")
    lines = file.readlines()
    count = 0

    for line in lines:
        parts = line.split(" ")
        min, max = map(int, parts[0].split("-"))
        letter = parts[1].replace(':', '')
        password = parts[2]

        occurences = password.count(letter)
        if(occurences >= min and occurences <= max):
            count += 1

    print("Part 1:")
    print(count)

    file.close()

def part2():
    file = open(path, "r")
    lines = file.readlines()
    count = 0

    for line in lines:
        parts = line.split(" ")
        char1, char2 = map(int, parts[0].split("-"))
        letter = parts[1].replace(':', '')
        password = parts[2]

        if(password[char1-1] == letter) is not (password[char2-1] == letter):
            count += 1

    print("Part 2:")
    print(count)

    file.close()

part1()
part2()
