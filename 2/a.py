maxRed = 12
maxGreen = 13
maxBlue = 14
gameIds = []

with open("./2/games.txt", "r") as file:
    games = file.readlines()
    
    for gameStr in games:
        game = gameStr.removesuffix("\n")
        possible = True

        gameId = int(game.split(": ")[0].split(" ")[1])
        rounds = game.split(": ")[1].split("; ")

        for round in rounds:
            entries = round.split(", ")

            # entry = "3 blue"
            for entry in entries:
                n = int(entry.split(" ")[0])
                color = entry.split(" ")[1]

                if color == "red" and n > maxRed:
                    possible = False
                    break
                elif color == "green" and n > maxGreen:
                    possible = False
                    break
                elif color == "blue" and n > maxBlue:
                    possible = False
                    break
            
        if possible:
            gameIds.append(gameId)

sum = sum(gameIds)
print("Sum of all game ids:", sum)