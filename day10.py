def checkSignal(cycle, signalCycle, totalValue, signalScore):
    cycle += 1
    if cycle == signalCycle:
        signalScore += (signalCycle * totalValue)
        signalCycle += 40
    return cycle, signalCycle, totalValue, signalScore

def partOne(lines):
    signalScore = 0
    cycle = 0
    signalCycle = 20
    totalValue = 1
    for line in lines:
        execution = line.split()
        cycle, signalCycle, totalValue, signalScore = checkSignal(cycle, signalCycle, totalValue, signalScore)
        if len(execution) > 1:
            cycle, signalCycle, totalValue, signalScore = checkSignal(cycle, signalCycle, totalValue, signalScore)
            totalValue += int(execution[1])
    print(signalScore)

def drawPixel(cycle, row, spritePositions):
    if spritePositions.__contains__((cycle) % 40):
        row.append("#")
    else:
        row.append(" ")

def partTwo(lines):
    spritePosition = [0,1,2]
    cycle = -1
    display = list()
    for _ in range(6):
        display.append(list())
    
    for line in lines:
        execution = line.split()
        cycle += 1
        drawPixel(cycle, display[cycle // 40], spritePosition)
        if len(execution) > 1:
            cycle += 1
            drawPixel(cycle, display[cycle // 40], spritePosition)
            spriteMiddle = spritePosition[1] + int(execution[1])
            spritePosition = [spriteMiddle - 1, spriteMiddle, spriteMiddle + 1]

    for row in display:
        string  = ""
        for char in row:
            string += char
        print(string)
    

data = open("day10Input.txt", "r")
lines = data.readlines()
data.close()

partOne(lines)
partTwo(lines)