directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

# get offsets for the 2 connected nodes given a symbol
offsetsGivenSymbol = {
    "|": (directions["up"], directions["down"]),
    "-": (directions["left"], directions["right"]),
    "L": (directions["up"], directions["right"]),
    "J": (directions["up"], directions["left"]),
    "7": (directions["down"], directions["left"]),
    "F": (directions["down"], directions["right"]),
}

type Grid = list[str]
type Node = tuple[int, int]


def addTuples(tuple1: tuple[int, int], tuple2: tuple[int, int]):
    return (tuple1[0] + tuple2[0]), (tuple1[1] + tuple2[1])


def setGridValue(grid: Grid, node: Node, value: str):
    row, col = node
    grid[row] = grid[row][:col] + value + grid[row][col + 1:]


def getGrid():
    with open("./10/sketch.txt", "r") as f:
    # with open("./10/testSketch2.txt", "r") as f:
    # with open("./10/testSketch3.txt", "r") as f:
        return f.read().split("\n")


def findStartingNode(grid: Grid):
    for rowIdx, row in enumerate(grid):
        colIdx = row.find("S")
        if colIdx != -1:
            return rowIdx, colIdx

    raise Exception("No starting node was found")


def getNeighboringNodes(grid: Grid, node: Node):
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
def areNodesConnected(grid: Grid, startNode: Node, nextNode: Node):
    nextRow, nextCol = nextNode
    offsets = offsetsGivenSymbol[grid[nextRow][nextCol]]

    for offset in offsets:
        if addTuples(nextNode, offset) == startNode:
            return True

    return False


# select a node from the start to start looping bby
# gets the first valid node to from the start
def getSecondNodeFromStart(grid: Grid, startNode: Node):
    neighboringNodes = getNeighboringNodes(grid, startNode)

    for node in neighboringNodes:
        if areNodesConnected(grid, startNode, node):
            return node

    raise Exception("No next node")


def getNextNode(grid: Grid, node: Node, previousNode: Node):
    row, col = node
    nodeSymbol = grid[row][col]
    offsets = offsetsGivenSymbol[nodeSymbol]

    for offset in offsets:
        nextNode = addTuples(node, offset)
        nextRow, nextCol = nextNode
        nextNodeSymbol = grid[nextRow][nextCol]

        if nextNode != previousNode and nextNodeSymbol != ".":
            return nextNode
    
    raise Exception("No next node was found")


def getLoop(grid: Grid, startNode: Node, secondNode: Node):
    loop = [startNode, secondNode]
    node = secondNode
    previousNode = startNode

    while node != startNode:
        nextNode = getNextNode(grid, node, previousNode)
        loop.append(nextNode)
        previousNode = node
        node = nextNode

    return loop[:-1:]


def cleanJunk(grid: Grid, loop: list[Node]):
    height = len(grid)
    width = len(grid[0])
    cleanGrid = ["." * width for i in range(height)]

    firstRow = len(grid) + 10
    lastRow = 0
    
    for node in loop:
        row, col = node
        nodeValue = grid[row][col]
        setGridValue(cleanGrid, node, nodeValue)

        if row < firstRow:
            firstRow = row
        if row > lastRow:
            lastRow = row
    
    # cut off the empty lines before and after loop
    return cleanGrid[firstRow:lastRow + 1:]


def replaceStartValue(grid: Grid):
    startNode = findStartingNode(grid)
    # find the 2 connected neighboring pipes
    neighbours = getNeighboringNodes(grid, startNode)
    neighbours = list(filter(lambda neighbor: areNodesConnected(grid, startNode, neighbor), neighbours))
    for value, offsets in offsetsGivenSymbol.items():
        # if the offsets give us the neighbors, we found the symbol
        if addTuples(startNode, offsets[0]) in neighbours and addTuples(startNode, offsets[1]) in neighbours:
            setGridValue(grid, startNode, value)


# loop through each row
# count the number loop tiles
# if we are on a . and loop tiles is odd then its enclosed
# scuffed implementation of the even-odd rule
def countEnclosedTiles(grid: Grid):
    enclosedTiles = 0

    corners = "LJ7F"
    correspondingCorners = {
        "F": "7",
        "L": "J"
    }

    for rowIdx, row in enumerate(grid):
        passedEdges = 0
        previousCorner = None

        for colIdx, nodeValue in enumerate(row):
            # guaranteeed passing of edge
            if nodeValue == "|":
                passedEdges += 1
                continue
            
            if nodeValue in corners:
                # if no previous corner just store it as the new previous
                if previousCorner is None:
                    previousCorner = nodeValue
                    continue
                # didnt pass edge
                # print(row)
                if correspondingCorners[previousCorner] == nodeValue:
                    previousCorner = None
                    continue
                # passed edge
                previousCorner = None
                passedEdges += 1
                continue
            
            # even-odd rule for polygons
            if nodeValue == "." and passedEdges % 2 == 1:
                setGridValue(grid, (rowIdx, colIdx), "1")
                enclosedTiles += 1
                
    return enclosedTiles


# starting node blir erstatta som feil type
if __name__ == "__main__":
    grid = getGrid()
    # print(f"Grid: {grid}")
    startNode = findStartingNode(grid)
    secondNode = getSecondNodeFromStart(grid, startNode)
    loop = getLoop(grid, startNode, secondNode)

    cleanGrid = cleanJunk(grid, loop)

    replaceStartValue(cleanGrid)

    enclosedTiles = countEnclosedTiles(cleanGrid)
    print(f"Processed grid: {cleanGrid}")
    print(f"Enclosed tiles: {enclosedTiles}")
    print("Expected: 563")