def getSprings():
    with open("./12/springs.txt", "r") as file:
    # with open("./12/springs_example.txt", "r") as file:
        lines = file.read().splitlines()
        return [(line.split()[0], [int(n) for n in line.split()[1].split(",")]) for line in lines]


# lastplacement is the . after the last placement
def getPlacements(spring, group, lastPlacement):
    placements = []

    for i in range(lastPlacement + 1, len(spring) - group + 1):
        c = spring[i]
        # cant place on dots
        if c == ".": 
            continue
        
        # group doesnt fit
        substring = spring[i:i+group]
        if substring.count("?") + substring.count("#") != group:
            continue
        
        # make sure . in front and after
        if i > 0 and spring[i - 1] == "#":
            continue
        if i + group < len(spring) and spring[i + group] == "#":
            continue
        
        placements.append(i)

        # cant be placed later than a # that fits
        if c == "#":
            return placements

    return placements


def placeGroup(spring, group, placement):
    if placement > 0 and placement + group < len(spring):
        return spring[:placement - 1] + "." + "#" * group + "." + spring[placement + group + 1:]
    elif placement > 0:
        return spring[:placement - 1] + "." + "#" * group + spring[placement + group:]
    elif placement + group < len(spring):
        return "#" * group + "." + spring[placement + group + 1:]


""" Ny ide
Tenk på det som et sjakk søk. Finn alle mulige plasseringa for en gruppe
- hvis ingen gyldige plasseringa har vi enten funne en løsning eller ikke
- samme hvis vi har nådd siste gruppe
- ellers: gjenta søk på neste dybde
"""
def getArrangements(spring, groups):
    arrangements = []

    # lastPlacement is the end of the group placement
    def search(spring, groups, i, lastPlacement):
        # when all groups are placed
        # TODO: we are accepting too many arrangements
        if i == len(groups):
            # check if there's unplaced groups
            if lastPlacement + 1 < len(spring) and spring[lastPlacement+1:].find("#") != -1:
                return
            arrangement = spring.replace("?", ".")
            arrangements.append(arrangement)
            return
        
        group = groups[i]
        placements = getPlacements(spring, group, lastPlacement)

        for placement in placements:
            oldSpring = spring
            spring = placeGroup(spring, group, placement)
            search(spring, groups, i + 1, placement + group) 
            spring = oldSpring
    
    search(spring, groups, 0, -1)
        
    print(f"Arrangements: {arrangements}")
    return len(arrangements)


def getTotalArrangements():
    # springs = getSprings()
    springs = [("#.???#????", (1, 3))]
    totalArrangements = 0
    
    for spring, groups in springs:
        totalArrangements += getArrangements(spring, groups)

    return totalArrangements


if __name__ == "__main__":
    totalArrangements = getTotalArrangements()
    print(f"Total arrangements: {totalArrangements}")
    print("2912 < answer < 8592. not [8211]")

