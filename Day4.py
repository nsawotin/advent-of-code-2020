import re

path = "./Inputs/day4.txt"
# path = "./Inputs/day4Test.txt"


def part1():
    valid = 0
    requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    with open(path) as file:
        passportFields = []
        for line in file.readlines():
            line = line.rstrip('\n')

            # if line is '', we've finished processing a complete passport, so check if valid
            if not line:
                if set(requiredFields).issubset(passportFields):
                    valid += 1
                passportFields = []
                continue

            fieldValuePairs = [s for s in line.split(' ') if s]

            # process the list to inlude only the included field names
            lineFields = list(map(lambda x: x.split(':')[0], fieldValuePairs))
            lineFields
            passportFields.extend(lineFields)

    # process the last passport
    if set(requiredFields).issubset(passportFields):
        valid += 1

    print("Part 1:")
    print(valid)


def part2():

    valid = 0
    requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    with open(path) as file:
        validPassportFields = []
        for line in file.readlines():
            line = line.rstrip('\n')

            # if line is '', we've finished processing a complete passport, so check if valid
            if not line:
                if set(requiredFields).issubset(validPassportFields):
                    valid += 1
                validPassportFields = []
                continue

            fieldValuePairs = [s for s in line.split(' ') if s]

            # process the list to inlude only the validated field names
            for pair in fieldValuePairs:
                field, value = pair.split(":")
                if validateField(field, value):
                    validPassportFields.append(field)

    # process the last passport
    if set(requiredFields).issubset(validPassportFields):
        valid += 1

    print("Part 2:")
    print(valid)


def validateField(field, value):
    if field == "byr":
        # four digits; at least 1920 and at most 2002.
        valid = int(value) >= 1920 and int(value) <= 2002
        return valid
    elif field == "iyr":
        # four digits; at least 2010 and at most 2020.
        valid = int(value) >= 2010 and int(value) <= 2020
        return valid
    elif field == "eyr":
        # four digits; at least 2020 and at most 2030.
        valid = int(value) >= 2020 and int(value) <= 2030
        return valid
    elif field == "hgt":
        # a number followed by either cm or in
        if "cm" in value:
            # if cm, the number must be at least 150 and at most 193.
            value = value.replace('cm', '')
            valid = int(value) >= 150 and int(value) <= 193
            return valid
        elif "in" in value:
            # if in, the number must be at least 59 and at most 76.
            value = value.replace('in', '')
            valid = int(value) >= 59 and int(value) <= 76
            return valid
        else:
            return False
    elif field == "hcl":
        # must be # symbol followed by exactly six characters 0-9 or a-f
        match = re.match('#[a-f0-9]{6}', value)
        return match
    elif field == "ecl":
        # exactly one of: amb blu brn gry grn hzl oth
        pattern = re.compile('amb|blu|brn|gry|grn|hzl|oth')
        match = pattern.match(value)
        return match
    elif field == "pid":
        # a nine-digit number, including leading zeroes
        match = re.match('^[0-9]{9}$', value)
        return match
    elif field == "cid":
        # always valid
        return True
    else:
        return False


part1()
part2()
