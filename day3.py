def partOne(lines):
    totalSum = 0
    for line in lines:
        firstComp = set()
        secondComp = set()
        for i in range(len(line) // 2):
            firstComp.add(line[i])
        for i in range(len(line) // 2, len(line)):
            secondComp.add(line[i])

        for item in firstComp:
            if secondComp.__contains__(item):
                totalSum += ord(item) - 96 if item.islower() else ord(item) - 38
    print(totalSum)


def partTwo(lines):
    totalSum = 0
    for i in range(0, len(lines), 3):
        firstElf = set(lines[i])
        firstElf.remove("\n")
        secondElf = set(lines[i + 1])
        secondElf.remove("\n")
        thirdElf = set(lines[i + 2])
        thirdElf.remove("\n")

        for item in firstElf:
            if secondElf.__contains__(item) and thirdElf.__contains__(item):
                totalSum += ord(item) - 96 if item.islower() else ord(item) - 38
    
    print(totalSum)





data = open("day3Input.txt", "r")
lines = data.readlines()
data.close()


linesTest = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw"
]

print(f"a: {ord('a')}") # 96
print(f"z: {ord('z')}")
print(f"A: {ord('A')}") # 38
print(f"Z: {ord('Z')}")

#partOne(lines)
partTwo(lines)