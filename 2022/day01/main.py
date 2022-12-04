import tools 

reader = open(tools.currentdir(__file__) + "input.txt", "r")
data = reader.readlines()
calories = list()

for i in range(len(data)):
    data[i] = data[i].rstrip("\n")

value = 0
for i in range(len(data)):
    if data[i].isnumeric():
        value += int(data[i])
    else:
        calories.append(value)
        value = 0

firstElf = max(calories)
calories.remove(firstElf)
secondElf = max(calories)
calories.remove(secondElf)
thirdElf = max(calories)

print(firstElf, secondElf, thirdElf)
print(firstElf + secondElf + thirdElf)