def getPlatform():
    # with open("./14/platform_example.txt", "r") as f:
    with open("./14/platform.txt", "r") as f:
        return f.read().splitlines()


def flipPlatform(platform):
    flippedPlatform = []
    for i in range(len(platform[0])):
        column = "".join([line[i] for line in platform])
        flippedPlatform.append(column)
    return flippedPlatform


def slideRocksNorth(platform):
    columns = flipPlatform(platform)

    newColumns = []

    for column in columns:
        newColumn = ""
        sections = column.split("#")

        for i, section in enumerate(sections):
            prefix = "#" if i > 0 else ""
            if len(section) == 0:
                newColumn += prefix
                continue

            numberOfRocks = section.count("O")
            numberOfEmptySpaces = len(section) - numberOfRocks
            newColumn += prefix + "O" * numberOfRocks + "." * numberOfEmptySpaces
        
        newColumns.append(newColumn)

    flippedPlatform = flipPlatform(newColumns)
    return flippedPlatform


def totalLoad():
    platform = slideRocksNorth(getPlatform())
    print(f"Platform: {platform}")
    numberOfRows = len(platform)
    totalLoad = 0

    for i, row in enumerate(platform):
        weightMultipler = numberOfRows - i
        numberOfRocks = row.count("O")
        totalLoad += numberOfRocks * weightMultipler

    return totalLoad


if __name__ == "__main__":
    totalLoad = totalLoad()
    print(f"Total load: {totalLoad}")
