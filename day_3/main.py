input_file = open("input/input.txt", mode="r")
result = 0
group = []


def find_group_duplicates(group):
    items = []
    duplicates = []

    rucksack_1 = group[0]
    rucksack_2 = group[1]
    rucksack_3 = group[2]

    for item in rucksack_1:
        if not items.__contains__(item):
            items.append(item)

    for item in rucksack_2:
        if items.__contains__(item):
            duplicates.append(item)

    for item in rucksack_3:
        if duplicates.__contains__(item):
            return item


def calc_priority(duplicate_item):
    if duplicate_item.islower():
        return ord(duplicate_item) - ord("a") + 1
    else:
        return ord(duplicate_item) - ord("A") + 27


for counter, line in enumerate(input_file.readlines()):
    group.append(list(line.strip()))
    if (counter + 1) % 3 == 0:
        badge = find_group_duplicates(group)
        print(badge, calc_priority(badge))
        result += calc_priority(badge)
        group = []

print(result)
