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

def getComplement(binary):
    binary = ["0" for irgendwas in range(len(binary), 16)] + list(binary)
    outcome = ""
    for bit in binary:
        outcome += "1" if bit == "0" else "0"

    return int("0b" + outcome, 2)

wiresFound = 0

i = 0
while wiresFound < len(data):
    destinationWire = getValue(data[i][-1], dest=True)

    if len(data[i]) == 3:
        operation = "ASSIGN"
        wire1 = int(data[i][0]) if data[i][0].isnumeric() else getValue(data[i][0])
    elif len(data[i]) == 4:
        operation = data[i][0]
        wire1 = getValue(data[i][1])
    else:
        wire1 = int(data[i][0]) if data[i][0].isnumeric() else getValue(data[i][0])
        operation = data[i][1]
        wire2 = int(data[i][2]) if data[i][2].isnumeric() else getValue(data[i][2])

    if wire1 == 0 or wire2 == 0:
        operation = "undefined"

    if operation == "ASSIGN":
        wires[destinationWire][1] = wire1
        wiresFound += 1
    elif operation == "NOT":
        wires[destinationWire][1] = getComplement(bin(wire1)[2:])
        wiresFound += 1
    elif operation == "AND":
        wires[destinationWire][1] = wire1 & wire2
        wiresFound += 1
    elif operation == "OR":
        wires[destinationWire][1] = wire1 | wire2
        wiresFound += 1
    elif operation == "RSHIFT":
        wires[destinationWire][1] = wire1 >> wire2
        wiresFound += 1
    elif operation == "LSHIFT":
        wires[destinationWire][1] = wire1 << wire2
        wiresFound += 1
    
    if i == len(data) - 1:
        i = 0
    else:
        i += 1