reports = {"Safe": 0, "Unsafe": 0}

def readFile():
    global reports
    with open("test.txt") as input:
        for level in input:
            level = level.split()
            level = list(map(int, level))

            state = None
            safe = True

            for num in range(1, len(level)): #true for increasing, false for decreasing, None for beginning
                tempState = None
                diff = level[num] - level[num - 1]

                if 1 <= diff <= 3:
                    tempState = True
                elif -3 <= diff <= -1:
                    tempState = False
                else:
                    safe = False
                    break

                if state is None:
                    state = tempState
                elif tempState != state:
                    safe = False
                    break
            if safe:
                reports["Safe"] += 1
            else:
                reports["Unsafe"] += 1
        print(reports)

readFile()





