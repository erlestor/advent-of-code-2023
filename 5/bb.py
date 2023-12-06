# Her e problemet som æ se det
# Ranges kan overlapp med flere mapRanges. Derfor må æ kun flytt over dem tallan som overlappe. 
# Og behold de som ikke overlapp for å sjekke med dem neste mapRangan

with open("./5/map.txt", "r") as f:
# with open("./5/testMap.txt", "r") as f:
    almanac = f.read()

numbers = [int(x) for x in almanac.split("\n")[0].split(":")[1].split()]
maps = almanac.split("\n\n")[1::]
seedRanges = []

for i in range(0, len(numbers), 2):
    start = numbers[i]
    length = numbers[i+1]
    end = start + length - 1
    seedRanges.append((start, end))
    
print("Original seed ranges:", seedRanges)

for mappa in maps:
    # find the mapping ranges
    mapRanges = []
    for line in mappa.split("\n")[1::]:
        destinationStart, sourceStart, rangeLength = (int(x) for x in line.split())
        sourceEnd = sourceStart + rangeLength - 1
        rangeDiff = destinationStart - sourceStart
        mapRanges.append((destinationStart, sourceStart, sourceEnd, rangeDiff))
        
    translatedRanges = []

    # translate the seed ranges
    i = 0
    while i < len(seedRanges):
        start, end = seedRanges[i]

        for mapRange in mapRanges:
            destinationStart, sourceStart, sourceEnd, rangeDiff = mapRange

            # if overlapping
            if (start <= sourceEnd and start >= sourceStart) or (end <= sourceEnd and end >= sourceStart):
                seedRanges.pop(i)
                i -= 1

                if start < sourceStart:
                    seedRanges.append((start, sourceStart - 1))
                if end > sourceEnd:
                    seedRanges.append((sourceEnd + 1, end))  

                translatedRanges.append((max(start, sourceStart) + rangeDiff, min(end, sourceEnd) + rangeDiff))
                break

        i += 1
        
    seedRanges = seedRanges + translatedRanges
    print(seedRanges)

lowestValues = [range[0] for range in seedRanges]

print("Lowest location number", min(lowestValues))


    
    