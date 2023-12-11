# plan:
# - instead of expanding galaxies. just mark empty rows and columns with x
# - when finding shortest path: count x's passed 
# - add number of x's * 1 million to length


def replaceValue(space, position, value):
    row, col = position
    space[row] = space[row][:col] + value + space[row][col + 1:]


def getSpace():
    with open("./11/space.txt", "r") as f:
    # with open("./11/space_example_1.txt", "r") as f:
        return f.read().split("\n")


def getExpandedSpace():
    space = getSpace()

    # expand vertically
    for rowIdx, row in enumerate(space):
        if row.count(".") == len(row):
            space[rowIdx] = "x" * len(row)
    
    # expand horizontally
    for colIdx, _ in enumerate(space[0]):
        col = "".join([row[colIdx] for row in space])

        if col.count(".") + col.count("x") == len(col):
            for rowIdx, row in enumerate(space):
                position = (rowIdx, colIdx)
                replaceValue(space, position, "x")

    return space


# assumes space is expanded
def getGalaxyLocations(space):
    galaxyLocations = []

    for rowIdx, _ in enumerate(space):
        for colIdx, _ in enumerate(space[rowIdx]):
            if space[rowIdx][colIdx] == "#":
                galaxyLocations.append((rowIdx, colIdx))
    
    return galaxyLocations


def getShortestPathLength(space, start, end):
    startRow, startCol = start
    endRow, endCol = end
    length = 0
    expansionSize = 1_000_000

    down = [row[startCol] for row in space[startRow + 1: endRow + 1:]]
    length += down.count("x") * expansionSize + down.count("#") + down.count(".")

    right = space[endRow][startCol + 1: endCol + 1:] if endCol >= startCol else space[endRow][endCol:startCol:]
    length += right.count("x") * expansionSize + right.count("#") + right.count(".")

    return length


def getAllShortestPaths():
    space = getExpandedSpace()
    galaxies = getGalaxyLocations(space)
    totalLength = 0

    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            start = galaxies[i]
            end = galaxies[j]
            totalLength += getShortestPathLength(space, start, end)
    
    return totalLength


if __name__ == "__main__":
    totalLength = getAllShortestPaths()
    print(f"Total length of shortest paths: {totalLength}")
    print("Expected: 685038186836")