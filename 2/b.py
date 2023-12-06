sumOfPowers = 0

with open("./2/games.txt", "r") as file:
    games = file.readlines()
    
    for gameStr in games:
        game = gameStr.removesuffix("\n")
        maxRed = 0
        maxGreen = 0
        maxBlue = 0

        rounds = game.split(": ")[1].split("; ")

        for round in rounds:
            entries = round.split(", ")

            # entry = "3 blue"
            for entry in entries:
                n = int(entry.split(" ")[0])
                color = entry.split(" ")[1]

                if color == "red" and n > maxRed:
                    maxRed = n
                elif color == "green" and n > maxGreen:
                    maxGreen = n
                elif color == "blue" and n > maxBlue:
                    maxBlue = n
            
        sumOfPowers += maxRed * maxGreen * maxBlue

print("Sum of all powers:", sumOfPowers)