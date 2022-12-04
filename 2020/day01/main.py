reader = open("input.txt", "r")
numbers = reader.readlines()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i].rstrip("\n"))

for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        for k in range(j, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == 2020:
                print(numbers[i] * numbers[j] * numbers[k])
                quit()