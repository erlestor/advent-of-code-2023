def getInstructions():
    with open("./8/map.txt", "r") as f:
    # with open("./8/testMap.txt", "r") as f:
        text = f.read()
        instructions = text.split("\n\n")[0]
        map = {}

        for path in text.split("\n\n")[1].split("\n"):
            key = path.split()[0]
            left = path.split()[2][1:4:]
            right = path.split()[3][0:3:]
            map[key] = (left, right)

        return instructions, map

def findRequiredSteps(instructions, map):
    location = "AAA"
    endFound = False
    loops = 1

    while not endFound:
        for i, instruction in enumerate(instructions):
            # use i to return the steps
            locationIdx = 0 if instruction == "L" else 1
            location = map[location][locationIdx]

            if location == "ZZZ":
                endFound = True
                return (i + 1) * loops

        loops += 1
    
    return "Uh oh. Didnt find ZZZ"


if __name__ == "__main__":
    instructions, map = getInstructions()
    print(instructions)
    print(map)

    steps = findRequiredSteps(instructions, map)
    print("Required steps:", steps)