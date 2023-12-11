# expand empty space
# find location of all galaxies
# make a function for finding length of shortest path between two galaxies
# loop through all combinations of galaxy pairs and sum the shortest paths


def insertGalaxy(space, position, value):
    row, col = position
    space[row] = space[row][:col] + value + space[row][col:]


def getSpace():
    with open("./11/space.txt", "r") as f:
    # with open("./11/space_example_1.txt", "r") as f:
        return f.read().split("\n")


def getExpandedSpace():
    space = getSpace()
    print(f"Start space: {space}")

    # expand vertically
    rowIdx = 0
    while rowIdx < len(space):
        row = space[rowIdx]

        if row.count(".") == len(row):
            space.insert(rowIdx, row)
            rowIdx += 1
        
        rowIdx += 1
    
    # expand horizontally
    colIdx = 0
    while colIdx < len(space[0]):
        col = "".join([row[colIdx] for row in space])

        if col.count(".") == len(col):
            for rowIdx, row in enumerate(space):
                position = (rowIdx, colIdx)
                insertGalaxy(space, position, ".")
            colIdx += 1

        colIdx += 1
    
    print(f"Expanded space: {space}")
    return space


# assumes space is expanded
def getGalaxyLocations(space):
    galaxyLocations = []

    for rowIdx, _ in enumerate(space):
        for colIdx, _ in enumerate(space[rowIdx]):
            if space[rowIdx][colIdx] == "#":
                galaxyLocations.append((rowIdx, colIdx))
    
    print(f"Galaxy locations: {galaxyLocations}")
    return galaxyLocations


def getShortestPathLength(space, start, end):
    startRow, startCol = start
    endRow, endCol = end

    return abs(endRow - startRow) + abs(endCol - startCol)


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