# Her e problemet som æ se det
# Ranges kan overlapp med flere mapRanges. Derfor må æ kun flytt over dem tallan som overlappe. 
# Og behold de som ikke overlapp for å sjekke med dem neste mapRangan

# with open("./5/map.txt", "r") as f:
with open("./5/testMap.txt", "r") as f:
    almanac = f.read()

numbers = [int(x) for x in almanac.split("\n")[0].split(":")[1].split()]
ranges = []

for i in range(0, len(numbers), 2):
    start = numbers[i]
    length = numbers[i+1]
    end = start + length - 1
    ranges.append((start, end))
    
print("Original Ranges:", ranges)

maps = almanac.split("\n\n")[1::]
for mappa in maps:
    # find the ranges to be mapped
    mapRanges = []
    for line in mappa.split("\n")[1::]:
        destinationStart, sourceStart, rangeLength = (int(x) for x in line.split())
        sourceEnd = sourceStart + rangeLength - 1
        rangeDiff = destinationStart - sourceStart
        mapRanges.append((destinationStart, sourceStart, sourceEnd, rangeDiff))
    
    # gå mapRange for mapRange
    # flytt range som e i range te newRange
    # behold gamle range i oldRange

    oldRanges = ranges.copy()
    newRanges = []

    i = 0
    rangesLength = len(oldRanges)

    while i < rangesLength:
        start, end = oldRanges[i]
        rangeTranslated = False

        for mapRange in mapRanges:
            destinationStart, sourceStart, sourceEnd, rangeDiff = mapRange

            # if overlapping
            if (start <= sourceEnd and start >= sourceStart) or (end <= sourceEnd and end >= sourceStart):
                if start < sourceStart:
                    oldRanges.append((start, sourceEnd - 1))
                    rangesLength += 1
                if end > sourceEnd:
                    oldRanges.append((sourceEnd + 1, end))  
                    rangesLength += 1

                newRanges.append((max(start, sourceStart) + rangeDiff, min(end, sourceEnd) + rangeDiff))
                rangeTranslated = True
                break

        # if it doesnt overlap at all just add it
        if not rangeTranslated:
            newRanges.append([start, end])
        
        i += 1
        
    ranges = list(set([tuple(newRange) for newRange in newRanges]))
    print(ranges)

lowestValues = [range[0] for range in ranges]

print("Lowest location number", min(lowestValues))


    
    