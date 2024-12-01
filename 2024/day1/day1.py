list1 = []
list2 = []

def readFile():
    global list1, list2
    with open("test.txt") as input:
        for line in input:
            line = line.split()
            list1 = sortedInsert(list1, line[0])
            list2 = sortedInsert(list2, line[1])

def sortedInsert(arr: list, n: int) -> list:
    if len(arr) == 0:
        arr.append(n)
        return arr

    for i in range(len(arr)):
        if arr[i] > n :
            arr.insert(i, n)
            return arr

    arr.append(n) # n is greater than all elements
    return arr

def calcDiff():
    diff: int = 0
    for i in range(len(list1)):
        diff += abs(int(list1[i]) - int(list2[i]))
    print(diff)

def dictionarise():
    dict1 = {key: 0 for key in list1}
    dict2 = {key: 0 for key in list2}

    for n in list1:
        dict1[n] += 1
    for n in list2:
        dict2[n] += 1
    
    keys1 = set(dict1.keys())
    keys2 = set(dict2.keys())

    common_keys = keys1 & keys2

    sim = 0
    for num in common_keys:
        sim += dict1[num] * int(num) * dict2[num] 
    print(sim)
        


readFile()
calcDiff()
dictionarise()