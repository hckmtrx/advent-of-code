reader = open("input.txt", "r")
numbers = reader.readlines()

def replace(content):
    for i in range(len(content)):
        if content[i] == "-":
            min = int(content[:i])
        elif content[i] == " " and content[i + 2] == ":":
            max = int(content[len(str(min)) + 1:i])
            letter = content[i + 1]
        elif content[i] == " ":
            password = content[i + 1:]
    
    return [min, max, letter, password]

for i in range(len(numbers)):
    numbers[i] = replace(numbers[i].rstrip("\n"))

validPasswords = 0
for number in numbers:
    firstExpr = number[-1][number[0] - 1] == number[2]
    secondExpr = number[-1][number[1] - 1] == number[2]
    if firstExpr or secondExpr:
        if not (firstExpr and secondExpr):
            validPasswords += 1

print(validPasswords)