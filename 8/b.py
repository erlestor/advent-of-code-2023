import math


def getInstructions():
    # with open("./8/testMap2.txt", "r") as f:
    with open("./8/map.txt", "r") as f:
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

    # go through each starting node:
    # - loop instructions till you find a node that ends with Z
    # save the length of the path
    # answer: lcm(length of paths)

    pathLengths = []

    for startingNode in nodes:
        pathLength = 0
        node = startingNode
        endNodeFound = False

        while not endNodeFound:
            for i, instruction in enumerate(instructions):
                pathLength += 1
                direction = 0 if instruction == "L" else 1
                node = map[node][direction]

                if node[-1] == "Z":
                    pathLengths.append(pathLength)
                    endNodeFound = True
                    break
        
        print(f"Path length for {startingNode}: {pathLength}")

    return math.lcm(*pathLengths)


if __name__ == "__main__":
    instructions, map = getInstructions()
    print(instructions)
    print(map)

    steps = findRequiredSteps(instructions, map)
    print("Required steps:", steps)
