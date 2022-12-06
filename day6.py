def partOne(code):
    task = 13   # partOne: 3
    lastThree = list()
    for i, char in enumerate(code):
        if len(lastThree) >= task:
            if lastThree.__contains__(char) or len(set(lastThree)) < task:
                del(lastThree[0])
                lastThree.append(char)
            else:
                print(i + 1)
                break
        else:
            lastThree.append(char)


data = open("day6Input.txt", "r")
code = data.readline()
data.close()

linesTest = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
partOne(code)