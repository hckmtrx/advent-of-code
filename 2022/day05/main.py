import tools

reader = open(tools.currentdir(__file__) + "input.txt", "r")
data = reader.readlines()
for i in range(len(data)):
    data[i] = data[i].rstrip("\n")

crates = list()

i = 0
while data[i] != "":
    crates.append(list(data[i]))
    i += 1

data = data[i + 1:]
for i in range(len(data)):
    data[i] = data[i].split(" ")

for i in range(len(data)):
    cratesFrom = int(data[i][1]) - 1
    cratesTo = int(data[i][2]) - 1
    cratesToMove = crates[cratesFrom][-int(data[i][0]):]
    # cratesToMove.reverse()

    crates[cratesTo] += cratesToMove
    crates[cratesFrom] = crates[cratesFrom][:-len(cratesToMove)]

for i in range(len(crates)):
    print(crates[i][-1], end="")