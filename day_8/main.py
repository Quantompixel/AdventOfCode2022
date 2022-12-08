input_file = open("input/input.txt")

tree_map = []


def look_up(walk_row, walk_column, size):
    if walk_row - 1 < 0:
        return True

    if tree_map[walk_row - 1][walk_column] >= size:
        return False

    return look_up(walk_row - 1, walk_column, size)


def look_down(walk_row, walk_column, size):
    if walk_row + 1 >= len(tree_map):
        return True
    elif tree_map[walk_row + 1][walk_column] >= size:
        return False
    else:
        return look_down(walk_row + 1, walk_column, size)


def look_left(walk_row, walk_column, size):
    if walk_column - 1 < 0:
        return True

    if tree_map[walk_row][walk_column - 1] >= size:
        return False

    return look_left(walk_row, walk_column - 1, size)


def look_right(walk_row, walk_column, size):
    if walk_column + 1 > len(tree_map[walk_row]) - 1:
        return True

    if tree_map[walk_row][walk_column + 1] >= size:
        return False

    return look_right(walk_row, walk_column + 1, size)


for line in input_file:
    int_list = list(map(lambda tree: int(tree), list(line.strip())))
    tree_map.append(int_list)

counter = 0

for row in range(len(tree_map)):
    for column in range(len(tree_map[row])):
        if look_up(row, column, tree_map[row][column]):
            counter += 1
        elif look_right(row, column, tree_map[row][column]):
            counter += 1
        elif look_down(row, column, tree_map[row][column]):
            counter += 1
        elif look_left(row, column, tree_map[row][column]):
            counter += 1
        else:
            print("not visible", row, column)

print(counter)
