input_file = open("./input/input.txt", mode="r")

temp_sum = 0
sums = []

for line in input_file.readlines():
    if line.strip().isdecimal():
        temp_sum += int(line.strip())
    else:
        sums.append(temp_sum)
        temp_sum = 0
sums.append(temp_sum)

print(sum(sorted(sums, reverse=True)[0:3]))

