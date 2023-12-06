def something():
    copies = []

    # with open("./4/cards_test.txt", "r") as f:
    with open("./4/cards.txt", "r") as f:
        cards = f.read().split("\n")

        for i in range(len(cards)):
            copies.append(1)

        for card in cards:
            winningNumbers = card.split(": ")[1].split(" | ")[0].split()
            yourNumbers = card.split(": ")[1].split(" | ")[1].split()
            gameNumber = int(card.split(": ")[0].split()[1])
            # print("Game", gameNumber, ": ", winningNumbers, " | ", yourNumbers)
            
            matchingNumbers = len(list(filter(lambda n: n in winningNumbers, yourNumbers)))
            
            for i in range(gameNumber, gameNumber + matchingNumbers):
                copies[i] += copies[gameNumber - 1]
            
    return sum(copies)
            

if __name__ == "__main__":
    print("Total points", something())