def readFile():
    with open("test.txt") as input:
        rules = {}
        for line in input:
            if line.strip() == "": #blank line between rules and updates
                break
            rule = line.strip().split("|")
            rules[rule[0]] = rule[1] 
    print(rules)

readFile()