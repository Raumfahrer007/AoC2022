def partOne(lines):
    dirLevel = -1
    dirSizes = list()
    totalSum = 0
    i = 0
    while i < len(lines):
        if lines[i].startswith("$ cd .."):
            if dirSizes[dirLevel] <= 100000:
                totalSum += dirSizes[dirLevel]
            if not dirLevel == 0:
                dirSizes[dirLevel - 1] += dirSizes[dirLevel]
            del(dirSizes[dirLevel])
            dirLevel -= 1
        elif lines[i].startswith("$ cd"):
            dirLevel += 1
            dirSizes.append(0)
        else:
            if lines[i][0].isdigit():
                valueLine = lines[i].split()
                dirSizes[dirLevel] += int(valueLine[0])
        i += 1
    print(f"DirLevel: {dirLevel}")
    print(dirSizes)
    for index in reversed(range(len(dirSizes))):
        if index > 0:
            dirSizes[index - 1] += dirSizes[index]
    availableSpace = 70000000 - dirSizes[0]
    print(f"Available Space: {availableSpace}")
    spaceToClear = 30000000 - availableSpace
    print(f"Space to Clear: {spaceToClear}")
    print(totalSum)


def partTwo(lines):
    dirLevel = -1
    delDir = list()
    dirSizes = list()
    i = 0
    while i < len(lines):
        if lines[i].startswith("$ cd .."):
            if dirSizes[dirLevel] >= 2677139:
                delDir.append(dirSizes[dirLevel])
            if not dirLevel == 0:
                dirSizes[dirLevel - 1] += dirSizes[dirLevel]
            del(dirSizes[dirLevel])
            dirLevel -= 1
        elif lines[i].startswith("$ cd"):
            dirLevel += 1
            dirSizes.append(0)
        else:
            if lines[i][0].isdigit():
                valueLine = lines[i].split()
                dirSizes[dirLevel] += int(valueLine[0])
        i += 1
    print(min(delDir))
            


data = open("day07Input.txt", "r")
lines = data.readlines()
data.close()

partOne(lines)
partTwo(lines)