def getRace():
    with open("./6/races.txt", "r") as f:
    # with open("./6/testRaces.txt", "r") as f:
        lines = f.read().split("\n")

    time = int("".join(lines[0].split()[1::]))
    distance = int("".join(lines[1].split()[1::]))
    
    return (time, distance)

def numberOfWaysToWinRace(race):
    # race: (time, distance)
    time, distance = race
    waysToWin = 0

    # x = secondsHeld
    # distance traveled: f(secondsHeld) = secondsHeld * (time - secondsHeld)
    # deriverte f'(secondsHeld) = time - 2 * secondsHeld

    for secondsHeld in range(time + 1):
        # m / s
       speed = secondsHeld
       timeLeft = time - secondsHeld
       distanceTraveled = speed * timeLeft
       
       if distanceTraveled > distance:
           waysToWin += 1
    
    return waysToWin
        

if __name__ == "__main__":
    race = getRace()
    print("Race:", race)

    result = numberOfWaysToWinRace(race)
    print("Result:", result)