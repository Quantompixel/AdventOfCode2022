input_file = open("input/input.txt")

tree_map = []


def look_up(walk_row, walk_column, size, score=0):
    if walk_row - 1 < 0:
        return score

    if tree_map[walk_row - 1][walk_column] >= size:
        return score + 1

    return look_up(walk_row - 1, walk_column, size, score + 1)


def look_down(walk_row, walk_column, size, score=0):
    if walk_row + 1 >= len(tree_map):
        return score
    elif tree_map[walk_row + 1][walk_column] >= size:
        return score + 1
    else:
        return look_down(walk_row + 1, walk_column, size, score + 1)


def look_left(walk_row, walk_column, size, score=0):
    if walk_column - 1 < 0:
        return score

    if tree_map[walk_row][walk_column - 1] >= size:
        return score + 1

    return look_left(walk_row, walk_column - 1, size, score + 1)


def look_right(walk_row, walk_column, size, score=0):
    if walk_column + 1 > len(tree_map[walk_row]) - 1:
        return score
    if tree_map[walk_row][walk_column + 1] >= size:
        return score + 1

    return look_right(walk_row, walk_column + 1, size, score + 1)


for line in input_file:
    int_list = list(map(lambda tree: int(tree), list(line.strip())))
    tree_map.append(int_list)

highest = 0

for row in range(len(tree_map)):
    for column in range(len(tree_map[row])):
        up = look_up(row, column, tree_map[row][column])
        down = look_down(row, column, tree_map[row][column])
        right = look_right(row, column, tree_map[row][column])
        left = look_left(row, column, tree_map[row][column])

        if up * down * right * left > highest:
            highest = up * down * right * left

print(highest)
