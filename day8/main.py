from math import lcm
inp = ""
traversal = {}

def readFile():
    global inp
    with open("day8\\input.txt") as input:
        inp = input.readline().strip()
        for lines in input:
            lines = lines.strip()
            #print(len(lines))
            if len(lines) == 16:
                equal_index = lines.index("=")
                open_paren_index = lines.index("(")
                close_paren_index = lines.index(")")

                # Extract substrings, use E1 as dict key and E2, E3 as a tuple data entry
                E1 = lines[:equal_index].strip()
                E2, E3 = map(str.strip, lines[open_paren_index + 1:close_paren_index].split(","))
                traversal[E1] = (E2, E3)


def calcSteps1():
    currentKey = "AAA"
    steps = 0
    finished = False
    #print(current)
    while finished == False:
        for direction in inp: # for each letter in INP (L or R)
            if "L" in direction:
                #current = getLeft(current)
                currentKey = traversal[currentKey][0]
                steps += 1
            else:
                currentKey = traversal[currentKey][1]
                steps += 1

            #also check if it is at the destination (ZZZ)
            if currentKey == "ZZZ":
                finished = True
                return steps

def calcSteps(currentKey):
    current = traversal[currentKey]
    steps = 0
    finished = False
    #print(current)
    while finished == False:
        for direction in inp: # for each letter in INP (L or R)
            if "L" in direction:
                #current = getLeft(current)
                currentKey = traversal[currentKey][0]
                steps += 1
            else:
                currentKey = traversal[currentKey][1]
                steps += 1

            #also check if it is at the destination (ZZZ)
            if currentKey[2] == "Z":
                finished = True
                return steps

def calcSteps2():
    startPoints = []
    for key in traversal.keys():
        if key[2] == "A":
            startPoints.append(key)
    
    result = []
    for key in startPoints:
        result.append(calcSteps(key))
    return lcm(*result)


readFile()
print("Part 1:", calcSteps1())
print("Part 2:", calcSteps2())
            