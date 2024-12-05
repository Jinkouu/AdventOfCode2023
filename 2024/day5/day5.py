rules = []
updates = []

def readFile():
    global rules, updates
    with open("test.txt") as input:
        input = input.readlines()

        before = True
        for i in range(len(input)):
            if input[i].strip() == "": #blank line between rules and updates
                before = False
                continue

            if before == True:
                rule = input[i].strip().split("|")
                ruleTuple = (rule[0], rule[1])
                rules.append(ruleTuple)
                #rules[rule[0]] = rule[1]
            else:
                updates.append(input[i].strip())

    #print(rules)
    #print(updates)
def matchingRules(num) -> list[int]:
    global rules
    queryRules = []
    for rule in rules:
        if num == rule[0]:
            queryRules.append(rule)
    return queryRules


def partA():
    global rules, updates
    count = 0
    for update in updates:
        valid = True
        update = update.split(",")
        for i in range(0, len(update)-1):
            #queryRules = matchingRules(update[i])
            matchingRule = [queryRules[1] for queryRules in matchingRules(update[i])]
            #print(f"{valid} {update[i]} {matchingRule} {update[i+1:]}")
            if not any(r in update[i+1:] for r in matchingRule): #the update minus the first _ amount of entries
                valid = False
                break #break the rule finding loop
        if valid:
            count += int(update[int(len(update)/2)])
        print(f"{valid}: {update}")
    print(count)





readFile()
partA()