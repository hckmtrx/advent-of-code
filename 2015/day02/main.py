reader = open(r"day2\input.txt", "r")
input = reader.readlines()

ribbonLength = 0

for i in range(len(input)):
    input[i] = input[i].replace("\n", "").split("x")
    for a in range(len(input[i])):
        input[i][a] = int(input[i][a])
    input[i].sort()

for content in input:
    ribbonLength += 2 * (content[0] + content[1]) + content[0] * content[1] * content[2]

print(ribbonLength)