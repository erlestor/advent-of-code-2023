def getContraption():
    with open("./16/contraption_example.txt", "r") as f:
        contraption = f.read().splitlines()
        print(f"Contraption: {contraption}")
        return contraption

directions = {
    "right": (1, 0),
    "left": (-1, 0),
    "down": (0, 1),
    "up": (0, -1)
}

def nextPosition(pos, direction):
    x, y = pos
    offset = directions[direction]
    xOffset, yOffset = offset

    nextX = x + xOffset
    nextY = y + yOffset

    return (nextX, nextY)

"""
Follow beam path
Note which positions have been visited
When splitting use recursion
When we reach a visited position or the end we stop that recursion
"""

def countEnergizedSquares():
    contraption = getContraption()
    visitedSquares = set()

    def followBeam(position, direction):
        x, y = position
        square = contraption[x][y]
        print(square)
        visitedSquares.add((x,y))
        
        # TODO: make seperate function for finding out the next direction/directions
        # empty
        if square == "." or (square == "-" and direction == "right" or direction:
            nextPos = nextPosition(position, direction)
            followBeam(nextPos, direction)
            return
        # mirror
        if square == "\"
    
    followBeam((0,0), "right")


if __name__ == "__main__":
    countEnergizedSquares()