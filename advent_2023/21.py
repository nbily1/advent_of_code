raise Exception("part 2 not solved")

# %% 1

import numpy as np

raw = []

with open("advent_2023/21.txt", "r") as file:
    raw = [[y for y in x.strip()] for x in file if x.strip() != ""]

# print(raw)

active_rows = [y for y in range(len(raw)) if "S" in raw[y]]

# print(active_rows)

moves_to_check = [[1, 0], [-1, 0], [0, 1], [0, -1]]

visited = 1

for i in range(64):
    active_rows += [min(active_rows) - 1]
    active_rows += [max(active_rows) + 1]

    new_active_rows = []
    holder = []
    holder_1 = []

    for y in range(len(raw)):
        if y not in range(min(active_rows), max(active_rows) + 1):
            continue

        for x in range(len(raw[0])):
            if raw[y][x] == ".":
                for m in moves_to_check:
                    check_y = y + m[0]
                    check_x = x + m[1]
                    try:
                        if raw[check_y][check_x] in ["O", "S"]:
                            if [y, x] not in holder:
                                holder += [[y, x]]
                                if y not in new_active_rows:
                                    new_active_rows += [y]
                            if [check_y, check_x] not in holder_1:
                                holder_1 += [[check_y, check_x]]
                    except IndexError:
                        pass

    for h in holder:
        raw[h[0]][h[1]] = "O"
        visited = len(holder)
    for h in holder_1:
        raw[h[0]][h[1]] = "."
    # print(holder, holder_1)

    active_rows = new_active_rows.copy()

# print(np.array(raw))
print(visited)
