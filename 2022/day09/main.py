import tools

reader = open(tools.currentdir(__file__) + "input.txt", "r")
data = reader.readlines()

for i in range(len(data)):
    data[i] = data[i].rstrip("\n").split(" ")
    data[i][1] = int(data[i][1])

headPosition = [0, 0]

tailPosition = []
for i in range(9):
    tailPosition.append([0, 0])

visitedPositions = [[0, 0]]

def UpdateTailPosition(currentPos: list, leadingPos: list) -> list:
    tailPosX = currentPos[0]
    tailPosY = currentPos[1]

    if [tailPosX - 2, tailPosY - 2] == leadingPos or [tailPosX - 1, tailPosY - 2] == leadingPos or [tailPosX - 2, tailPosY - 1] == leadingPos:
        return [tailPosX - 1, tailPosY - 1]
    elif [tailPosX, tailPosY - 2] == leadingPos:
        return [tailPosX, tailPosY - 1]
    elif [tailPosX + 1, tailPosY - 2] == leadingPos or [tailPosX + 2, tailPosY - 2] == leadingPos or [tailPosX + 2, tailPosY - 1] == leadingPos:
        return [tailPosX + 1, tailPosY - 1]
    elif [tailPosX + 2, tailPosY] == leadingPos:
        return [tailPosX + 1, tailPosY]
    elif [tailPosX + 1, tailPosY + 2] == leadingPos or [tailPosX + 2, tailPosY + 2] == leadingPos or [tailPosX + 2, tailPosY + 1] == leadingPos:
        return [tailPosX + 1, tailPosY + 1]
    elif [tailPosX, tailPosY + 2] == leadingPos:
        return [tailPosX, tailPosY + 1]
    elif [tailPosX - 1, tailPosY + 2] == leadingPos or [tailPosX - 2, tailPosY + 2] == leadingPos or [tailPosX - 2, tailPosY + 1] == leadingPos:
        return [tailPosX - 1, tailPosY + 1]
    elif [tailPosX - 2, tailPosY] == leadingPos:
        return [tailPosX - 1, tailPosY]
    
    return currentPos

for i in range(len(data)):
    vertical = data[i][0] == "U" or data[i][0] == "D"
    direction = -1 if data[i][0] == "U" or data[i][0] == "L" else 1
    
    for j in range(data[i][1]):
        if vertical:
            headPosition[1] += direction
        else:
            headPosition[0] += direction

        for k in range(len(tailPosition)):
            tailPosition[k] = UpdateTailPosition(tailPosition[k], headPosition if k == 0 else tailPosition[k - 1])

        if tailPosition[8] not in visitedPositions:
            visitedPositions.append(tailPosition[8])

print(len(visitedPositions))