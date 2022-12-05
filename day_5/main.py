import re

# stacks = [
    # ["Z", "N"],
    # ["M", "C", "D"],
    # ["P"],
# ]

stacks = [
    ["S", "M", "R", "N", "W", "J", "V", "T"],
    ["B", "W", "D", "J", "Q", "P", "C", "V"],
    ["B", "J", "F", "H", "D", "R", "P"],
    ["F", "R", "P", "B", "M", "N", "D"],
    ["H", "V", "R", "P", "T", "B"],
    ["C", "B", "P", "T"],
    ["B", "J", "R", "P", "L"],
    ["N", "C", "S", "L", "T", "Z", "B", "W"],
    ["L", "S", "G"]
]

input_file = open("input/input.txt", mode="r")

for line in input_file.readlines():
    data = re.findall("[0-9]+", line)
    moves = int(data[0])
    move_from = int(data[1])
    move_to = int(data[2])
    print(moves, move_from, move_to)

    for i in range(moves):
        stacks[move_to - 1].append(stacks[move_from - 1].pop())

for stack in stacks:
    print(stack.pop(), end="")
