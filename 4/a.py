def something():
    totalPoints = 0

    # with open("./4/cards_test.txt", "r") as f:
    with open("./4/cards.txt", "r") as f:
        cards = f.read().split("\n")
        for card in cards:
            winningNumbers = list(filter(lambda x: len(x) > 0, card.split(": ")[1].split(" | ")[0].split(" ")))
            yourNumbers = list(filter(lambda x: len(x) > 0, card.split(": ")[1].split(" | ")[1].split(" ")))
            print(winningNumbers, " | ", yourNumbers)
            points = 0

            for yourNumber in yourNumbers:
                if yourNumber in winningNumbers:
                    if points == 0:
                        points = 1
                    else:
                        points *= 2
            
            totalPoints += points

    return totalPoints
            

if __name__ == "__main__":
    print("Total points", something())