def partOne(lines):
    mostCalories = 0
    calories = 0
    for line in lines:
        if(line != "\n"):
            calories += int(line)
        else:
            if calories > mostCalories:
                mostCalories = calories
            calories = 0

    print(mostCalories)

def partTwo(lines):
    mostCalories = [0, 0, 0]
    calories = 0
    for line in lines:
        if(line != "\n"):
            calories += int(line)
        else:
            for count, max in enumerate(mostCalories):
                if calories > max:
                    mostCalories = insertNumber(mostCalories, count, calories)
                    break
            calories = 0


    print(sum(mostCalories))

def insertNumber(list, index, value):
    list.insert(index, value)
    del(list[-1])
    
    return list


data = open("day1Input.txt", "r")
lines = data.readlines()
data.close()
partTwo(lines)