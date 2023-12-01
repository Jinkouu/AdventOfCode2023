from collections import deque
ints = {"one": 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
listOfWords = []
listOfIntWords = []

def readFile():
    with open("input.txt") as input:
        for line in input:
            listOfWords.append(line)

def checkDigit(string):
    print(string)
    
    #state = 0
    #for key in ints:
    #    if key in string:
    #        state += 1
    #if state == 0:
    #    return
    ##print("working")
    #for key in ints:
    #    for i in range (0, len(string) - 1):
    #        for k in range (i, len(string) - 1):
    #            if key in string[i : k]:
    #                string = string[: k] + str(ints[key]) + string[k:]
    state = False
    for key, value in ints.items():
        for i in range (0, len(string)):
            for k in range (i, len(string)):
                if key in string[i : k+1]:
                    string = string[: k] + str(ints[key]) + string[k:]

                
        #if key in string:
        #    string = string.replace(key, str(value))
    listOfIntWords.append(string)
    print(string)
    print(calcVal(string))


def calcVal(string):
    queue = deque()
    for char in string:
        if char.isnumeric():
            queue.append(char)
    if len(queue) == 0:
        return 0
    elif len(queue) == 1:
        return int(queue[0] + queue[0]) 
    elif len(queue) >= 2:
        return int(queue[0] + queue[len(queue) - 1])

def loopFile():
    sum = 0
    for word in listOfWords:
        #print(word)
        checkDigit(word)

    for word in listOfIntWords:
        #print(word)
        #print(int(calcVal(word)))
        sum += int(calcVal(word))
    return sum

readFile()
print(loopFile())