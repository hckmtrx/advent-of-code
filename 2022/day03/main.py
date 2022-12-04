import tools
from string import ascii_lowercase, ascii_uppercase 

LETTERS = list(ascii_lowercase) + list(ascii_uppercase)

reader = open(tools.currentdir(__file__) + "input.txt", "r")
data = reader.readlines()

def GetSameLetters(item1: list, item2: list, item3:list, returnLetterPos: bool = False):
    for i in range(len(LETTERS)):
        if LETTERS[i] in item1 and LETTERS[i] in item2 and LETTERS[i] in item3:
            return i + 1 if returnLetterPos else True

for i in range(len(data)):
    data[i] = data[i].rstrip("\n")

i = 0
while i < len(data):
    data[i] = [data[i], data[i + 1], data[i + 2]]
    i += 3

i = 0
while i < len(data):
    if isinstance(data[i], str):
        data.pop(i)
    else:
        i += 1

for i in range(len(data)):
    if GetSameLetters(data[i][0], data[i][1], data[i][2]):
        data[i] = GetSameLetters(data[i][0], data[i][1], data[i][2], True)

print(sum(data))