inp = ""
traversal = []

def readFile():
    global inp
    with open("day8\\test1.txt") as input:
        inp = input.readline().strip()
        for lines in input:
            lines = lines.strip()
            #print(len(lines))
            if len(lines) == 16:
                equal_index = lines.index("=")
                open_paren_index = lines.index("(")
                close_paren_index = lines.index(")")

                # Extract substrings
                E1 = lines[:equal_index].strip()
                E2, E3 = map(str.strip, lines[open_paren_index + 1:close_paren_index].split(","))
                traversal.append((E1, E2, E3))

readFile()
print(inp)
print(traversal)
            