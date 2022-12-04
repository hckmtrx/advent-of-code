reader = open("input.txt", "r")
input = reader.readline()

floor = 0
for bracket in range(len(input)):
    if input[bracket] == "(":
        floor += 1
    else:
        floor -= 1
    if floor < 0:
        print(bracket + 1)

print(floor)