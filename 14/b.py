"""
looping 1_000_000_000 times takes very long. 1 min with a simple +1 operation aka. O(n)
there's probably some constraints to find
surely the pattern repeats after a while and i can use that to find the answer
i assume rocks get stuck after a while
maybe just go rock by rock and find where it gets stuck
"""

def getPlatform():
    with open("./14/platform.txt", "r") as f:
    # with open("./14/platform_example.txt", "r") as f:
        return f.read().splitlines()


def flipPlatform(platform):
    flippedPlatform = []
    for i in range(len(platform[0])):
        column = "".join([line[i] for line in platform])
        flippedPlatform.append(column)
    return flippedPlatform


def slideRocks(platform, direction):
    if direction == "north" or direction == "south":
        platform = flipPlatform(platform)

    newRows = []

    for row in platform:
        newRow = ""
        sections = row.split("#")

        for i, section in enumerate(sections):
            prefix = "#" if i > 0 else ""

            if len(section) == 0:
                newRow += prefix
                continue

            numberOfRocks = section.count("O")
            numberOfEmptySpaces = len(section) - numberOfRocks
            if direction == "north" or direction == "west":
                newRow += prefix + "O" * numberOfRocks + "." * numberOfEmptySpaces
            else:
                newRow += prefix + "." * numberOfEmptySpaces + "O" * numberOfRocks
                
        
        newRows.append(newRow)

    if direction == "north" or direction == "south":
        flippedPlatform = flipPlatform(newRows)
    else:
        flippedPlatform = newRows
    return flippedPlatform


# performs one cycle of north,west,south,east and returns the new platform
def performCycle(platform):
    for direction in ["north", "west", "south", "east"]:
        platform = slideRocks(platform, direction)
    return platform


def getFinalPlatform():
    platform = getPlatform()

    previousPlatforms = ["\n".join(platform)]
    cycle = []

    for i in range(1_000_000_000):
        platform = performCycle(platform) 
        platformStr = "\n".join(platform)

        if platformStr in previousPlatforms:
            # found cycle
            previousPlatformIdx = previousPlatforms.index(platformStr)
            cycle = previousPlatforms[previousPlatformIdx:]
            break

        previousPlatforms.append(platformStr)
    

    platformsBeforeCycle = len(previousPlatforms) - len(cycle)

    cycleIdx = (1_000_000_000 - platformsBeforeCycle) % len(cycle)

    finalPlatform = cycle[cycleIdx].splitlines()

    print(f"Final platform: {finalPlatform}")
    return finalPlatform

def totalLoad():
    finalPlatform = getFinalPlatform()
    numberOfRows = len(finalPlatform)
    totalLoad = 0

    for i, row in enumerate(finalPlatform):
        weightMultipler = numberOfRows - i
        numberOfRocks = row.count("O")
        totalLoad += numberOfRocks * weightMultipler

    return totalLoad


if __name__ == "__main__":
    totalLoad = totalLoad()
    print(f"Total load: {totalLoad}")
