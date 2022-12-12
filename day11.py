def partOne(lines):
    monkeysItems = list()   # list that contains the list of items for every monkey
    operations = list() # mathematical operation of each monkey
    tests = list()  # test case for each monkey
    trueCases = list()  # next monkey if test=true for each monkey
    falseCases = list() # next monkey if test=false for each monkey
    inspectedItems = list() # number of inspected items for each monkey

    for i in range((len(lines) + 1) // 7):
    # for each monkey
        # Items 
        line = lines[i * 7 + 1]
        line = line.replace("Starting items: ", "")
        line = line.replace(",", "")
        items = line.split()
        items = list(map(int, items))
        monkeysItems.append(items)
        inspectedItems.append(0)

        # Operation
        line = lines[i * 7 + 2]
        line = line.replace("Operation: new = ", "")
        line = line.replace("\n", "")
        line = line.replace("  ", "")
        operations.append(line)

        # Test
        line = lines[i * 7 + 3]
        lineTemp = line.split()
        tests.append(int(lineTemp[-1]))

        # True Case
        line = lines[i * 7 + 4]
        lineTemp = line.split()
        trueCases.append(int(lineTemp[-1]))

        # False Case
        line = lines[i * 7 + 5]
        lineTemp = line.split()
        falseCases.append(int(lineTemp[-1]))

    # product of all monkey test-numbers
    product = 1
    for x in tests:
        product *= x

    for i in range(10000):
        for monkey in range(len(monkeysItems)):
            for _ in range(len(monkeysItems[monkey])):
                old = monkeysItems[monkey].pop(0)
                worryLevel = eval(operations[monkey])

                # Part One
                #worryLevel = worryLevel // 3
                # Part One

                #Part Two
                factor = worryLevel // product
                worryLevel = worryLevel - (factor * product)
                #Part Two

                if worryLevel % tests[monkey] == 0:
                    monkeysItems[trueCases[monkey]].append(worryLevel)
                else: 
                    monkeysItems[falseCases[monkey]].append(worryLevel)
                inspectedItems[monkey] += 1

    inspectedItems.sort(reverse=True)
    print(inspectedItems)
    print(f"Monkey Business: {inspectedItems[0] * inspectedItems[1]}")




data = open("day11Input.txt", "r")
lines = data.readlines()
data.close()

linesTest = [
    "Monkey 0:\n",
    "Starting items: 79, 98\n",
    "Operation: new = old * 19\n",
    "Test: divisible by 23\n",
    "If true: throw to monkey 2\n",
    "If false: throw to monkey 3\n",
    "\n",
    "Monkey 1:\n",
    "Starting items: 54, 65, 75, 74\n",
    "Operation: new = old + 6\n",
    "Test: divisible by 19\n",
    "If true: throw to monkey 2\n",
    "If false: throw to monkey 0\n",
    "\n",
    "Monkey 2:\n",
    "Starting items: 79, 60, 97\n",
    "Operation: new = old * old\n",
    "Test: divisible by 13\n",
    "If true: throw to monkey 1\n",
    "If false: throw to monkey 3\n",
    "\n",
    "Monkey 3:\n",
    "Starting items: 74\n",
    "Operation: new = old + 3\n",
    "Test: divisible by 17\n",
    "If true: throw to monkey 0\n",
    "If false: throw to monkey 1"
]

partOne(lines)