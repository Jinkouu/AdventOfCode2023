#a k q j t 9 8 7 6 5 4 3 2 1
#order = {'A' : 14, 'K' : 13, 'Q' : 12, 'J' : 11, 'T' : 10, '9' : 9, '8' : 8, '7' : 7, '6' : 6, '5' : 5, '4' : 4, '3' : 3, '2' : 2, '1' : 1}
entries = []

def readFile():
    with open("day7\\input.txt") as input:
        for lines in input:
            newLine = lines.strip()
            newLine = newLine.split(' ')
            newLine = list(filter(None, newLine))
            handDict = {}
            for letter in newLine[0]:
                if letter in handDict:
                    handDict[letter] += 1
                else:
                    handDict[letter] = 1
            
            #sort them
            points = 0
            type = 0
            for entry in handDict.keys():
                if handDict[entry] > points:
                    points = handDict[entry]
            if points == 5:
                type = 6
            elif points == 4:
                type = 5
            elif points == 3 and len(handDict) == 2:
                type = 4
            elif points == 3 and len(handDict) == 3:
                type = 3
            elif points == 2 and len(handDict) == 3:
                type = 2
            elif points == 2 and len(handDict) == 4:
                type = 1
            else:
                type = 0
            #print(type)
                
            #    for point in order.keys():
            #        print(point)
            #        if entry == point:
            #            points += handDict[entry] * order[point]
            entries.append((newLine[0], type, newLine[1]))
    #print(entries)

rank = "AKQJT987654321"

def calcHigher(card1, card2):
    for char1, char2 in zip(card1, card2):
        if rank.index(char1) > rank.index(char2):
            return True
        elif rank.index(char1) < rank.index(char2):
            return False
    return False

def sort():
    #sorting algorithm
    semisort = sorted(entries, key=lambda x: x[1])
    #print(semisort)
    for i in range(1, len(semisort)):
        key = semisort[i]
        j = i - 1
        while(j >= 0 and calcHigher(key[0], semisort[j][0]) and key[1] == semisort[j][1]):
            semisort[j+1] = semisort[j]
            j-=1
        semisort[j + 1] = key

    print(semisort)
    sum = 0
    for i in range(len(semisort)):
        #print(semisort[i][2], int(semisort[i][2])*(i+1))
        sum += int(semisort[i][2])*(i+1)
            
    print(sum)

readFile()
sort()
