# %% Part 1

with open("advent_2024/04.txt", "r") as file:
    my_list = [[y for y in x.strip()] for x in file]

# print(my_list)

my_dict = {}

dirs = {
    "r": [[0, 1], [0, 2], [0, 3]],
    "rd": [[1, 1], [2, 2], [3, 3]],
    "d": [[1, 0], [2, 0], [3, 0]],
    "ld": [[1, -1], [2, -2], [3, -3]],
    "l": [[0, -1], [0, -2], [0, -3]],
    "lu": [[-1, -1], [-2, -2], [-3, -3]],
    "u": [[-1, 0], [-2, 0], [-3, 0]],
    "ru": [[-1, 1], [-2, 2], [-3, 3]],
}

counter = 0

for x in range(len(my_list)):
    for y in range(len(my_list[0])):
        if my_list[x][y] != "X":
            continue

        for d in dirs:
            plus_1 = dirs[d][0]
            plus_2 = dirs[d][1]
            plus_3 = dirs[d][2]

            if x + plus_3[0] < 0 or y + plus_3[1] < 0:
                continue

            try:
                third = my_list[x + plus_3[0]][y + plus_3[1]]
            except IndexError:
                continue

            second = my_list[x + plus_2[0]][y + plus_2[1]]

            first = my_list[x + plus_1[0]][y + plus_1[1]]

            if first + second + third == "MAS":
                counter += 1

print(counter)

# %% Part 2

with open("advent_2024/04.txt", "r") as file:
    my_list = [[y for y in x.strip()] for x in file]

# print(my_list)

my_dict = {}

dirs = {
    "rd": [[1, 1], [-1, -1]],
    "ld": [[1, -1], [-1, 1]],
}

counter = 0
keep = []

for x in range(len(my_list)):
    for y in range(len(my_list[0])):
        if my_list[x][y] != "A":
            continue

        tracker = 0

        for d in dirs:
            plus_1 = dirs[d][0]
            plus_2 = dirs[d][1]

            if (x + plus_2[0] < 0 or y + plus_2[1] < 0) or (
                x + plus_1[0] < 0 or y + plus_1[1] < 0
            ):
                continue

            try:
                second = my_list[x + plus_2[0]][y + plus_2[1]]
                first = my_list[x + plus_1[0]][y + plus_1[1]]
            except IndexError:
                continue

            if first + second in ["MS", "SM"]:
                tracker += 1
                if tracker == 2:
                    counter += 1

print(counter)
