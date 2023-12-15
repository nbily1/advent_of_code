# %% 1

raw = []

with open("advent_2023/14.txt", "r") as file:
    raw = [[y for y in x.strip()] for x in file if x.strip() != ""]


print(raw)

for y in range(1, len(raw)):
    for x in range(len(raw[0])):
        curr_coord = [y, x]
        curr_y = y
        curr_x = x
        # print(curr_coord, raw[curr_y][curr_x])
        if raw[curr_y][curr_x] == "O":
            # print("help")
            stopped = False
            while stopped != True:
                new_coord = [curr_y - 1, curr_x]
                new_y = curr_y - 1
                new_x = curr_x
                # print("\t", new_coord, raw[new_y][new_x])
                if new_y >= 0 and raw[new_y][new_x] == ".":
                    raw[curr_y][curr_x] = "."
                    raw[new_y][new_x] = "O"
                    curr_coord = new_coord.copy()
                    curr_x = new_x
                    curr_y = new_y
                    # print(new_coord)
                else:
                    stopped = True

print(raw)

mult = len(raw)
row_sums = []

for y in raw:
    row_sums += [len([x for x in y if x in ["O"]]) * mult]
    mult -= 1

print(row_sums)
print(sum(row_sums))

# %% 2
from functools import cache

import numpy as np

raw = []

with open("advent_2023/14.txt", "r") as file:
    raw = [[y for y in x.strip()] for x in file if x.strip() != ""]


# print(raw)

raw = f"{raw}"


@cache
def tilt(inp: str, dir: str):
    inp = eval(inp)
    y_range = range(len(inp))
    x_range = range(len(inp[0]))

    if dir == "u":
        to_move = [-1, 0]
    elif dir == "d":
        to_move = [1, 0]
        y_range = range(len(inp) - 1, -1, -1)
    elif dir == "r":
        to_move = [0, 1]
        x_range = range(len(inp[0]) - 1, -1, -1)
    elif dir == "l":
        to_move = [0, -1]

    # print(inp)

    for y in y_range:
        for x in x_range:
            # curr_coord = [y, x]
            curr_y = y
            curr_x = x
            # print(curr_coord, inp[curr_y][curr_x])
            if inp[curr_y][curr_x] == "O":
                # print("help")
                stopped = False
                while stopped != True:
                    new_coord = [curr_y + to_move[0], curr_x + to_move[1]]
                    new_y = curr_y + to_move[0]
                    new_x = curr_x + to_move[1]
                    # print("\t", new_coord, inp[new_y][new_x])
                    if (
                        new_y >= 0
                        and new_x >= 0
                        and new_y < len(inp)
                        and new_x < len(inp[0])
                        and inp[new_y][new_x] == "."
                    ):
                        inp[curr_y][curr_x] = "."
                        inp[new_y][new_x] = "O"
                        # curr_coord = new_coord.copy()
                        curr_x = new_x
                        curr_y = new_y
                        # print(new_coord)
                    else:
                        stopped = True
    # print("\n", np.array(inp))
    return f"{inp}"


dirs = ["u", "l", "d", "r"]

for i in range(1000000000):
    for d in dirs:
        raw = tilt(raw, d)
    if i % 10000000 == 0:
        print("Finished cycle:", i)

raw = eval(f"{raw}")
print(np.array(raw))

mult = len(raw)
row_sums = []

for y in raw:
    row_sums += [len([x for x in y if x in ["O"]]) * mult]
    mult -= 1

print(row_sums)
print(sum(row_sums))
