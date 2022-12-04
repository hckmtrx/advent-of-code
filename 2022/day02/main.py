import tools 

reader = open(tools.currentdir(__file__) + "input.txt", "r")
data = reader.readlines()
score = 0

def GetPointsBasedOnLetter(letter):
    points = 0
    if letter == "A":
        points += 1
    elif letter == "B":
        points += 2
    elif letter == "C":
        points += 3
    
    return points

def GetPointsBasedOnWin(letter1, letter2):
    points = 0
    
    if letter1 == letter2:
        points += 3
    elif letter1 == "A" and letter2 == "B":
        points += 6
    elif letter1 == "B" and letter2 == "C":
        points += 6
    elif letter1 == "C" and letter2 == "A":
        points += 6
    
    return points

for i in range(len(data)):
    data[i] = data[i].rstrip("\n").split(" ")
    if data[i][-1] == "X":
        if data[i][0] == "A":
            data[i][-1] = "C"
        elif data[i][0] == "B":
            data[i][-1] = "A"
        elif data[i][0] == "C":
            data[i][-1] = "B"
    elif data[i][-1] == "Y":
        data[i][-1] = data[i][0]
    else:
        if data[i][0] == "A":
            data[i][-1] = "B"
        elif data[i][0] == "B":
            data[i][-1] = "C"
        elif data[i][0] == "C":
            data[i][-1] = "A"

    score += GetPointsBasedOnLetter(data[i][-1])
    
    score += GetPointsBasedOnWin(data[i][0], data[i][-1])

print(score)