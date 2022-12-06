translation = {
    "X" : "A",
    "Y" : "B",
    "Z" : "C"
}
points = {
    "A" : 1,
    "B" : 2,
    "C" : 3
}
rulesWin = {
    "A" : "B",
    "B" : "C",
    "C" : "A",
}
rulesLose = {
    "A" : "C",
    "B" : "A",
    "C" : "B",
}

def partOne(lines):
    totalScore = 0
    for line in lines:
        score = 0
        moves = line.split()
        moves[1] = translation[moves[1]]

        score += points[moves[1]]

        if rulesWin[moves[0]] == moves[1]:
            score += 6
        elif moves[0] == moves[1]:
            score += 3
        
        totalScore += score
    
    print(totalScore)
        


def partTwo(lines):
    totalScore = 0
    for line in lines:
        score = 0
        moves = line.split()

        if moves[1] == "X":     #LOSE
            myMove = rulesLose[moves[0]]
            score += points[myMove]
        elif moves[1] == "Y":   #DRAW
            myMove = moves[0]
            score += 3
            score += points[myMove]
        else:   #WIN
            myMove = rulesWin[moves[0]]
            score += 6
            score += points[myMove]

        totalScore += score
        score = 0
    print(totalScore)


data = open("day2Input.txt", "r")
lines = data.readlines()
data.close()

partTwo(lines)