numChars = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
nums = []
spelledNumbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4", 
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8", 
    "nine": "9",
}

with open("./1/numbers.txt", "r") as file:
    lines = file.readlines()
    
    for line in lines:
        characters = line.removesuffix("\n")
        firstIndex = 100000
        firstChar = ""
        lastIndex = -1
        lastChar = ""

        for numChar in numChars:
            i = line.find(numChar)
            if i != -1 and i < firstIndex:
                firstIndex = i  
                firstChar = numChar

            i = line.rfind(numChar)
            if i != -1 and i > lastIndex:
                lastIndex = i
                lastChar = numChar

        for spelledNumber in spelledNumbers.keys():
            i = line.find(spelledNumber)
            if i != -1 and i < firstIndex:
                firstIndex = i  
                firstChar = spelledNumbers[spelledNumber]

            i = line.rfind(spelledNumber)
            if i != -1 and i > lastIndex:
                lastIndex = i
                lastChar = spelledNumbers[spelledNumber]

        num = int(firstChar + lastChar) 
        nums.append(num)
        
print("Sum of all calibartion values:", sum(nums))