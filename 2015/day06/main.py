import tools

reader = open(tools.currentdir(__file__) + "input.txt", "r")
data = reader.readlines()
for i in range(len(data)):
    data[i] = data[i].rstrip("\n").split(" ")

matrix = list()
for height in range(1000):
    for width in range(1000):
        matrix.append([height, width, 0])

for instruction in data:
    action = instruction[0]
    curHeight = [int(instruction[1].split(".")[0]), int(instruction[2].split(".")[0])]
    curWidth = [int(instruction[1].split(".")[1]), int(instruction[2].split(".")[1])]
    for height in range(curHeight[0], curHeight[1] + 1):
        for width in range(curWidth[0], curWidth[1] + 1):
            if action == "<>":
                matrix[height * 1000 + width][-1] += 2
            elif action == "on":
                matrix[height * 1000 + width][-1] += 1
            elif action == "off":
                if matrix[height * 1000 + width][-1] > 0:
                    matrix[height * 1000 + width][-1] -= 1

lightLit = 0
for element in matrix:
    lightLit += element[-1]

print(lightLit)