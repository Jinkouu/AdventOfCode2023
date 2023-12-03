from collections import deque
import re

listOfChars = []


def readFile():
    with open("day3\\test.txt") as input:
        for lines in input:
            word = lines.split('.')
            listOfChars.append(word)
            print(word)
    #for row in listOfChars:
    #    print(row)

def loop():
    for row in range(len(listOfChars)):
        for col in range(len(listOfChars[row])):
            x = len(listOfChars[row][col])
            try:
                for r in range
            except:
                #out of bounds
            print(x)

#def checkAdjacent(row, col):
    #for r, c in listOfChars:
    #    if listOfChars[r][c] == listOfChars[row][col]:
    #        print("true")


readFile()
loop()

