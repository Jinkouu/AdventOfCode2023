def readFile():
    with open("test.txt") as input:
        input = input.readlines()
        rows = len(input)
        cols = len(input[0].strip())
        matrix = [[char for char in input[row].strip()] for row in range(rows)] #call matrix using rows and then columns
        print(matrix)

readFile()