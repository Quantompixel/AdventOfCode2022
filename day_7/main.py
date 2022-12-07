input_file = open("input/input.txt", mode="r")
lines = input_file.readlines()

path = []
directories = {}

for index, line in enumerate(lines):
    if line.startswith("$"):
        args = line.split(" ")
        command = args[1].strip()

        if command.__contains__("cd"):
            directory = args[2].strip()

            if directory.__contains__(".."):
                path.pop()
            else:
                directories.update({directory: 0})
                path.append(directory)
    else:
        if not line.startswith("dir"):
            file_size = int(line.split(" ")[0])
            print("--", path[-1], file_size)

            for i in range(1, len(path) + 1):
                directories[path[-i]] += file_size

result = 0
print(directories)

for key in directories:
    if directories[key] <= 100000:
        result += directories[key]

print(result)