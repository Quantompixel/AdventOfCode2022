input_file = open("input/input.txt", mode="r")

result = 0

def list_from_string_range(assignment_range):
    start = int(assignment_range.split("-")[0])
    end = int(assignment_range.split("-")[1])
    return list(range(start, end + 1))


def do_ranges_contain_each_other(range_1, range_2):
    if len(range_1) < len(range_2):
        for task in range_1:
            if not range_2.__contains__(task):
                return False
        return True
    else:
        for task in range_2:
            if not range_1.__contains__(task):
                return False
        return True


for line in input_file.readlines():
    split = line.strip().split(",")
    range_a = list_from_string_range(split[0])
    range_b = list_from_string_range(split[1])

    if do_ranges_contain_each_other(range_a, range_b):
        result += 1

print(result)
