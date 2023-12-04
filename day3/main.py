from collections import deque
import re

listOfChars = []
listOfCoords = []
currNum = ""


def readFile():
    with open("day3\\test.txt") as input:
        for lines in input:
            newLine = lines.strip()
            listOfChars.append([(line) for line in newLine])
    #print(listOfChars)

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
        print(startX, startY, endX, endY)


def prints():
    print(listOfCoords)

#def checkAdjacent(row, col):
    #for r, c in listOfChars:
    #    if listOfChars[r][c] == listOfChars[row][col]:
    #        print("true")


readFile()
findInts()
searchAround()
#prints()

