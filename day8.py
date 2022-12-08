def partOne(lines):
    tallestInLine = 0
    treeRows = list()
    treeColumns = list()
    visibleTrees = 0
    # store rows of trees in list
    for i in enumerate(lines):
        treeRows.append(list())
        for j in range(len(lines[0]) - 1):
            treeRows[i].append(int(lines[i][j]))

    # store columns of trees in list
    columns = len(treeRows[0])
    rows = len(lines)
    for i in range(columns):
        treeColumns.append(list())
        for j in range(rows):
            treeColumns[i].append(int(lines[j][i]))

    for i in range(rows):
        for j in range(columns):
            if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:   # trees on the edge
                visibleTrees += 1
            else:   # trees inside
                tree = int(lines[i][j])
                if max(treeRows[i][:j]) < tree: # From left
                    visibleTrees += 1
                elif max(treeRows[i][j + 1:]) < tree:   # From right
                    visibleTrees += 1
                elif max(treeColumns[j][:i]) < tree:    # From top
                    visibleTrees += 1
                elif max(treeColumns[j][i + 1:]) < tree:    # from bottom
                    visibleTrees += 1
    print(visibleTrees)


def partTwo(lines):
    treeRows = list()
    highestScenicScore = 0
    # store rows of trees in list
    for i in enumerate(lines):
        treeRows.append(list())
        for j in range(len(lines[0]) - 1):
            treeRows[i].append(int(lines[i][j]))

    for i in range(len(treeRows)):
        for j in range(len(treeRows[0])):
            l, r, t, b = 0, 0, 0, 0
            tree = treeRows[i][j]
            if j > 0:   # Score left
                for k in reversed(range(j)):
                    if treeRows[i][k] >= tree:
                        l += 1
                        break
                    l += 1
            if j < len(treeRows[0]) - 1:   # Score right
                for k in range(j + 1, len(treeRows[0])):
                    if treeRows[i][k] >= tree:
                        r += 1
                        break
                    r += 1
            if i > 0:   # Score top
                for k in reversed(range(i)):
                    if treeRows[k][j] >= tree:
                        t += 1
                        break
                    t += 1
            if i < len(treeRows) - 1:   # Score bottom
                for k in range(i + 1, len(treeRows)):
                    if treeRows[k][j] >= tree:
                        b += 1
                        break
                    b += 1
            score = l * r * t * b
            if score > highestScenicScore:
                highestScenicScore = score
    print(highestScenicScore)



data = open("day8Input.txt", "r")
lines = data.readlines()
data.close()

linesTest = [
    "30373\n",
    "25512\n",
    "65332\n",
    "33549\n",
    "35390\n"
]

partOne(lines)
partTwo(lines)