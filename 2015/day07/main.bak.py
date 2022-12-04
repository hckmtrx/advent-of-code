import tools
from string import ascii_lowercase

reader = open(tools.currentdir(__file__) + "input.txt", "r")
data = reader.readlines()
for i in range(len(data)):
    data[i] = data[i].rstrip("\n").split(" ")

wires = list()
for letter in ascii_lowercase:
    wires.append([letter, 0])

for letter1 in ascii_lowercase:
    for letter2 in ascii_lowercase:
        wires.append([letter1 + letter2, 0])

def getValue(wire, dest = False):
    for element in range(len(wires)):
        if wires[element][0] == wire:
            return int(element) if dest else int(wires[element][1])

for i in range(len(data)):
    destinationWire = getValue(data[i][-1], dest=True)

    if len(data[i]) == 3:
        wires[destinationWire][1] = int(data[i][0]) if data[i][0].isnumeric() else getValue(data[i][0])
    elif len(data[i]) == 4:
        operation = data[i][0]
        wire1 = getValue(data[i][1])
    else:
        wire1 = int(data[i][0]) if data[i][0].isnumeric() else getValue(data[i][0])
        operation = data[i][1]
        wire2 = int(data[i][2]) if data[i][2].isnumeric() else getValue(data[i][2])

    if operation == "AND":
        wires[destinationWire][1] = wire1 & wire2
    elif operation == "OR":
        wires[destinationWire][1] = wire1 | wire2
    elif operation == "RSHIFT":
        wires[destinationWire][1] = wire1 >> wire2
    elif operation == "LSHIFT":
        wires[destinationWire][1] = wire1 << wire2

    # print(wires[1])