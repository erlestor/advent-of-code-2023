with open("./5/map.txt", "r") as f:
# with open("./5/testMap.txt", "r") as f:
    almanac = f.read()
    values = [int(x) for x in almanac.split("\n")[0].split(":")[1].split()]
    print("Values:", values)

    # gå igjennom map for map
    # finn ranges
    # regn ut nye verdia
    # når ingen flere maps. finn laveste verdi

    maps = almanac.split("\n\n")[1::]
    for mappa in maps:
        ranges = []
        for line in mappa.split("\n")[1::]:
            destinationStart, sourceStart, rangeLength = [int(x) for x in line.split()]
            ranges.append({"destinationStart": destinationStart, "sourceStart": sourceStart, "rangeLength": rangeLength})
        
        print("Ranges:", ranges)
        for i, value in enumerate(values):
            inRange = False

            for range in ranges:
                destinationStart, sourceStart, rangeLength = range.values()
                sourceEnd = sourceStart + rangeLength - 1

                if value >= sourceStart and value <= sourceEnd:
                    values[i] = value + destinationStart - sourceStart
                    inRange = True
    
    # done going through maps
    print("Lowest location number", min(values))


    
    