def getSequence():
    # with open("./15/input_example.txt", "r") as f:
    with open("./15/input.txt", "r") as f:
        sequence = []
        lines = f.read().split(",")
        for string in lines:
            focusLength = None

            if "=" in string:
                label = string.split("=")[0]
                operator = "="
                focusLength = int(string.split("=")[1])
            else:
                label = string.split("-")[0]
                operator = "-"
            
            sequence.append((label, operator, focusLength))
        return sequence


def hash(label):
    currentValue = 0

    for char in label:
        ascii = ord(char)
        currentValue += ascii
        currentValue *= 17
        currentValue %= 256

    return currentValue


def findLens(box, label):
    for index, lens in enumerate(box):
        if lens[0] == label:
            return index

    return -1


def setupLenses(sequence):
    boxes = {}

    for instruction in sequence:
        label, operator, focusLength = instruction
        boxNum = str(hash(label))

        if boxNum not in boxes.keys():
            boxes[boxNum] = []

        box = boxes[boxNum]
        lensIdx = findLens(box, label)

        # remove
        if operator == "-":
            if lensIdx == -1:
                continue

            box.pop(lensIdx)
            if len(box) == 0:
                boxes.pop(boxNum)
            continue

        # add
        if lensIdx == -1:
            box.append((label, focusLength))
            continue

        # replace lens
        box[lensIdx] = (label, focusLength)

    return boxes


def focusPower(boxes):
    focusPower = 0

    for boxNum, box in boxes.items():
        boxNum = int(boxNum) + 1

        for slot, lens in enumerate(box):
            slot += 1
            _, focusLength = lens

            focusPower += boxNum * slot * focusLength

    return focusPower


if __name__ == "__main__":
    sequence = getSequence()
    print(f"Sequence: {sequence}")
    boxes = setupLenses(sequence)
    print(f"Boxes: {boxes}")
    totalFocusPower = focusPower(boxes)
    print(f"Focus power: {totalFocusPower}")
