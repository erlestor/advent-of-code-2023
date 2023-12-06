from a import *

gear = "*"

def getGearCandidates(grid):
    gearCandidates = []

    # finn alle gir med start og slutt index
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            c = grid[row][col]

            if c == gear:
                gearCandidates.append({
                    "row": row,
                    "col": col,
                })

    return gearCandidates

def getPartNumbers(parts):
    return list(map(lambda part: part["value"], parts))
                
def partExists(part, parts):
    return part["id"] in list(map(lambda p: p["id"], parts))

def addPartAtPosition(row, col, parts, adjacentParts):
    for part in parts:
       if row == part["row"] and col >= part["startCol"] and col <= part["endCol"]:
            if not partExists(part, adjacentParts):
                adjacentParts.append(part)


# input: the gear {row, col}, parts and grid
# finds the adjacent parts
# returns gear ratio if there are 2 parts
# else returns 0
def getGearRatio(gear, parts, grid):
    gearRow, gearCol = gear.values()
    adjacentParts = []
    height = len(grid)
    width = len(grid[0])

    # check above
    if gearRow > 0:
        start = gearCol - 1 if gearCol > 0 else gearCol
        end = gearCol + 1 if gearCol < width - 1 else gearCol

        for col in range(start, end + 1):
            addPartAtPosition(gearRow - 1, col, parts, adjacentParts)

    # check below
    if gearRow < height - 1:
        start = gearCol - 1 if gearCol > 0 else gearCol
        end = gearCol + 1 if gearCol < width - 1 else gearCol

        for col in range(start, end + 1):
            addPartAtPosition(gearRow + 1, col, parts, adjacentParts)

    # check left
    if gearCol > 0:
        print(gearRow, gearCol)
        addPartAtPosition(gearRow, gearCol - 1, parts, adjacentParts)

    # check right
    if gearCol < width - 1:
        addPartAtPosition(gearRow, gearCol + 1, parts, adjacentParts)

    print(getPartNumbers(adjacentParts))
    if len(adjacentParts) == 2:
        return adjacentParts[0]["value"] * adjacentParts[1]["value"]
    return 0
        
if __name__ == "__main__":
    grid = getGrid()
    numbers = getNumbers(grid)
    parts = getParts(grid, numbers)
    gears = getGearCandidates(grid)
    gearRatios = list(map(lambda gear: getGearRatio(gear, parts, grid), gears))
    sumOfGearRatios = sum(gearRatios)
    print("Sum of gear ratios:", sumOfGearRatios)