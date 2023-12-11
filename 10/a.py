directionOffsets = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

# get offsets for the 2 connected nodes given a symbol
offsetsGivenSymbol = {
    # (row, col)
    "|": (directionOffsets["up"], directionOffsets["down"]), # up, down
    "-": (directionOffsets["left"], directionOffsets["right"]), # left, right
    "L": (directionOffsets["up"], directionOffsets["right"]), # up, right
    "J": (directionOffsets["up"], directionOffsets["left"]), # up, left
    "7": (directionOffsets["down"], directionOffsets["left"]), # down, left
    "F": (directionOffsets["down"], directionOffsets["right"]), # down, right
}

def getGrid():
    # with open("./10/testSketch.txt", "r") as f:
    with open("./10/sketch.txt", "r") as f:
        return f.read().split("\n")

def findStartingNode(grid: list[str]):
    for rowIdx, row in enumerate(grid):
        for colIdx, node in enumerate(row):
            if node == "S":
                return rowIdx, colIdx

    raise Exception("No starting node")

# find the neighboring nodes
# node = (row, col)
def getNeighboringNodes(grid, node):
    row, col = node
    neighboringNodes = []

    # left
    if row > 0 and grid[row - 1][col] != ".":
        neighboringNodes.append((row - 1, col))
    # right
    if row < len(grid[row]) - 1 and grid[row + 1][col] != ".":
        neighboringNodes.append((row + 1, col))
    # up
    if col > 0 and grid[row][col - 1] != ".":
        neighboringNodes.append((row, col - 1))
    # down
    if col < len(grid) - 1 and grid[row][col + 1] != ".":
        neighboringNodes.append((row, col + 1))

    return neighboringNodes

# only for start nodes since we don't know the symbol underneath S
# get the symbol of the next node
# see if one of the offsets matches our start node
# if so. they are connected, return true
def areNodesConnected(grid, startNode, nextNode):
    startRow, startCol = startNode
    nextRow, nextCol = nextNode
    offsets = offsetsGivenSymbol[grid[nextRow][nextCol]]

    for offset in offsets:
        offsetRow, offsetCol = offset
        if nextRow + offsetRow == startRow and nextCol + offsetCol == startCol:
            return True

    return False

# select a node from the start to start looping bby
# gets the first valid node to from the start
def getSecondNodeFromStart(grid, startNode):
    neighboringNodes = getNeighboringNodes(grid, startNode)

    for node in neighboringNodes:
        if areNodesConnected(grid, startNode, node):
            return node

    raise Exception("No next node")

def getNextNode(grid, node, previousNode):
    row, col = node
    nodeSymbol = grid[row][col]
    offsets = offsetsGivenSymbol[nodeSymbol]

    for offset in offsets:
        offsetRow, offsetCol = offset

        nextNode = (row + offsetRow, col + offsetCol)
        nextNodeSymbol = grid[nextNode[0]][nextNode[1]]

        if nextNode != previousNode and nextNodeSymbol != ".":
            return nextNode
    
    raise Exception("No next node was found")

def getLoop():
    grid = getGrid()
    print(f"Grid: {grid}")
    startNode = findStartingNode(grid)
    print(f"Starting node: {startNode}")
    secondNode = getSecondNodeFromStart(grid, startNode)
    print(f"Second node: {secondNode}")

    loop = [startNode, secondNode]
    print(loop)
    node = secondNode
    previousNode = startNode

    while node != startNode:
        # find the next node
        # add it to the loop
        nextNode = getNextNode(grid, node, previousNode)
        loop.append(nextNode)
        previousNode = node
        node = nextNode

    return loop[:-1:]

def getFarthestDistance():
    loop = getLoop()
    return len(loop) // 2

if __name__ == "__main__":
    print(f"Farthest distance: {getFarthestDistance()}")