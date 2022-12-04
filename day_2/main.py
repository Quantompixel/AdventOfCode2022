input_file = open("./input/input.txt", mode="r");


def calculate_score(player_a, player_b):
    if player_a == 'A':
        if player_b == 'X':
            return 4
        elif player_b == 'Y':
            return 8
        elif player_b == 'Z':
            return 3
    elif player_a == 'B':
        if player_b == 'X':
            return 1
        elif player_b == 'Y':
            return 5
        elif player_b == 'Z':
            return 9
    elif player_a == 'C':
        if player_b == 'X':
            return 7
        elif player_b == 'Y':
            return 2
        elif player_b == 'Z':
            return 6


def create_response(player_a, player_b):
    if player_b == 'X':
        if player_a == 'A':
            return calculate_score(player_a, 'Z')
        elif player_a == 'B':
            return calculate_score(player_a, 'X')
        elif player_a == 'C':
            return calculate_score(player_a, 'Y')
    elif player_b == 'Y':
        if player_a == 'A':
            return calculate_score(player_a, 'X')
        elif player_a == 'B':
            return calculate_score(player_a, 'Y')
        elif player_a == 'C':
            return calculate_score(player_a, 'Z')
    elif player_b == 'Z':
        if player_a == 'A':
            return calculate_score(player_a, 'Y')
        elif player_a == 'B':
            return calculate_score(player_a, 'Z')
        elif player_a == 'C':
            return calculate_score(player_a, 'X')


sum = 0

for line in input_file.readlines():
    split = line.split(" ")
    sum += create_response(split[0].strip(), split[1].strip())

print(sum)
