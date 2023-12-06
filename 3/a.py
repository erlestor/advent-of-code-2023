import uuid

# finn symbolan
nums = "0123456789"

def isSymbol(c):
    return c not in nums and c != "."

def isNumber(c):
    return c in nums

def getGrid():
    with open("./3/engine.txt", "r") as f:
    # with open("./3/engine_test.txt", "r") as f:
        return f.read().split("\n")

def getNumbers(grid):
    numbers = []
    width = len(grid[0])

    # finn alle tall med start og slutt index
    for row in range(len(grid)):
        n = ""

        for col in range(len(grid[0])):
            c = grid[row][col]

            if isNumber(c):
                n += c
                # hvis tall e sist på rekka. legg d te
                if col == width - 1:
                    numbers.append({
                        "id": uuid.uuid1(),
                        "row": row,
                        "startCol": col - len(n) + 1,
                        "endCol": col,
                        "value": int(n)
                    })
            else:
                if len(n) > 0:
                    numbers.append({
                        "id": uuid.uuid1(),
                        "row": row,
                        "startCol": col - len(n),
                        "endCol": col - 1,
                        "value": int(n)
                    })
                n = ""
    return numbers
            
# iterer gjennom numbers og finn ut om dem har adjacent symbols
# deretter filtrer for d og summe

def isPart(grid, number):
    _, row, startCol, endCol, _ = number.values()
    width = len(grid[0])
    height = len(grid)

    # check above
    if row > 0:
        start = startCol - 1 if startCol > 0 else startCol
        end = endCol + 1 if endCol < width - 1 else endCol

        for col in range(start, end + 1):
            if isSymbol(grid[row - 1][col]):
                return True

    # check below
    if row < height - 1:
        start = startCol - 1 if startCol > 0 else startCol
        end = endCol + 1 if endCol < width - 1 else endCol

        for col in range(start, end + 1):
            if isSymbol(grid[row + 1][col]):
                return True

    # check left
    if startCol > 0:
        if isSymbol(grid[row][startCol - 1]):
            return True
    # check right
    if endCol < width - 1:
        if isSymbol(grid[row][endCol + 1]):
            return True

    return False
    
def getParts(grid, numbers):
    return list(filter(lambda number: isPart(grid, number), numbers))

if __name__ == "__main__":
    grid = getGrid()
    numbers = getNumbers(grid)
    parts = getParts(grid, numbers)
    print(parts)
    partNumbers = list(map(lambda part: part["value"], parts))
    sumOfPartNumbers = sum(partNumbers)

    print("Sum of parts:", sumOfPartNumbers)

    