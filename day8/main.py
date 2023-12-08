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

                # Extract substrings
                E1 = lines[:equal_index].strip()
                E2, E3 = map(str.strip, lines[open_paren_index + 1:close_paren_index].split(","))
                traversal[E1] = (E2, E3)
                #traversal.append((E1, E2, E3))

#def getLeft(current):
#    for route in traversal: # for each entry in traversal
#        if current[1] == route[0]:
#            return route
#    return
#
#def getRight(current):
#    for route in traversal: # for each entry in traversal
#        if current[2] in route[0]:
#            return route
#    return

def calcSteps():
    currentKey = "AAA"
    current = traversal[currentKey]
    steps = 0
    finished = False
    #print(current)
    while finished == False:
        for direction in inp: # for each letter in INP (L or R)
            if "L" in direction:
                #current = getLeft(current)
                currentKey = traversal[currentKey][0]
                current = traversal[currentKey]
                steps += 1
            else:
                currentKey = traversal[currentKey][1]
                current = traversal[currentKey]
                steps += 1

            #also check if it is at the destination (ZZZ)
            if currentKey == "ZZZ":
                finished = True
                return steps

readFile()
#print(inp)
#print(traversal)
print(calcSteps())
            