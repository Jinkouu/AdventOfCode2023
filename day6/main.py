time = []
dist = []
ways = []

def readFile():
    with open("day6\\input.txt") as input:
        for lines in input:
            newLine = lines.strip()
            newLine = newLine.split(' ')
            newLine = list(filter(None, newLine))
            print(newLine)
            if newLine[0] == "Time:":
                #time.append(newLine)
                for i in range(1, len(newLine)):
                    time.append(newLine[i])
            elif newLine[0] == "Distance:":
                #dist.append(newLine)
                for i in range(1, len(newLine)):
                    dist.append(newLine[i])

def calc():
    for race in range (len(time)):
        numOfWays = 0
        for hold in range (int(time[race])):
            if(hold * (int(time[race]) - hold) > int(dist[race])):
                #print(hold)
                numOfWays += 1
        ways.append(numOfWays)
    multi = 1
    for way in ways:
        multi *= way
    print(multi)

readFile()
calc()