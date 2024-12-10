import numpy as np

# %% Part 1

with open("advent_2024/10.txt", "r") as file:
    my_list = [[int(y) for y in x.strip()] for x in file]

print(np.array(my_list))

dirs = {"n": [-1, 0], "s": [1, 0], "e": [0, 1], "w": [0, -1]}

min_y = 0
min_x = 0
max_y = len(my_list) - 1
max_x = len(my_list[0]) - 1

trails = {}

for y in range(len(my_list)):
    for x in range(len(my_list[0])):
        if my_list[y][x] == 0:
            trails[f"{y},{x}"] = {
                "open_paths": [[[int(y), int(x)]]],
                "complete_paths": [],
            }

print(trails)

for t in trails:
    # if t != "0,2":
    #     continue

    while len(trails[t]["open_paths"]) > 0:
        this_path = trails[t]["open_paths"].pop(0)

        # print(this_path)

        for d in dirs:
            curr = this_path[-1]

            ghost = [curr[0] + dirs[d][0], curr[1] + dirs[d][1]]

            # print(curr, ghost)

            if (
                ghost[0] >= min_y
                and ghost[1] >= min_x
                and ghost[0] <= max_y
                and ghost[1] <= max_x
            ):
                curr_val = my_list[curr[0]][curr[1]]
                ghost_val = my_list[ghost[0]][ghost[1]]

                if ghost_val == curr_val + 1:
                    new_path = this_path + [ghost]
                    if ghost_val == 9:
                        if new_path[-1] not in [
                            x[-1] for x in trails[t]["complete_paths"]
                        ]:
                            trails[t]["complete_paths"] += [new_path]
                    else:
                        trails[t]["open_paths"] += [new_path]

        trails[t]["open_paths"]

print(trails)

compl = sum([len(trails[k]["complete_paths"]) for k in trails])

print(compl)


# %% Part 2

with open("advent_2024/10.txt", "r") as file:
    my_list = [[int(y) for y in x.strip()] for x in file]

print(np.array(my_list))

dirs = {"n": [-1, 0], "s": [1, 0], "e": [0, 1], "w": [0, -1]}

min_y = 0
min_x = 0
max_y = len(my_list) - 1
max_x = len(my_list[0]) - 1

trails = {}

for y in range(len(my_list)):
    for x in range(len(my_list[0])):
        if my_list[y][x] == 0:
            trails[f"{y},{x}"] = {
                "open_paths": [[[int(y), int(x)]]],
                "complete_paths": [],
            }

print(trails)

for t in trails:
    # if t != "0,2":
    #     continue

    while len(trails[t]["open_paths"]) > 0:
        this_path = trails[t]["open_paths"].pop(0)

        # print(this_path)

        for d in dirs:
            curr = this_path[-1]

            ghost = [curr[0] + dirs[d][0], curr[1] + dirs[d][1]]

            # print(curr, ghost)

            if (
                ghost[0] >= min_y
                and ghost[1] >= min_x
                and ghost[0] <= max_y
                and ghost[1] <= max_x
            ):
                curr_val = my_list[curr[0]][curr[1]]
                ghost_val = my_list[ghost[0]][ghost[1]]

                if ghost_val == curr_val + 1:
                    new_path = this_path + [ghost]
                    if ghost_val == 9:
                        trails[t]["complete_paths"] += [new_path]
                    else:
                        trails[t]["open_paths"] += [new_path]

        trails[t]["open_paths"]

print(trails)

compl = sum([len(trails[k]["complete_paths"]) for k in trails])

print(compl)
