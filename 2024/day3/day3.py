def readFile():
    with open("input.txt") as input:
        input = input.read()
        #print(input)
        results = []

        index = 0
        while index < len(input):
            index = input.find("mul", index) # sets the index as the instance of the next "mul"
            if index == -1: #if there is no more, break
                break
        
            snippet = input[index + 3:index + 12] #get mul + 9 characters afterwards (upto 6 digits and 3 symbols)
            results.append(snippet)

            index += 3

    multResult = 0
    for expression in results:
        #for i in range (0, len(expression)):
        i = 0
        while i < len(expression):
            if expression[i] == "(":
                j = i + 1
                digits1 = ""
                while j < len(expression) and expression[j].isdigit() and j-1 <= 3: #finds up to 3 digits
                    digits1 += expression[j]
                    j += 1

                if j < len(expression) and expression[j] == ",": #finds comma
                    j += 1
                else:
                    break

                k = j
                digits2 = ""
                while k < len(expression) and expression[k].isdigit() and k-j <= 3: #finds up to 3 digits
                    digits2 += expression[k]
                    k += 1

                if k < len(expression) and expression[k] == ')': # Valid '(digits,digits)', remove '('
                    multResult = multResult + (int(digits1) * int(digits2))
                    break
                else:
                    break
            else:
            # Ignore characters outside of parentheses
                i += 1
    print(f"Part 1 results: {multResult}")
    #print(results)

import re
def readFile2():
    with open("input.txt") as input:
        input = input.read()
        #print(input)
        results = []

        #use regex this time
        pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)" #first part gets mul(*,*), second gets do(), third part gets don't()

        matches = re.findall(pattern, input)
        
        results.extend(matches)
        print(results)
            
    #states: True: do, False: dont
    state = True
    multResult = 0
    for expression in results:
        if expression == "do()": #the expression is do()
            state = True
        elif expression == "don't()": #the expression is don't()
            state = False
        else:
            i = 0
            while i < len(expression):
                if expression[i] == "(":
                    j = i + 1
                    digits1 = ""
                    while j < len(expression) and expression[j].isdigit() and len(digits1) < 3: #finds up to 3 digits
                        digits1 += expression[j]
                        j += 1

                    if j < len(expression) and expression[j] == ",": #finds comma
                        j += 1
                    else:
                        break

                    k = j
                    digits2 = ""
                    while k < len(expression) and expression[k].isdigit() and len(digits2) < 3: #finds up to 3 digits
                        digits2 += expression[k]
                        k += 1

                    if k < len(expression) and expression[k] == ')': # Valid '(digits,digits)', remove '('
                        if state == True:
                            multResult = multResult + (int(digits1) * int(digits2))
                        break
                    else:
                        break
                else:
                # Ignore characters outside of parentheses
                    i += 1
    print(f"Part 2 results: {multResult}")

readFile()
readFile2()