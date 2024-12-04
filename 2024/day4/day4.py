def readFile():
    with open("test.txt") as input:
        input = input.readlines()
        rows = len(input)
        cols = len(input[0].strip())
        matrix = [["." for _ in range ]]

        #for line in input:

readFile()