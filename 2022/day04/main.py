import tools

def Contains(list1: list, list2: list) -> bool:
    for item1 in list1:
        if item1 in list2:
            return True
    return False

reader = open(tools.currentdir(__file__) + "input.txt", "r")
data = reader.readlines()

assignmentPairs = 0
for i in range(len(data)):
    data[i] = data[i].rstrip("\n").split(",")
    data[i] = [data[i][0].split("-"), data[i][1].split("-")]
    data[i][0] = list(range(int(data[i][0][0]), int(data[i][0][1]) + 1))
    data[i][1] = list(range(int(data[i][1][0]), int(data[i][1][1]) + 1))
    if Contains(data[i][0], data[i][1]):
        assignmentPairs += 1

print(assignmentPairs)