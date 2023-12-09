# get the histories stored as [[history]]
def getHistories():
    # with open("./9/testHistories.txt", "r") as f:
    with open("./9/histories.txt", "r") as f:
        histories = []
        for historyArr in f.read().split("\n"):
            history = list(map(lambda value: int(value), historyArr.split()))
            histories.append(history)

        return histories


# get the sequences found by getting the difference between numbers above
def getSequences(history):
    sequences = [history]
    sequence = history

    while True:
        nextSequence = []

        for i, value1 in enumerate(sequence):
            # ensure we skip last element
            if i == len(sequence) - 1:
                break

            value2 = sequence[i+1]

            nextSequence.append(value2 - value1)

        sequence = nextSequence
        sequences.append(sequence)

        # if sequence is all 0's we're done
        if sequence.count(0) == len(sequence):
            break

    return sequences


# find the next value of a history
def findNextValue(history):
    sequences = getSequences(history)
    sequencesLength = len(sequences)

    for i, sequence in reversed(list(enumerate(sequences))):
        # add a zero for the last row
        if i == sequencesLength - 1:
            sequence.append(0)
            continue

        n = sequence[-1] + sequences[i + 1][-1]
        sequence.append(n)

    print(sequences)

    return sequences[0][-1]


if __name__ == "__main__":
    histories = getHistories()
    print(f"Histories: {histories}")

    nextValues = [findNextValue(history) for history in histories]
    print(f"Sum of next value: {sum(nextValues)}")
