def getSprings():
    with open("./12/springs_example.txt", "r") as file:
        lines = file.read().splitlines()
        return [(line.split()[0], [int(n) for n in line.split()[1].split(",")]) for line in lines]


def getArrangements(spring, groups):
    print(f"Spring: {spring}, Groups: {groups}" )
    arrangements = []
    arrangement = spring

    for group in groups:
        # could loop through placements instead
        for i, c in enumerate(arrangement):
            # if not a valid placement
            if c != "?": 
                continue
            
            # if group doesnt fit or it would be too long
            # TODO: doesnt work if group is at the very end
            substring = arrangement[i:i+group]
            if substring.count("?") + substring.count("#") != group or arrangement[i + group] == "#":
                continue
            
            print("huh")

            arrangement = arrangement[:i] + "#" * group + "." + arrangement[i + group + 1:]
            arrangements.append(arrangement)
            break
        
        # if no valid placement found
        
    print(f"Arrangements: {arrangements}")
    return len(arrangements)


def getTotalArrangements():
    springs = getSprings()[1:2]
    totalArrangements = 0
    
    for spring, groups in springs:
        totalArrangements += getArrangements(spring, groups)

    return totalArrangements


if __name__ == "__main__":
    print(f"Springs: {getSprings()}")
    getTotalArrangements()


""" Ny ide
Tenk på det som et sjakk søk. Finn alle mulige plasseringa for en gruppe
- hvis ingen gyldige plasseringa har vi enten funne en løsning eller ikke
- samme hvis vi har nådd siste gruppe
- ellers: gjenta søk på neste dybde
"""