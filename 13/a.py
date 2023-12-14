def getPatterns():
    # with open("./13/patterns_example.txt", "r") as f:
    with open("./13/patterns.txt", "r") as f:
        return [pattern.splitlines() for pattern in f.read().split("\n\n")]


def getLinesBefore(lines):
    stack = []

    for i, line in enumerate(lines):
        if len(stack) == 0 or line != stack[-1]:
            stack.append(line)
            continue

        linesBefore = stack
        linesAfter = lines[i:][::-1]

        # scope out the one that's larger
        # reflection can be anywhere in the pattern
        if len(linesBefore) > len(linesAfter):
            linesBefore = linesBefore[len(linesBefore) - len(linesAfter):]
        if len(linesAfter) > len(linesBefore):
            linesAfter = linesAfter[len(linesAfter) - len(linesBefore):]

        # check if they are mirroring eachother
        isReflection = True

        for j in range(len(linesBefore)):
            if linesBefore[j] != linesAfter[j]:
                isReflection = False
                break

        if isReflection:
            print(linesBefore, linesAfter)
            numberOfRowsAbove = len(stack)
            return numberOfRowsAbove

        stack.append(line)

    return 0


def getNotes(pattern):
    rows = pattern

    # if i can rearrange into columns i can just repeat the above
    columns = []
    for i in range(len(pattern[0])):
        column = ""
        for row in pattern:
            column += row[i]
        columns.append(column)

    notes = getLinesBefore(rows) * 100 + getLinesBefore(columns)

    if notes == 0:
        print("\n".join(pattern))
        raise Exception("No reflection found")

    return notes


if __name__ == "__main__":
    patterns = getPatterns()
    # print(f"Patterns: {patterns}")
    total = sum([getNotes(pattern) for pattern in patterns])
    print(f"Total: {total}")
    print("1318 < answer < 36788")
