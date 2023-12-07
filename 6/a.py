def getRaces():
    with open("./6/races.txt", "r") as f:
        lines = f.read().split("\n")

    times = [int(time) for time in lines[0].split()[1::]]
    distances = [int(distance) for distance in lines[1].split()[1::]]
    
    races = []
    for i in range(len(times)):
        races.append((times[i], distances[i]))
    
    return races

def numberOfWaysToWinRace(race):
    # race: (time, distance)
    time, distance = race
    waysToWin = 0

    for secondsHeld in range(time + 1):
        # m / s
       speed = secondsHeld
       timeLeft = time - secondsHeld
       distanceTraveled = speed * timeLeft
       
       if distanceTraveled > distance:
           waysToWin += 1
    
    return waysToWin
        

if __name__ == "__main__":
    races = getRaces()
    print(races)

    numberOfWaysToWinRaces = [numberOfWaysToWinRace(race) for race in races]
    result = 1
    for n in numberOfWaysToWinRaces:
        result *= n
    
    print("Result:", result)