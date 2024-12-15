# %% Part 1

with open("advent_2024/12.txt", "r") as file:
    my_list = [[y for y in x.strip()] for x in file]


unique_letters = set([y for y in "".join(["".join(x) for x in my_list])])

for y in range(len(my_list) - 1, -1, -1):
    for x in range(len(my_list[0]) - 1, -1, -1):
        my_list[y].insert(x, "|")
    my_list[y].append("|")

for y in range(len(my_list) - 1, -1, -1):
    my_list.insert(y, ["-" for _ in my_list[0]])

my_list.append(["-" for x in my_list[0]])

for _ in range(2):
    for y in range(1, len(my_list) - 1):
        my_list[y][0] = "|"
        my_list[y][-1] = "|"
        for x in range(1, len(my_list[0]) - 1):
            if my_list[y][x] == "-":
                if my_list[y - 1][x] == my_list[y + 1][x]:
                    if my_list[y - 1][x] == "|":
                        my_list[y][x] = "|"
                    elif my_list[y - 1][x] == " ":
                        my_list[y][x] = "-"
                    else:
                        my_list[y][x] = " "
            if my_list[y][x] == "|":
                if my_list[y][x - 1] == my_list[y][x + 1]:
                    if my_list[y][x - 1] == "-":
                        my_list[y][x] = "-"
                    elif my_list[y][x - 1] == " ":
                        my_list[y][x] = "|"
                    else:
                        my_list[y][x] = " "

for y in range(1, len(my_list) - 1):
    for x in range(1, len(my_list[0]) - 1):
        if (
            my_list[y][x] in ["-", "|"]
            and my_list[y - 1][x] == " "
            and my_list[y + 1][x] == " "
            and my_list[y][x - 1] == " "
            and my_list[y][x + 1] == " "
        ):
            my_list[y][x] = " "

# for y in my_list:
#     print("".join(y))

# print(unique_letters)

regions = {x: {"cells": [], "regions": [[]], "values": []} for x in unique_letters}

for y in range(len(my_list)):
    for x in range(len(my_list[0])):
        if my_list[y][x] in [" ", "-", "|"]:
            continue

        letter = my_list[y][x]

        if regions[letter]["regions"] == [[]]:
            regions[letter]["regions"][0] += [[y, x]]
        else:
            regions[letter]["cells"] += [[y, x]]

dirs1 = {"n": [-2, 0], "e": [0, 2], "s": [2, 0], "w": [0, -2]}

# print(regions)

for lett in regions:
    while len(regions[lett]["cells"]) > 0:
        for i in range(len(regions[lett]["regions"])):
            added = 0
            for this_loc in regions[lett]["regions"][i]:
                for d in dirs1.values():
                    try:
                        to_check = [this_loc[0] + d[0], this_loc[1] + d[1]]
                    except IndexError:
                        continue
                    if to_check in regions[lett]["cells"]:
                        regions[lett]["regions"][i] += [
                            regions[lett]["cells"].pop(
                                regions[lett]["cells"].index(to_check)
                            )
                        ]
                        added += 1
        if added == 0 and len(regions[lett]["cells"]) > 0:
            regions[lett]["regions"] += [[regions[lett]["cells"].pop(0)]]
    # print(regions["C"])


dirs2 = {"n": [-1, 0], "e": [0, 1], "s": [1, 0], "w": [0, -1]}

total = 0

for lett in regions:
    for r in regions[lett]["regions"]:
        this_len = len(r)
        edges = 0
        for this_loc in r:
            for d in dirs2.values():
                to_check = [this_loc[0] + d[0], this_loc[1] + d[1]]
                if my_list[to_check[0]][to_check[1]] in ["-", "|"]:
                    edges += 1
        regions[lett]["values"] += [[this_len, edges]]

        total += this_len * edges


# for r in regions:
#     print(r, regions[r])

print(total)


# %% Part 2

with open("advent_2024/12.txt", "r") as file:
    my_list = [[y for y in x.strip()] for x in file]


unique_letters = set([y for y in "".join(["".join(x) for x in my_list])])


dirs1 = {"n": [-2, 0], "e": [0, 2], "s": [2, 0], "w": [0, -2]}
dirs2 = {"n": [-1, 0], "e": [0, 1], "s": [1, 0], "w": [0, -1]}
dirs3 = {"ne": [-1, 1], "nw": [-1, -1], "se": [1, 1], "sw": [1, -1]}
ltrs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for y in range(len(my_list) - 1, -1, -1):
    for x in range(len(my_list[0]) - 1, -1, -1):
        my_list[y].insert(x, " ")
    my_list[y].append(" ")

for y in range(len(my_list) - 1, 0, -1):
    my_list.insert(y, [" " for _ in my_list[0]])

my_list.insert(0, ["-" for _ in my_list[0]])
my_list.append(["-" for _ in my_list[0]])

