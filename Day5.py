path = "./Inputs/day5.txt"
# path = "./Inputs/day5Test.txt"


def part1():

    seats = getSeats()
    highestSeat = max(seats)

    print("Part 1:")
    print(highestSeat)


def part2():

    seats = getSeats()
    # get the missing seat
    difference = sorted(set(range(seats[0], seats[-1] + 1)).difference(seats))

    print("Part 2:")
    print(difference[0])


def getSeats():
    seats = []

    with open(path) as file:
        for line in file.readlines():
            rows = list(range(128))
            cols = list(range(8))
            letters = list(line.rstrip('\n'))

            for letter in letters:
                if(letter == 'F' or letter == 'B'):
                    rows = splitList(rows, letter)
                elif(letter == 'L' or letter == 'R'):
                    cols = splitList(cols, letter)

            row = rows[0]
            col = cols[0]
            seat = row * 8 + col
            seats.append(seat)

    return seats


def splitList(origList, part):
    if (part == 'F' or part == 'L'):
        # take first half
        new_list = origList[:len(origList)//2]
    else:
        # take second half
        new_list = origList[len(origList)//2:]

    return new_list


part1()
part2()
