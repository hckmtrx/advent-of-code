import tools

reader = open(tools.currentdir(__file__) + "input.txt", "r")
data = reader.readlines()

for i in range(len(data)):
    data[i] = data[i].rstrip("\n")

treesVisible = list()

def CheckTree(i: int, j: int, currentTreeHeight: int):
    factors = [0, 0, 0, 0]

    for lookUp in range(i - 1, -1, -1):
        if int(data[lookUp][j]) >= currentTreeHeight or lookUp == 0 or lookUp == len(data) - 1:
            factors[0] = i - lookUp
            break
    for lookDown in range(i + 1, len(data)):
        if int(data[lookDown][j]) >= currentTreeHeight or lookDown == 0 or lookDown == len(data) - 1:
            factors[1] = lookDown - i
            break
    for lookLeft in range(j - 1, -1, -1):
        if int(data[i][lookLeft]) >= currentTreeHeight or lookLeft == 0 or lookLeft == len(data[i]) - 1:
            factors[2] = j - lookLeft
            break
    for lookRight in range(j + 1, len(data[i])):
        if int(data[i][lookRight]) >= currentTreeHeight or lookRight == 0 or lookRight == len(data[i]) - 1:
            factors[3] = lookRight - j
            break

    product = factors[0]
    for i in range(1, len(factors)):
        product *= factors[i]
        
    return product

for i in range(1, len(data)):
    for j in range(1, len(data[i])):
        currentTreeHeight = int(data[i][j])
        treesVisible.append(CheckTree(i, j, currentTreeHeight))

print(max(treesVisible))