import tools

reader = open(tools.currentdir(__file__) + "input.txt", "r")
data = reader.readline().rstrip("\n")

foundLetters = list()
i = 0
while i < len(data):
    if data[i] not in foundLetters:
        foundLetters.append(data[i])
        if len(foundLetters) == 14:
            print(i + 1)
            quit()
    else:
        foundLetters.pop(0)
        i -= 1
    i += 1