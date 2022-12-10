def partOne(lines):
    totalSum = 0
    for line in lines:
        pair = line.split(",")
        elfOne = pair[0].split("-")
        elfOneIDs = list(range(int(elfOne[0]), int(elfOne[1]) + 1))
        elfTwo = pair[1].split("-")
        elfTwoIDs = list(range(int(elfTwo[0]), int(elfTwo[1]) + 1))

        totalSum += compareLists(elfOneIDs, elfTwoIDs)
    
    print(totalSum)

def compareLists(list1: list, list2: list):
    list1BE = [list1[0], list1[len(list1) - 1]]
    list2BE = [list2[0], list2[len(list2) - 1]]
    if list2.__contains__(list1BE[0]) or list2.__contains__(list1BE[1]):   # "and" for partOne
        return 1
    elif list1.__contains__(list2BE[0]) or list1.__contains__(list2BE[1]): # "and" for partOne
        return 1
    else:
        return 0

data = open("day04Input.txt", "r")
lines = data.readlines()
data.close()

linesTest = {
    "2-4,6-8",
    "2-3,4-5",
    "5-7,7-9",
    "2-8,3-7",
    "6-6,4-6",
    "2-6,4-8"
}

partOne(lines)