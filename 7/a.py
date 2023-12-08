from functools import cmp_to_key

cardValues = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}

def getCardValue(card):
    return cardValues[card]


def getHands():
    # with open("./7/hands.txt", "r") as f:
    with open("./7/testHands.txt", "r") as f:
        return [(hand.split()[0], int(hand.split()[1])) for hand in f.read().split("\n")]


# input: hand = "ATQ44"
# output: te [1, 1, 1, 2]
def numberOfOccurences(hand):
    occurences = {}

    for card in hand:
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
    highestOccurence = max(cardOccurences)
    # five of a kind
    if highestOccurence == 5:
        return 6
    # four of a kind
    elif highestOccurence == 4:
        return 5
    # full house
    elif highestOccurence == 3 and 2 in cardOccurences:
        return 4
    # three of a kind
    elif highestOccurence == 3:
        return 3
    # two pair
    elif cardOccurences.count(2) == 2:
        return 2
    # one pair
    elif highestOccurence == 2:
        return 1
    return 0
    

# hand1/2 = (hand, bid)
# output: positive int if hand1 is better, negative if hand2
def compareHands(hand1, hand2):
    # gi en score typan hender. hvis begge hands har samme score. sammenlign høyeste kort
    score1 = getHandScore(hand1[0])
    score2 = getHandScore(hand2[0])
    
    if score1 != score2:
        return score2 - score1
    
    # compare each card until one is higher
    for i in range(5):
        value1 = getCardValue(hand1[0][i])       
        value2 = getCardValue(hand2[0][i])       

        if value1 != value2:
            return value2 - value1
    
    return 0

def getRankedHands(hands):
    return sorted(hands, key=cmp_to_key(compareHands), reverse=True)

# input: hands = (hand, bid) in order of their rank
def getTotalWinnings(hands):
    totalWinnings = 0

    for i in range(len(hands)):
        _, bid = hands[i]

        totalWinnings += bid * (i + 1)
    
    return totalWinnings


# ranke alle hands og lagre som (hand, bid, rank)
# finn winnings av hver rank
# mappe over hands og finn total winnings
if __name__ == "__main__":
    hands = getHands()
    print("Hands:", hands)
    rankedHands = getRankedHands(hands)
    print("Ranked hands:", rankedHands)
    totalWinnings = getTotalWinnings(rankedHands)
    print("Total winnings:", totalWinnings)