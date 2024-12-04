def readFile():
    with open("input.txt") as input:
        input = input.readlines()
        rows = len(input)
        cols = len(input[0].strip())
        matrix = [["." for _ in range(cols)] for _ in range(rows)] #call matrix using rows and then columns
        count = 0
        
        #left to right
        for j in range(0, len(input)): #rows
            for i in range(0, len(input[j])): # columns
                if i - 3 >= 0:
                    if input[j][i] == "S" and input[j][i-1] == "A" and input[j][i-2] == "M" and input[j][i-3] == "X":
                        count += 1
                        matrix[j][i] = "S"
                        matrix[j][i-1] = "A" 
                        matrix[j][i-2] = "M" 
                        matrix[j][i-3] = "X"
        
        #right to left
        for j in range(len(input)): #rows
            for i in range(0, len(input[j])): # columns
                if i - 3 >= 0:
                    if input[j][i-3] == "S" and input[j][i-2] == "A" and input[j][i-1] == "M" and input[j][i] == "X":
                        count += 1
                        matrix[j][i-3] = "S"
                        matrix[j][i-2] = "A" 
                        matrix[j][i-1] = "M" 
                        matrix[j][i] = "X"

        #up to down
        for j in range(0,len(input)): #rows
            for i in range(0, len(input[j])): # columns
                if j - 3 >= 0:
                    if input[j][i] == "S" and input[j-1][i] == "A" and input[j-2][i] == "M" and input[j-3][i] == "X":
                        count += 1
                        matrix[j][i] = "S"
                        matrix[j-1][i] = "A" 
                        matrix[j-2][i] = "M" 
                        matrix[j-3][i] = "X"

        #down to up
        for j in range(0,len(input)): #rows
            for i in range(0, len(input[j])): # columns
                if j - 3 >= 0:
                    if input[j-3][i] == "S" and input[j-2][i] == "A" and input[j-1][i] == "M" and input[j][i] == "X":
                        count += 1
                        matrix[j-3][i] = "S"
                        matrix[j-2][i] = "A" 
                        matrix[j-1][i] = "M" 
                        matrix[j][i] = "X"
        
        #top left to bottom right
        for j in range(0,len(input)): #rows
            for i in range(0, len(input[j])): # columns
                if j - 3 >= 0 and i -3 >= 0:
                    if input[j][i] == "S" and input[j-1][i-1] == "A" and input[j-2][i-2] == "M" and input[j-3][i-3] == "X":
                        count += 1
                        matrix[j][i] = "S"
                        matrix[j-1][i-1] = "A" 
                        matrix[j-2][i-2] = "M" 
                        matrix[j-3][i-3] = "X"

        #bottom right to top left
        for j in range(0,len(input)): #rows
            for i in range(0, len(input[j])): # columns
                if j - 3 >= 0 and i -3 >= 0:
                    if input[j-3][i-3] == "S" and input[j-2][i-2] == "A" and input[j-1][i-1] == "M" and input[j][i] == "X":
                        count += 1
                        matrix[j-3][i-3] = "S"
                        matrix[j-2][i-2] = "A" 
                        matrix[j-1][i-1] = "M" 
                        matrix[j][i] = "X"

        #bottom left to top right
        for j in range(0,len(input)): #rows
            for i in range(0, len(input[j])): # columns
                if j - 3 >= 0 and i - 3 >= 0:
                    if input[j-3][i] == "S" and input[j-2][i-1] == "A" and input[j-1][i-2] == "M" and input[j][i-3] == "X":
                        count += 1
                        matrix[j-3][i] = "S"
                        matrix[j-2][i-1] = "A" 
                        matrix[j-1][i-2] = "M" 
                        matrix[j][i-3] = "X"
        
        # top right to bottom left
        for j in range(0,len(input)): #rows
            for i in range(0, len(input[j])): # columns
                if j - 3 >= 0 and i - 3 >= 0:
                    if input[j][i-3] == "S" and input[j-1][i-2] == "A" and input[j-2][i-1] == "M" and input[j-3][i] == "X":
                        count += 1
                        matrix[j][i-3] = "S"
                        matrix[j-1][i-2] = "A" 
                        matrix[j-2][i-1] = "M" 
                        matrix[j-3][i] = "X"

        printMatrix(matrix)
        print(f"part 1 XMAS count: {count}")
        #for line in input:

def printMatrix(matrix):
    for row in matrix:
        print(row)

readFile()