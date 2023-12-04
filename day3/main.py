from collections import deque
import re

listOfChars = []
listOfCoords = []
symbols = {}
parts = {}
currNum = ""


def readFile():
    with open("day3\\input.txt") as input:
        for lines in input:
            newLine = lines.strip()
            listOfChars.append([(line) for line in newLine])
    print(listOfChars)

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
            #x = len(listOfChars[row][col])
            #print(listOfChars[row][col])
    #print(listOfCoords)

def searchAround():
    for element in listOfCoords:
        height = len(listOfCoords) - 1
        width = len(listOfCoords) if listOfCoords else 0
        #start = element[0]
        startX = element[0][0]
        startY = element[0][1]
        #end = element[1]
        endX = element[1][0]
        endY = element[1][1]
        #print(startX, startY, endX, endY)
        #print(height, width)
        if (startX - 1) > 0: #if left isnt out of bounds, increase search area
            startX -= 1
        if (startY - 1) > 0: #if top isnt out of bounds, increase search area
            startY -= 1
        if (endX + 1) < (width): # if right isnt out of bounds, increase search area
            endX += 1
        if (endY + 1) < (height): # if bottom isnt out of bounds, increase search area
            endY += 1
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
    print(parts)

def sumOfParts():
    sum = 0
    for key in parts:
        sum += int(key)
    print(sum)


def prints():
    print(listOfCoords)

#def checkAdjacent(row, col):
    #for r, c in listOfChars:
    #    if listOfChars[r][c] == listOfChars[row][col]:
    #        print("true")


readFile()
findSymbols()
findInts()
searchAround()
sumOfParts()
#prints()

