input_file = open("input/input.txt", mode="r")
result = 0


def calc_priority(duplicate_item):
    if duplicate_item.islower():
        return ord(duplicate_item) - ord("a") + 1
    else:
        return ord(duplicate_item) - ord("A") + 27


for line in input_file.readlines():
    items = list(line)[:len(line) - 1]
    first_half = items[:len(items) // 2]
    second_half = items[len(items) // 2: len(items)]

    for item in first_half:
        if second_half.__contains__(item):
            print(item, calc_priority(item))
            result += calc_priority(item)
            break

print(result)
