input_file = open("input/input.txt", mode="r")
lines = input_file.readlines()

path = []
directories = {}


def path_to_string(path_array):
    path_string = ""
    for element in path_array:
        path_string += element

    return path_string


for index, line in enumerate(lines):
    if line.startswith("$"):
        args = line.split(" ")
        command = args[1].strip()

        if command.__contains__("cd"):
            directory = args[2].strip()

            if directory.__contains__(".."):
                path.pop()
            else:
                path.append(directory)
                directories.update({path_to_string(path): 0})
    else:
        if not line.startswith("dir"):
            file_size = int(line.split(" ")[0])

            for i in range(len(path)):
                key = path_to_string(path[0:i + 1])
                directories[key] += file_size

result = 0
print(directories)

space_to_free_up = 30_000_000 - (70_000_000 - directories["/"])
smallest_dir = 70_000_000

for key in directories:
    directory = directories[key]
    if directory > space_to_free_up:
        if directory < smallest_dir:
            smallest_dir = directory

print(smallest_dir)
