import tools

reader = open(tools.currentdir(__file__) + "input.txt", "r")
data = reader.readlines()
for i in range(len(data)):
    data[i] = data[i].rstrip("\n")

def hasDoubleLetters(doubleLetter, doubleLetterEquality, string, pos1):
    for i in range(len(string) - 1):
        if doubleLetter == string[i:i + 2] and i != pos1:
            return True
    
    return False

niceStrings = 0
for string in data:
    pairOfLetters = 0
    # doubleLetters = [string[i : i + 2] for i in range(0, len(string), 2)]
    for i in range(len(string) - 1):
        if hasDoubleLetters(string[i:i + 2], string[i] == string[i + 1], string, i):
            pairOfLetters += 1
    
    # print(pairOfLetters); quit()

    repeatingLetter = 0
    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            repeatingLetter += 1
    
    if pairOfLetters >= 1 and repeatingLetter >= 1:
        niceStrings += 1
    
print(niceStrings)