from collections import deque
ints = {"one": 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
listOfWords = []
listOfIntWords = []

def readFile():
    with open("input.txt") as input:
        for line in input:
            listOfWords.append(line)

def checkDigit(string):
    state = False
    for key, value in ints.items():
        for i in range (0, len(string)):
            for k in range (i, len(string)):
                if key in string[i : k+1]: # basically place the int 1 before the end to account for things like sevenine being 79 = seve7nin9e
                    string = string[: k] + str(ints[key]) + string[k:]
                    break
    listOfIntWords.append(string)

def calcVal(string):
    queue = deque()
    for char in string:
        if char.isnumeric(): # places all ints into a queue in order to get the first and last accordingly
            queue.append(char)
    if len(queue) == 0:
        return 0
    elif len(queue) == 1:
        return int(queue[0] + queue[0]) 
    elif len(queue) >= 2:
        return int(queue[0] + queue[len(queue) - 1])
    
def part1():
    sum = 0
    readFile()
    for word in listOfWords:
        sum += int(calcVal(word))
    return sum

def part2():
    sum = 0
    readFile()
    for word in listOfWords:
        checkDigit(word)

    for word in listOfIntWords:
        sum += int(calcVal(word))
    return sum

def clear():
    listOfWords.clear()
    listOfIntWords.clear()

print("Part 1: ", part1())
clear()
print("Part 2: ", part2())