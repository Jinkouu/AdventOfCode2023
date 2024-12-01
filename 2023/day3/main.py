from collections import deque
import re

listOfChars = []
listOfCoords = []
symbols = {}
parts = {}
ratio = []
currNum = ""


def readFile():
    with open("day3\\input.txt") as input:
        for lines in input:
            newLine = lines.strip()
            listOfChars.append([(line) for line in newLine])
    #print(listOfChars)

def findSymbols():
    for row in range(len(listOfChars)):
        for col in range(len(listOfChars[row])):
            if listOfChars[row][col] not in "0123456789.":
                sym = listOfChars[row][col]
                if sym in symbols:
                    symbols[sym] += 1
                else:
                    symbols[sym] = 1
    #print(symbols)

def findInts():
    currNum = ""
    for row in range(len(listOfChars)):
        for col in range(len(listOfChars[row])):
            if listOfChars[row][col].isnumeric():
                currNum += listOfChars[row][col]
            else:
                if currNum:
                    listOfCoords.append(((row, col - len(currNum)), (row, col-1), currNum))
                    currNum = ""
        if currNum:
            listOfCoords.append(((row, col - len(currNum)), (row, col - 1), currNum))
            currNum = ""
            #x = len(listOfChars[row][col])
            #print(listOfChars[row][col])
    #print(listOfCoords)

def searchAround():
    for element in listOfCoords:
        height = len(listOfChars) - 1
        width = len(listOfChars) - 1 if listOfChars else 0
        #start = element[0]
        startX = element[0][0]
        startY = element[0][1]
        #end = element[1]
        endX = element[1][0]
        endY = element[1][1]
        #print(startX, startY, endX, endY)
        #print(height, width)
        startX = max(startX - 1, 0)
        startY = max(startY - 1, 0)
        endX = min(endX + 1, width)
        endY = min(endY + 1, height)
        #if (startX - 1) > 0: #if left isnt out of bounds, increase search area
        #    startX -= 1
        #if (startY - 1) > 0: #if top isnt out of bounds, increase search area
        #    startY -= 1
        #if (endX + 1) <= (width): # if right isnt out of bounds, increase search area
        #    endX += 1
        #if (endY + 1) <= (height): # if bottom isnt out of bounds, increase search area
        #    endY += 1
        #print(startX, startY, endX, endY)
        for row in range (startX, endX+1):
            for col in range(startY, endY+1):
                #print(row, col)
                if listOfChars[row][col] in symbols.keys():
                    #print(listOfChars[row][col])
                    if element[2] not in parts:
                        parts[element[2]] = 1
                    else:
                        parts[element[2]] += 1
    #print(parts)

def sumOfParts():
    #print(parts)
    sum = 0
    for key in parts:
        #sum += int(key)
        sum += int(key)*parts[key]
    print(sum)

def part2():
    ratioCoord = {}
    for element in listOfCoords:
        startX, startY = element[0]
        endX, endY = element[1]

        elements = 0

        for row in range(startX - 1, endX + 2):
            for col in range(startY - 1, endY + 2):
                if 0 <= row < len(listOfChars) and 0 <= col < len(listOfChars[0]) and listOfChars[row][col] == '*': # if another number in within the range of *
                    ratioCoordKey = (row, col)
                    if ratioCoordKey not in ratioCoord:
                        ratioCoord[ratioCoordKey] = int(element[2])
                    else:
                        ratioCoord[ratioCoordKey] *= int(element[2])

    toDelete = []
    for ratio in ratioCoord:
        for element in listOfCoords:
            #print(ratioCoord[ratio], element[2])
            if int(element[2]) == int(ratioCoord[ratio]):
                if ratio not in toDelete:
                    toDelete.append(ratio)
                #print(ratioCoord[ratio], element[2])
                
                #ratioCoord.pop(ratio)
    for element in toDelete:
        #print(element)
        ratioCoord.pop(element)

    sum = 0
    for element in ratioCoord:
        sum += ratioCoord[element]
    print(sum)



readFile()
findSymbols()
findInts()
searchAround()
#sumOfParts()
part2()
#prints()

