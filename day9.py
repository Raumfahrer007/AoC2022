import copy

def buildGrid(lines):
    l, r, u, d = 0, 0, 0, 0
    for line in lines:
        operations = line.split()
        match operations[0]:
            case "L":
                l += int(operations[1])
            case "R":
                r += int(operations[1])
            case "U":
                u += int(operations[1])
            case "D":
                d += int(operations[1])
    horizontal = l + r  # max movement without reaching borders
    vertical = u + d

    grid = list()
    for i in range(vertical):
        grid.append(list())
        for _ in range(horizontal):
            grid[i].append(".")
    start = [u, r]
    return grid, start


def moveHead(head, operation):
    match operation:
            case "L":
                head[1] -= 1
            case "R":
                head[1] += 1
            case "U":
                head[0] -= 1
            case "D":
                head[0] += 1


def moveTail(grid, head, tail, tailNum):

    if head[1] + 1 < tail[1]:
        tail[1] -= 1
        if head[0] > tail[0]:
            tail[0] += 1
        elif head[0] < tail[0]:
            tail[0] -= 1
    elif head[1] - 1 > tail[1]:
        tail[1] += 1
        if head[0] > tail[0]:
            tail[0] += 1
        elif head[0] < tail[0]:
            tail[0] -= 1
    elif head[0] + 1 < tail[0]:
        tail[0] -= 1
        if head[1] > tail[1]:
            tail[1] += 1
        elif head[1] < tail[1]:
            tail[1] -= 1
    elif head[0] - 1 > tail[0]:
        tail[0] += 1
        if head[1] > tail[1]:
            tail[1] += 1
        elif head[1] < tail[1]:
            tail[1] -= 1
    if tailNum == 9:
        grid[tail[0]][tail[1]] = "#"
    

def partOne(lines):
    grid, start = buildGrid(lines)
    head, tail = copy.deepcopy(start), copy.deepcopy(start)

    for line in lines:
        operations = line.split()
        for _ in range(int(operations[1])):
            moveHead(head, operations[0])
            moveTail(grid, head, tail, 9)   # 9 to print "#" in grid
        
    tailPositions = 0
    for row in grid:
        tailPositions += row.count("#")
    print(tailPositions)


def partTwo(lines):
    grid, start = buildGrid(lines)
    rope = list()
    for _ in range(10):
        rope.append(copy.deepcopy(start))
    
    for line in lines:
        operations = line.split()
        for _ in range(int(operations[1])):
            moveHead(rope[0], operations[0])
            for i in range(1, len(rope)):
                moveTail(grid, rope[i - 1], rope[i], i)

    tailPositions = 0
    for row in grid:
        #print(row)
        tailPositions += row.count("#")
    print(tailPositions)



data = open("day9Input.txt", "r")
lines = data.readlines()
data.close()

linesTest = [
    "R 5\n",
    "U 8\n",
    "L 8\n",
    "D 3\n",
    "R 17\n",
    "D 10\n",
    "L 25\n",
    "U 20"
]

linesTest2 = [
    "R 4\n",
    "U 4\n",
    "L 3\n",
    "D 1\n",
    "R 4\n",
    "D 1\n",
    "L 5\n",
    "R 2"
]


partOne(lines)
partTwo(lines)