import tools

writer = open(tools.currentdir(__file__) + "input2.txt", "w+")
writer.truncate(0)

lookForWires = ["a"]
linesFound = []

reader = open(tools.currentdir(__file__) + "input.txt", "r")
data = reader.readlines()
for i in range(len(data)):
    data[i] = data[i].rstrip("\n").split(" ")

writer = open(tools.currentdir(__file__) + "input2.txt", "a")

def getWire(wire:str, currentLine:int) -> list:
    foundLines = [data[currentLine]]
    for i in range(len(data)):
        currentWires = [j for j in data[i] if not j.isnumeric() and j.islower() and j != "->"]
        for k in range(len(currentWires)):
            if currentWires[k] == wire and i != currentLine:
                foundLines += getWire(currentWires[k], i)
    
    return foundLines

print(getWire("a", 78)); quit()

for i in range(len(data)):
    appendWires = [wires for wires in data[i] if not wires.isnumeric() and wires.islower() and wires != "->"]
    for wire in appendWires:
        if wire in lookForWires:
            getWire(wire, i)
            linesFound += data[i]
            lookForWires += appendWires
            for i in range(len(lookForWires)):
                try:
                    lookForWires.remove(wire)
                except:
                    print(lookForWires)
            tmp = list(map(str, data[i]))
            writer.write(" ".join(tmp) + "\n")
            # test tmp (https://eddmann.com/posts/advent-of-code-2015-day-7-some-assembly-required/)