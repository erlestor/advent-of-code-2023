# get offsets for the 2 connected nodes given a symbol
offsetsGivenSymbol = {
    "|": ((0, 1), (0, -1)),
    "-": ((0, 1), (0, -1)),
    "L": ((0, 1), (0, -1)),
    "J": ((0, 1), (0, -1)),
    "7": ((0, 1), (0, -1)),
    "F": ((0, 1), (0, -1)),
}

def getGrid():
    with open("./10/testSketch.txt", "r") as f:
        return f.read().split("\n")


def getGridValue(grid, node):
    row, col = node
    return grid[row][col]


def findStartingNode(grid):
    for rowIdx, row in enumerate(grid):
        for colIdx, node in enumerate(row):
            if node == "S":
                return rowIdx, colIdx
    raise Exception("No starting node")


# find the neighboring nodes
# node = (row, col)
def getNeighboringNodes(node):
    row, col = node
    neighboringNodes = []

    # TODO: check if its a "." then discard
    # left
    if row > 0:
        neighboringNodes.append((row - 1, col))
    # right
    if row < len(grid[row]) - 1:
        neighboringNodes.append((row + 1, col))
    # up
    if col > 0:
        neighboringNodes.append((row, col - 1))
    # down
    if col < len(grid) - 1:
        neighboringNodes.append((row, col + 1))

    return neighboringNodes


def areNodesConnected(node, nextNode):
    row, col = node
    nextRow, nextCol = nextNode

    return


if __name__ == "__main__":
    grid = getGrid()
    print(f"Grid: {grid}")
    startNode = findStartingNode(grid)
    print(f"Starting node: {startNode}")
    print(getNeighboringNodes(startNode))
