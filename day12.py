import copy

class Map:
    def __init__(self, lines):
        self.grid = list()
        for i, line in enumerate(lines):
            line = line.replace("\n", "")
            listLine = list(line)
            if listLine.__contains__("S"):
                self.start = [i, listLine.index("S")]
                listLine[listLine.index("S")] = chr(ord("a") - 1)   # makes ASCII-number of start smaller than ASCII-number of "a"
            if listLine.__contains__("E"):
                self.end = [i, listLine.index("E")]
                listLine[listLine.index("E")] = chr(ord("z") + 1)   # makes ASCII-number of end bigger than ASCII-number of "z"
            newLine = list()
            for char in listLine:
                newLine.append(ord(char))   # Saves ASCII-numbers of every position
            self.grid.append(newLine)


    def getPositionValue(self, cp, r=0, c=0, part=1):   # Returns value at specific position
        value = 0
        if (r > 0 and cp[0] == len(self.grid) - 1) or (r < 0 and cp[0] == 0):
            value = 1000     # number that's bigger than any number in the grid
        elif (c > 0 and cp[1] == len(self.grid[cp[0]]) - 1) or (c < 0 and cp[1] == 0):
            value = 1000     # number that's bigger than any number in the grid
        else:
            value = self.grid[cp[0] + r][cp[1] + c]

        if part == 2 and value == 1000:
            return -value
        else:
            return value

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end


def alterPosition(cp, r, c):    # Return new coordinates
    return [cp[0] + r, cp[1] + c]

def partOne(lines):
    map = Map(lines)
    start = map.getStart()  
    end = map.getEnd()

    deadends = list() 
    positionsVisited = list()

    firstRoute = list()
    firstRoute.append(start)
    routes = list()
    routes.append(firstRoute)

    shortestRoute = list()
    finished = False

    while not finished:
        newRoutes = list()
        for route in routes:
            possibleWays = [0, 0, 0, 0]    #up, down, left, right
            cp = route[-1]

            if cp == end:
                finished = True
                shortestRoute = route
                break

            # -- up --
            if (map.getPositionValue(cp, -1, 0) <= map.getPositionValue(cp) + 1) \
                    and not deadends.__contains__(alterPosition(cp, -1, 0)) and not route.__contains__(alterPosition(cp, -1, 0)):
                possibleWays[0] = alterPosition(cp, -1, 0)

            # -- down --
            if (map.getPositionValue(cp, 1, 0) <= map.getPositionValue(cp) + 1) \
                    and not deadends.__contains__(alterPosition(cp, 1, 0)) and not route.__contains__(alterPosition(cp, 1, 0)):
                possibleWays[1] = alterPosition(cp, 1, 0)

            # -- left --
            if (map.getPositionValue(cp, 0, -1) <= map.getPositionValue(cp) + 1) \
                    and not deadends.__contains__(alterPosition(cp, 0, -1)) and not route.__contains__(alterPosition(cp, 0, -1)):
                possibleWays[2] = alterPosition(cp, 0, -1)

            # -- right --
            if (map.getPositionValue(cp, 0, 1) <= map.getPositionValue(cp) + 1) \
                    and not deadends.__contains__(alterPosition(cp, 0, 1)) and not route.__contains__(alterPosition(cp, 0, 1)):
                possibleWays[3] = alterPosition(cp, 0, 1)

            if not possibleWays == [0, 0, 0, 0]:
                for newStep in possibleWays:
                    if newStep == 0 or positionsVisited.__contains__(newStep):
                        continue
                    else:
                        positionsVisited.append(newStep)
                        newRoute = copy.deepcopy(route)
                        newRoute.append(newStep)
                        newRoutes.append(newRoute)
            else:
                deadends.append(cp)
            
        routes = newRoutes
        
    print(f"Steps necessary: {len(shortestRoute) - 1}")


def partTwo(lines):
    map = Map(lines)
    start = map.getEnd()  

    deadends = list() 
    positionsVisited = list()

    firstRoute = list()
    firstRoute.append(start)
    routes = list()
    routes.append(firstRoute)

    shortestRoute = list()
    finished = False

    while not finished:
        newRoutes = list()
        print(len(routes))
        for route in routes:
            possibleWays = [0, 0, 0, 0]    #up, down, left, right
            cp = route[-1]

            if map.getPositionValue(cp) == ord("a"):
                finished = True
                shortestRoute = route
                break

            # -- up --
            if (map.getPositionValue(cp, -1, 0, 2) >= map.getPositionValue(cp) - 1) \
                    and not deadends.__contains__(alterPosition(cp, -1, 0)) and not route.__contains__(alterPosition(cp, -1, 0)):
                possibleWays[0] = alterPosition(cp, -1, 0)

            # -- down --
            if (map.getPositionValue(cp, 1, 0, 2) >= map.getPositionValue(cp) - 1) \
                    and not deadends.__contains__(alterPosition(cp, 1, 0)) and not route.__contains__(alterPosition(cp, 1, 0)):
                possibleWays[1] = alterPosition(cp, 1, 0)

            # -- left --
            if (map.getPositionValue(cp, 0, -1, 2) >= map.getPositionValue(cp) - 1) \
                    and not deadends.__contains__(alterPosition(cp, 0, -1)) and not route.__contains__(alterPosition(cp, 0, -1)):
                possibleWays[2] = alterPosition(cp, 0, -1)

            # -- right --
            if (map.getPositionValue(cp, 0, 1, 2) >= map.getPositionValue(cp) - 1) \
                    and not deadends.__contains__(alterPosition(cp, 0, 1)) and not route.__contains__(alterPosition(cp, 0, 1)):
                possibleWays[3] = alterPosition(cp, 0, 1)

            if not possibleWays == [0, 0, 0, 0]:
                for newStep in possibleWays:
                    if newStep == 0 or positionsVisited.__contains__(newStep):
                        continue
                    else:
                        positionsVisited.append(newStep)
                        newRoute = copy.deepcopy(route)
                        newRoute.append(newStep)
                        newRoutes.append(newRoute)
            else:
                deadends.append(cp)
            
        routes = newRoutes
        
    print(f"Steps necessary: {len(shortestRoute) - 1}")



data = open("day12Input.txt", "r")
lines = data.readlines()
data.close()

linesTest = [
    "Sabqponm\n",
    "abcryxxl\n",
    "accszExk\n",
    "acctuvwj\n",
    "abdefghi\n"
]

#partOne(lines)
partTwo(lines)