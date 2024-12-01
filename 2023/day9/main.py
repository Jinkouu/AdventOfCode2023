listOfInputs = []

def readFile():
    with open("day9\\test.txt") as input:
        for line in input:
            line = line.strip().split(' ')
            inp = []
            for num in line:
                inp.append(num)
            listOfInputs.append(inp)
        
def sumOfLayer(layer):
    sum = 0
    for num in layer:
        sum += int(num)
    return sum

def calcPart1():
    allResults = []
    for history in range (len(listOfInputs)):
        historyEntry = listOfInputs[history]
        while sumOfLayer(historyEntry[len(historyEntry) - 1]) != 0:
            layer = []
            for num in range (1, len(listOfInputs[history])):
                e1 = int(listOfInputs[history][num])
                e2 = int(listOfInputs[history][num - 1])
                diff = e1 - e2
                #print(diff)
                layer.append(diff)
            historyEntry.append(layer)
        print(historyEntry)

readFile()
calcPart1()