# for _ in range(3):
for y in range(1, len(my_list) - 1):
    my_list[y][0] = "|"
    my_list[y][-1] = "|"
    for x in range(1, len(my_list[0]) - 1):
        if my_list[y][x] == " ":
            n_loc = [y + dirs2["n"][0], x + dirs2["n"][1]]
            s_loc = [y + dirs2["s"][0], x + dirs2["s"][1]]
            e_loc = [y + dirs2["e"][0], x + dirs2["e"][1]]
            w_loc = [y + dirs2["w"][0], x + dirs2["w"][1]]

            if (
                my_list[n_loc[0]][n_loc[1]] in ltrs
                and my_list[n_loc[0]][n_loc[1]] != my_list[s_loc[0]][s_loc[1]]
            ):
                my_list[y][x] = "-"
            elif (
                my_list[w_loc[0]][w_loc[1]] in ltrs
                and my_list[w_loc[0]][w_loc[1]] != my_list[e_loc[0]][e_loc[1]]
            ):
                my_list[y][x] = "|"

for y in range(1, len(my_list) - 1):
    for x in range(1, len(my_list[0]) - 1):
        if (
            my_list[y][x] == " "
            and my_list[y - 1][x] == "|"
            and my_list[y + 1][x] == "|"
            and my_list[y][x - 1] == "-"
            and my_list[y][x + 1] == "-"
        ):
            my_list[y][x] = "+"
        elif (
            my_list[y][x] == " "
            and my_list[y - 1][x] == "|"
            and my_list[y + 1][x] == "|"
        ):
            my_list[y][x] = "|"
        elif (
            my_list[y][x] == " "
            and my_list[y][x - 1] == "-"
            and my_list[y][x + 1] == "-"
        ):
            my_list[y][x] = "-"


# for y in my_list:
#     print("".join(y))

# print(unique_letters)

regions = {
    x: {"cells": [], "regions": [[]], "edges": [], "values": []} for x in unique_letters
}

for y in range(len(my_list)):
    for x in range(len(my_list[0])):
        if my_list[y][x] in [" ", "-", "|", "+"]:
            continue

        letter = my_list[y][x]

        if regions[letter]["regions"] == [[]]:
            regions[letter]["regions"][0] += [[y, x]]
        else:
            regions[letter]["cells"] += [[y, x]]

# print(regions)

for lett in regions:
    while len(regions[lett]["cells"]) > 0:
        for i in range(len(regions[lett]["regions"])):
            added = 0
            for this_loc in regions[lett]["regions"][i]:
                for d in dirs1.values():
                    try:
                        to_check = [this_loc[0] + d[0], this_loc[1] + d[1]]
                    except IndexError:
                        continue
                    if to_check in regions[lett]["cells"]:
                        regions[lett]["regions"][i] += [
                            regions[lett]["cells"].pop(
                                regions[lett]["cells"].index(to_check)
                            )
                        ]
                        added += 1
        if added == 0 and len(regions[lett]["cells"]) > 0:
            regions[lett]["regions"] += [[regions[lett]["cells"].pop(0)]]
    # print(regions["C"])


total = 0

for lett in regions:
    for r in range(len(regions[lett]["regions"])):
        this_len = len(regions[lett]["regions"][r])
        regions[lett]["edges"].append([])
        for this_loc in regions[lett]["regions"][r]:
            for d in dirs2.values():
                to_check = [this_loc[0] + d[0], this_loc[1] + d[1]]
                if my_list[to_check[0]][to_check[1]] in ["-", "|"]:
                    # edges += 1
                    regions[lett]["edges"][r] += [to_check]
        regions[lett]["values"] += [[this_len, 0]]

    # print(lett, regions[lett])

    for r in range(len(regions[lett]["regions"])):
        edges = 0

        for e in regions[lett]["edges"][r]:
            found_dirs = []
            this_edge = my_list[e[0]][e[1]]
            for d in dirs3:
                if this_edge == "|" and (
                    (d in ["ne", "nw"] and ("nw" in found_dirs or "ne" in found_dirs))
                    or (
                        d in ["se", "sw"] and ("sw" in found_dirs or "se" in found_dirs)
                    )
                ):
                    continue
                if this_edge == "-" and (
                    (d in ["ne", "se"] and ("ne" in found_dirs or "se" in found_dirs))
                    or (
                        d in ["nw", "sw"] and ("nw" in found_dirs or "sw" in found_dirs)
                    )
                ):
                    continue
                to_check = [e[0] + dirs3[d][0], e[1] + dirs3[d][1]]
                # print(e, to_check)
                if to_check in regions[lett]["edges"][r]:
                    edges += 0.5
                    found_dirs += [d]

        regions[lett]["values"][r][1] = edges

        total += regions[lett]["values"][r][0] * regions[lett]["values"][r][1]

        # print(lett, regions[lett])


# for r in regions:
#     print(r, regions[r])

print(int(total))
