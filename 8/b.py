def getInstructions():
    # with open("./8/map.txt", "r") as f:
    with open("./8/testMap2.txt", "r") as f:
        text = f.read()
        instructions = text.split("\n\n")[0]
        map = {}

        for path in text.split("\n\n")[1].split("\n"):
            key = path.split()[0]
            left = path.split()[2][1:4:]
            right = path.split()[3][0:3:]
            map[key] = (left, right)

        return instructions, map


def getStartingNodes(map):
    return [key for key in map.keys() if key[-1] == "A"]


def findRequiredSteps(instructions, map):
    # nodes is just [12A, 22A]
    nodes = getStartingNodes(map)
    print("Starting nodes:", nodes)
    numberOfNodes = len(nodes)
    print("Numberofnodes:", numberOfNodes)
    loops = 1

    while True:
        for i, instruction in enumerate(instructions):
            direction = 0 if instruction == "L" else 1

            # find next nodes and see if they all end with Z
            nodes = [map[node][direction] for node in nodes]
            numberOfEndNodes = len([node for node in nodes if node[-1] == "Z"])

            if numberOfEndNodes == numberOfNodes:
                return (i + 1) * loops

        loops += 1


if __name__ == "__main__":
    instructions, map = getInstructions()
    print(instructions)
    print(map)

    steps = findRequiredSteps(instructions, map)
    print("Required steps:", steps)
