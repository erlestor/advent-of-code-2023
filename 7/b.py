from functools import cmp_to_key

cardValues = {
    "J": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "Q": 11,
    "K": 12,
    "A": 13
}

def getCardValue(card):
    return cardValues[card]


def getHands():
    with open("./7/hands.txt", "r") as f:
    # with open("./7/testHands.txt", "r") as f:
        return [(hand.split()[0], int(hand.split()[1])) for hand in f.read().split("\n")]


# input: hand = "ATQ44"
# output: te [1, 1, 1, 2]
# occurences of each card except joker
def numberOfOccurences(hand):
    occurences = {}

    for card in hand:
        if card == "J":
            continue
        if card in occurences.keys():
            occurences[card] += 1
        else:
            occurences[card] = 1

    return list(occurences.values())


# takes in a hand and gives a score. used for comparing hands
# output: hand = "ATQ49"
# input: int (the higher the better hand)
def getHandScore(hand):
    cardOccurences = numberOfOccurences(hand)
    highestOccurence = max(cardOccurences) if len(cardOccurences) > 0 else 0
    jokerCount = hand.count("J")

    # five of a kind
    if highestOccurence + jokerCount == 5:
        return 6
    # four of a kind
    if highestOccurence + jokerCount == 4:
        return 5
    # full house
    # problem: AAJ21 telle som fullt hus no
    if (highestOccurence == 3 and 2 in cardOccurences) or (highestOccurence + jokerCount == 3 and cardOccurences.count(2) == 2):
        return 4
    # three of a kind
    if highestOccurence + jokerCount == 3:
        return 3
    # two pair
    if cardOccurences.count(2) == 2:
        return 2
    # one pair
    if highestOccurence + jokerCount == 2:
        return 1
    return 0
    

# hand1/2 = (hand, bid)
# output: positive int if hand1 is better, negative if hand2
def compareHands(hand1, hand2):
    # gi en score typan hender. hvis begge hands har samme score. sammenlign høyeste kort
    score1 = getHandScore(hand1[0])
    score2 = getHandScore(hand2[0])
    
    if score1 != score2:
        return score1 - score2
    
    # compare each card until one is higher
    for i in range(5):
        value1 = getCardValue(hand1[0][i])       
        value2 = getCardValue(hand2[0][i])       

        if value1 != value2:
            return value1 - value2
    
    return 0

def getRankedHands(hands):
    return sorted(hands, key=cmp_to_key(compareHands))

# input: hands = (hand, bid) in order of their rank
def getTotalWinnings(hands):
    totalWinnings = 0

    for i in range(len(hands)):
        _, bid = hands[i]
        totalWinnings += bid * (i + 1)
        
    return totalWinnings


# ranke alle hands
# finn winnings av hver rank
# mappe over hands og finn total winnings
if __name__ == "__main__":
    hands = getHands()
    print("Hands:", hands)

    rankedHands = getRankedHands(hands)
    print("Ranked hands:", rankedHands)

    if len(hands) < 50:
        print("Expected winnings:", 5905)
    else:
        print("Previous answer (too low):", 249032195)
        
    totalWinnings = getTotalWinnings(rankedHands)
    print("Total winnings:", totalWinnings)

    # print(getHandScore(""))