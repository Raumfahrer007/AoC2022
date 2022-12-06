def partOne(lines):
    # __create stacks of crates__
    border = 0
    for index, line in enumerate(lines):    # find border between stacks and instructions
        if line == "\n":
            border = index
            break

    indices = list()
    for index, char in enumerate(lines[border - 1]): #saves the indices of the stacks
        if char != " " and char != "\n":
            indices.append(index)

    stacks = list()
    for _ in range(len(indices)):   # creates lists for stacks of crates
        stacks.append(list())

    for i, line in enumerate(lines):    # stores all crates per column in one lists
        if i == border - 1:  # read just the lines with crates
            break
        for j, crateIndex in enumerate(indices):    # looks at position crateIndex in line
            if line[crateIndex] != " ":             # if there is a create, add it to the stack
                stacks[j].append(line[crateIndex])  

    for stack in stacks:
        stack.reverse() # for better handling with pop and append

    # __save instructions__
    instructions = list()
    for i, line in enumerate(lines):
        if i < border + 1:  # 10
            continue
        line = line.replace("move ", "")
        line = line.replace("from ", "")
        line = line.replace("to ", "")
        instructions.append(line.split())

    # __execute instructions__
    for instruction in instructions:
        instruction[0] = int(instruction[0])
        instruction[1] = int(instruction[1]) - 1
        instruction[2] = int(instruction[2]) - 1

        amount = instruction[0]
        fromStack = stacks[instruction[1]]
        toStack = stacks[instruction[2]]
        movingStack = fromStack[len(fromStack) - amount : len(fromStack)]
        newFromStack = fromStack[0 : len(fromStack) - amount]
        newToStack = extendOne(toStack, movingStack)
        stacks[instruction[1]] = newFromStack
        stacks[instruction[2]] = newToStack

    # print top crates
    for stack in stacks:
        print(stack[-1])
        
def extendOne(list1, list2):
    for element in list2: # part one: reversed(list2)
        list1.append(element)
    return list1
        


data = open("day5Input.txt", "r")
lines = data.readlines()
data.close()

linesTest = [
    "    [D]    \n",
    "[N] [C]    \n",
    "[Z] [M] [P]\n",
    " 1   2   3 \n",
    "\n",
    "move 1 from 2 to 1\n",
    "move 3 from 1 to 3\n",
    "move 2 from 2 to 1\n",
    "move 1 from 1 to 2\n"
]
partOne(lines)