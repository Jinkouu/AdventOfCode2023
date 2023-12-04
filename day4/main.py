from collections import deque
import re

listOfInts = []
listOfWinning = []

listOfIntSplit = []
listOfWinningSplit = []
listOfPoints = []
listOfWinnings = []
scratchCards = {}

def readFile():
    with open("day4\\input.txt") as input:
        for lines in input:
            newLine = lines.strip()
            #words = newLine.split(' | ')
            words = re.split(': | \| ', newLine)
            listOfInts.append(words[1])
            listOfWinning.append(words[2])

def splitLists():
    for line in listOfInts:
        newLine = line.split(' ')
        newLine = list(filter(None, newLine))
        listOfIntSplit.append(newLine)
    for line in listOfWinning:
        newLine = line.split(' ')
        newLine = list(filter(None, newLine))
        listOfWinningSplit.append(newLine)

def calculateWinnings():
    for k in range(0, len(listOfIntSplit)):
        points = 0
        for i in range (0, len(listOfIntSplit[k])):
            for j in range (0, len(listOfWinningSplit[k])):
                #print(listOfIntSplit[k][i], listOfWinningSplit[k][j])
                if int(listOfIntSplit[k][i]) == int(listOfWinningSplit[k][j]):
                    #print(listOfIntSplit[k][i], listOfWinningSplit[k][j])
                    if points == 0:
                        points = 1
                    else:
                        points = points * 2
        #print(points)
        listOfPoints.append(points)

def calculateSum():
    sum = 0
    for point in listOfPoints:
        sum += int(point)
    print("part 1:", sum)

def calculateScratches():
    coppy = [1]*len(listOfIntSplit)
    for k in range(0, len(listOfIntSplit)):
        copies = 0
        for i in range (0, len(listOfIntSplit[k])):
            for j in range (0, len(listOfWinningSplit[k])):
                if int(listOfIntSplit[k][i]) == int(listOfWinningSplit[k][j]):
                    copies += 1
        while copies > 0:
            coppy[k+copies] += 1 *coppy[k]
            copies -= 1
            #scratchCards["game " + str(z)] = scratchCards.get("game " + str(z), 0) + 1
        #for z in range(k, k + copies - 1):
        #    scratchCards[z] = scratchCards.get(z, 0) + 1
        #listOfWinnings.append(copies)
        #copies = 0
    print(sum(coppy))

readFile()
splitLists()
calculateWinnings()
calculateSum()
calculateScratches()
#printScratches()