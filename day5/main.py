from collections import deque
import re

seeds = []
seedList = []
soilList = []
fertList = []
waterList = []
lightList = []
tempList = []
humidList = []

def readFile():
    with open("day5\\test.txt") as input:
        seed = False
        soil = False
        fert = False
        water = False
        light = False
        temp = False
        humid = False

        for lines in input:
            newLine = lines.strip()
            newLine = newLine.split(' ')
            #newLine = list(filter(None, newLine))
            #print(newLine)
            if newLine[0] == "seeds":
                newLine.pop[0]
                seeds.append(newLine)
            elif newLine[0] == "seed-to-soil":
                seed = True
            elif newLine[0] == "soil-to-fertilizer":
                seed = False
                soil = True
            elif newLine[0] == "fertilizer-to-water":
                soil = False
                fert = True
            elif newLine[0] == "water-to-light":
                fert = False
                water = True
            elif newLine[0] == "light-to-temperature":
                water = False
                light = True
            elif newLine[0] == "temperature-to-humidity":
                light = False
                temp = True
            elif newLine[0] == "humidity-to-location":
                temp = False
                humid = True
            
            if seed:
                seedList.append(newLine)
            elif soil:
                soilList.append(newLine)
            elif fert:
                fertList.append(newLine)
            elif water:
                waterList.append(newLine)
            elif light:
                lightList.append(newLine)
            elif temp:
                tempList.append(newLine)
            elif humid:
                humidList.append(newLine)

def run():
    for seed in seeds:
        calcSeed(int(seed))

def seed(seedNum, sourceNum, range):
    if 


def calcSeed(seedNum):
    for seedMap in seedList:
        #if seedMap[1] == seedNum:
        #    print("continue")
        #else:



readFile()
run()