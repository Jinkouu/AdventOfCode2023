from collections import deque
import re

listOfChars = []
listOfCoords = []
symbols = {}
currNum = ""


def readFile():
    with open("day3\\test.txt") as input:
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
            #x = len(listOfChars[row][col])
            #print(listOfChars[row][col])
    #print(listOfCoords)

def searchAround():
    for element in listOfCoords:
        #start = element[0]
        startX = element[0][0]
        startY = element[0][1]
        #end = element[1]
        endX = element[1][0]
        endY = element[1][1]
        if (startX - 1) > 0: #if left isnt out of bounds, increase search area
            startX -= 1
        if (startY - 1) > 0: #if top isnt out of bounds, increase search area
            startY -= 1
        if (endX + 1) < len(listOfCoords[0]): # if right isnt out of bounds, increase search area
            endX += 1
        if (endY + 1) < len(listOfCoords): # if bottom isnt out of bounds, increase search area
            endY += 1
        
        


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
#prints()

