import numpy as np
from copy import deepcopy

# %% Part 1

with open("advent_2024/06.txt", "r") as file:
    my_list = [[y for y in x.strip()] for x in file]

print(my_list)

for y in range(len(my_list)):
    for x in range(len(my_list[0])):
        if my_list[y][x] == "^":
            g_pos = [y, x, "u"]
            break

print(g_pos)

out_list = my_list.copy()

dir_list = ["u", "r", "d", "l"]
dirs = {"u": [-1, 0], "r": [0, 1], "d": [1, 0], "l": [0, -1]}

still_in = True

while still_in:
    dir = g_pos[2]
    my_list[g_pos[0]][g_pos[1]] = "X"

    next_pos = [g_pos[0] + dirs[dir][0], g_pos[1] + dirs[dir][1]]
    # print(next_pos)

    try:
        if my_list[next_pos[0]][next_pos[1]] != "#":
            g_pos[0] = next_pos[0]
            g_pos[1] = next_pos[1]
            continue
        else:
            g_pos[2] = dir_list[(dir_list.index(dir) + 1) % len(dir_list)]
            continue
    except IndexError:
        break

print(np.array(my_list))

visited = 0
for y in my_list:
    for x in y:
        if x == "X":
            visited += 1
print(visited)

# %% Part 2

with open("advent_2024/06.txt", "r") as file:
    my_list = [[y for y in x.strip()] for x in file]

print(my_list)

for y in range(len(my_list)):
    for x in range(len(my_list[0])):
        if my_list[y][x] == "^":
            g_pos = [y, x, "u"]
            g_pos1 = [y, x, "u"]
            break

print(g_pos)

dir_list = ["u", "r", "d", "l"]
dirs = {"u": [-1, 0], "r": [0, 1], "d": [1, 0], "l": [0, -1]}

still_in = True

while still_in:
    dir = g_pos[2]
    my_list[g_pos[0]][g_pos[1]] = {"X": []}

    next_pos = [g_pos[0] + dirs[dir][0], g_pos[1] + dirs[dir][1]]
    # print(next_pos)

    try:
        if my_list[next_pos[0]][next_pos[1]] != "#":
            g_pos[0] = next_pos[0]
            g_pos[1] = next_pos[1]
            continue
        else:
            g_pos[2] = dir_list[(dir_list.index(dir) + 1) % len(dir_list)]
            continue
    except IndexError:
        break

# to_check = [
#     [[y, x] for x in range(len(my_list[0])) if my_list[y][x] == {"X": []}]
#     for y in range(len(my_list))
# ]

to_check = []
for y in range(len(my_list)):
    for x in range(len(my_list)):
        if my_list[y][x] == {"X": []} and (y != g_pos1[0] or x != g_pos1[1]):
            to_check += [[y, x]]

# to_check = [x for x in to_check if x not in [[], [g_pos1[0], g_pos1[1]]]]

# print(np.array(my_list))

print(to_check)
# quit()

loopy = []

# to_check = [[7, 7]]

for c in to_check:
    my_list_copy = deepcopy(my_list)
    my_list_copy[c[0]][c[1]] = "#"
    g_pos2 = g_pos1.copy()

    still_in = True

    while still_in:
        dir = g_pos2[2]
        if my_list_copy[g_pos2[0]][g_pos2[1]] == ".":
            my_list_copy[g_pos2[0]][g_pos2[1]] = {"X": [dir]}
        elif dir in my_list_copy[g_pos2[0]][g_pos2[1]]["X"]:
            # print(dir, my_list_copy[g_pos2[0]][g_pos2[1]], g_pos2)
            loopy += [c]
            break
        else:
            my_list_copy[g_pos2[0]][g_pos2[1]]["X"] += [dir]

        next_pos = [g_pos2[0] + dirs[dir][0], g_pos2[1] + dirs[dir][1]]
        # print(next_pos)

        try:
            if next_pos[0] < 0 or next_pos[1] < 0:
                break
            elif my_list_copy[next_pos[0]][next_pos[1]] != "#":
                g_pos2[0] = next_pos[0]
                g_pos2[1] = next_pos[1]
                continue
            else:
                g_pos2[2] = dir_list[(dir_list.index(dir) + 1) % len(dir_list)]
                continue
        except IndexError:
            break

    # print(np.array(my_list_copy))

    # visited = 0
    # for y in my_list_copy:
    #     for x in y:
    #         if x == "X":
    #             visited += 1
    # print(visited)

print(loopy)
print(len(loopy))
