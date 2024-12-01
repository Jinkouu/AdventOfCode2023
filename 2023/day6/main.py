time = []
dist = []
ways = []

def readFilePart1():
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

def calcPart1():
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

def calcPart2():
    timing = ""
    distance = ""
    for t in time:
        timing += str(t)
    for d in dist:
        distance += str(d)
    #print (timing)

    numOfWays = 0
    for hold in range (int(timing)):
        if(hold * (int(timing) - hold) > int(distance)):
            #print(hold)
            numOfWays += 1
    print(numOfWays)

readFilePart1()
calcPart1()
calcPart2()