def readFile1():
    reports = {"Safe": 0, "Unsafe": 0}
    with open("input.txt") as input:
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

def readFile2():
    reports = {"Safe": 0, "Unsafe": 0}
    with open("input.txt") as input:
        for level in input:
            level = level.split()
            level = list(map(int, level))

            exception = False  # tracks exception use
            safe = True
            state = None
            i = 1  # Start comparison from the second element

            while i < len(level):
                print(level)
                print(level[i])
                diff = level[i] - level[i - 1]

                if 1 <= diff <= 3:
                    tempState = True
                elif -3 <= diff <= -1:
                    tempState = False
                else:
                    if not exception:
                        exception = True
                        del level[i] #deletes the number and uses the 1 exception
                        i = 1  # restart from the beginning
                        continue # re-does the loop
                    else:
                        safe = False #if the 1 exception has already been used, make a unsafe report
                        break

                if state is None:
                    state = tempState
                elif tempState != state:
                    if not exception:
                        exception = True
                        del level[i-1] #deletes the number and uses the 1 exception
                        i = 1  # restart from the beginning
                        continue
                    else:
                        safe = False #if the 1 exception has already been used, make a unsafe report
                        break

                i += 1  # next number
            if safe:
                reports["Safe"] += 1
            else:
                print (f"{safe}: {level}")
                reports["Unsafe"] += 1

    print(reports)

readFile1()
readFile2()






