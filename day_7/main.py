input_file = open("input/input.txt", mode="r")
lines = input_file.readlines()

path = []
directories = {}

for index, line in enumerate(lines):
    if line.startswith("$"):
        args = line.split(" ")
        command = args[1].strip()

        if command.__contains__("ls"):
            print("ls")
            counter = 1

            while True:
                if index + counter >= len(lines):
                    break
                elif lines[index + counter].startswith("$"):
                    break

                content = lines[index + counter]

                if not content.startswith("dir"):
                    file_size = int(content.split(" ")[0])
                    print("--", path[-1], file_size)
                    # directories[path[-1]] = directories[path[-1]] + int(file_size)
                    directories[path[-1]] += file_size
                counter += 1

        if command.__contains__("cd"):
            directory = args[2].strip()

            if directory.__contains__(".."):
                path.pop()
            else:
                directories.update({directory: 0})
                path.append(directory)

print(directories)
