import tools

reader = open(tools.currentdir(__file__) + "input.txt", "r")
data = reader.readline()

houses = ["0.0"]
housesSanta = ["0.0"]
housesRobo = ["0.0"]
housesVisited = 1

for house in range(len(data)):
    verticalChange = 0; horizontalChange = 0
    if data[house] == "^":
        verticalChange = 1
    elif data[house] == "v":
        verticalChange = -1
    elif data[house] == ">":
        horizontalChange = 1
    elif data[house] == "<":
        horizontalChange = -1

    if house % 2 == 0:
        newCoordinatesSanta = str(int(str(housesSanta[-1]).split(".")[0]) + verticalChange) + "." + str(int(str(housesSanta[-1]).split(".")[1]) + horizontalChange)
        if newCoordinatesSanta not in houses:
            houses.append(newCoordinatesSanta)
            housesVisited += 1
        housesSanta.append(newCoordinatesSanta)

    else:
        newCoordinatesRobo = str(int(str(housesRobo[-1]).split(".")[0]) + verticalChange) + "." + str(int(str(housesRobo[-1]).split(".")[1]) + horizontalChange)
        if newCoordinatesRobo not in houses:
            houses.append(newCoordinatesRobo)
            housesVisited += 1
        housesRobo.append(newCoordinatesRobo)

print(housesVisited)