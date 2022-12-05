import re

stacks_s = [
    ["Z", "N"],
    ["M", "C", "D"],
    ["P"],
]

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
    move_from = int(data[1]) - 1
    move_to = int(data[2]) - 1
    move_from_arr = stacks[move_from]
    move_to_arr = stacks[move_to]

    crates_to_be_moved = move_from_arr[len(move_from_arr) - moves: len(move_from_arr)]
    move_from_arr = move_from_arr[0: len(move_from_arr) - moves]
    move_to_arr = move_to_arr + crates_to_be_moved

    stacks[move_from] = move_from_arr
    stacks[move_to] = move_to_arr

    print(stacks)

for stack in stacks:
    print(stack.pop(), end="")
