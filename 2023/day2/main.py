from collections import deque
import re

listOfWords = []
listOfFixedWords = []
listOfGames = []

def readFile():
    with open("day2\input.txt") as input:
        for line in input:
            listOfWords.append(line)

def splitString():
    for line in listOfWords:
        text = re.split(': | *; ', line)
        listOfFixedWords.append(text)
        #print(text)

def countColours():
    count = 1
    for word in listOfFixedWords:
        dict = {"game" : 0, "red" : 0, "green": 0, "blue" : 0}
        #print(word)
        dict["game"] = count
        for i in range (1, len(word)):
            text = word[i].split(', ')
            #print(text)
            for j in range(0, len(text)):
                num = text[j].split(' ')
                #print(num)
                if num[0].isnumeric() and int(num[0]) >= dict["green"] and "green" in num[1]:
                    dict["green"] = int(num[0])
                elif num[0].isnumeric() and int(num[0]) >= dict["red"] and "red" in num[1]:
                    dict["red"] = int(num[0])
                elif num[0].isnumeric() and int(num[0]) >= dict["blue"] and "blue" in num[1]:
                    dict["blue"] = int(num[0])
        #print(dict)
        listOfGames.append(dict)
        dict.values()
        count += 1

def findGame(red, green, blue):
    sum = 0
    for dict in listOfGames:
        if dict["red"] <= red and dict["blue"] <= blue and dict["green"] <= green:
            sum += dict["game"]
            #print(dict)
    return sum

def findSumOfPower():
    sum = 0
    for dict in listOfGames:
        sum+= dict["red"] * dict["blue"] * dict["green"]
    return sum

readFile()
splitString()
countColours()
print("Part 1: ", findGame(12, 13, 14))
print("Part 2: ", findSumOfPower())