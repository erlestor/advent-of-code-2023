def getPatterns():
    # with open("./13/patterns_example.txt", "r") as f:
    with open("./13/patterns.txt", "r") as f:
        return [pattern.splitlines() for pattern in f.read().split("\n\n")]


# return true if exactly the same or one character flips and they're equal
# needs to return if flip was used or not
# return linesEqual, flipUsed
# assumes equal line length
def compareLines(line1, line2):
    if line1 == line2:
        return True, False

    commonCharacters = 0
    for i in range(len(line1)):
        c1, c2 = line1[i], line2[i]
        if c1 == c2:
            commonCharacters += 1

    if commonCharacters == len(line1) - 1:
        return True, True

    return False, False


# find the reflection line where
# exactly one character needs to be flipped to be valid
def getLinesBefore(lines):
    stack = []

    for i, line in enumerate(lines):
        # make sure last two lines are valid first for speed
        if len(stack) == 0 or not compareLines(line, stack[-1])[0]:
            # dont flip here? it will be revaluated later anyways
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
        flipsUsed = 0

        for j in range(len(linesBefore)):
            linesEqual, flipped = compareLines(linesBefore[j], linesAfter[j])

            if flipped:
                flipsUsed += 1

            # if they dont match or we are using our second flip
            if not linesEqual or flipsUsed > 1:
                isReflection = False
                break

        if isReflection and flipsUsed == 1:
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
        column = "".join([row[i] for row in pattern])
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
    # print("1318 < answer < 36788")
