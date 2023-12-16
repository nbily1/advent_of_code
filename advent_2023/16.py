# %% 1

raw = []

with open("advent_2023/16.txt", "r") as file:
    raw = [[y for y in x.strip()] for x in file if x.strip() != ""]

# print(raw)

used_tiles = {"0,0": {"coord": [0, 0], "dirs": ["d"]}}

active_beams = ["0,0:d"]

dirs = {"u": [-1, 0], "d": [1, 0], "r": [0, 1], "l": [0, -1]}

# print(used_tiles)


def check_if_used(coord: list, dir: str):
    global used_tiles
    if f"{coord[0]},{coord[1]}" in used_tiles:
        if dir in used_tiles[f"{coord[0]},{coord[1]}"]["dirs"]:
            return True
        else:
            used_tiles[f"{coord[0]},{coord[1]}"]["dirs"] += [dir]
    else:
        used_tiles[f"{coord[0]},{coord[1]}"] = {
            "coord": [coord[0], coord[1]],
            "dirs": [dir],
        }
    return False


while len(active_beams) > 0:
    new_active = []
    for ab in active_beams:
        coord = [int(x) for x in ab.split(":")[0].split(",")]
        dir = ab.split(":")[1]
        this_move = dirs[dir]

        new_coord = [coord[0] + this_move[0], coord[1] + this_move[1]]
        new_y = new_coord[0]
        new_x = new_coord[1]

        if new_y not in range(len(raw)) or new_x not in range(len(raw[0])):
            continue
        elif raw[new_y][new_x] == ".":
            if check_if_used(new_coord, dir) == False:
                new_active += [f"{new_y},{new_x}:{dir}"]
        elif raw[new_y][new_x] == "\\":
            if check_if_used(new_coord, dir) == False:
                if dir == "r":
                    new_active += [f"{new_y},{new_x}:d"]
                if dir == "l":
                    new_active += [f"{new_y},{new_x}:u"]
                if dir == "u":
                    new_active += [f"{new_y},{new_x}:l"]
                if dir == "d":
                    new_active += [f"{new_y},{new_x}:r"]
        elif raw[new_y][new_x] == "/":
            if check_if_used(new_coord, dir) == False:
                if dir == "r":
                    new_active += [f"{new_y},{new_x}:u"]
                if dir == "l":
                    new_active += [f"{new_y},{new_x}:d"]
                if dir == "u":
                    new_active += [f"{new_y},{new_x}:r"]
                if dir == "d":
                    new_active += [f"{new_y},{new_x}:l"]
        elif raw[new_y][new_x] == "|":
            if check_if_used(new_coord, dir) == False:
                if dir in ["r", "l"]:
                    new_active += [f"{new_y},{new_x}:d"]
                    new_active += [f"{new_y},{new_x}:u"]
                if dir in ["u", "d"]:
                    new_active += [f"{new_y},{new_x}:{dir}"]
        elif raw[new_y][new_x] == "-":
            if check_if_used(new_coord, dir) == False:
                if dir in ["u", "d"]:
                    new_active += [f"{new_y},{new_x}:r"]
                    new_active += [f"{new_y},{new_x}:l"]
                if dir in ["r", "l"]:
                    new_active += [f"{new_y},{new_x}:{dir}"]
    active_beams = new_active.copy()
    # break

    # print(active_beams)

# print(used_tiles)
# print([k for k in used_tiles])
print(len(used_tiles))

# checker = [["." for x in y] for y in raw]

# for y in range(len(raw)):
#     for x in range(len(raw[0])):
#         if f"{y},{x}" in used_tiles:
#             checker[y][x] = "#"

# import numpy as np

# print(np.array(checker))


# %% 2

raw = []

with open("advent_2023/16.txt", "r") as file:
    raw = [[y for y in x.strip()] for x in file if x.strip() != ""]

# print(raw)

dirs = {"u": [-1, 0], "d": [1, 0], "r": [0, 1], "l": [0, -1]}

starting_pos = [f"0,{x}:d" for x in range(len(raw[0]))]
starting_pos += [f"{len(raw)-1},{x}:u" for x in range(len(raw[0]))]
starting_pos += [f"{x},0:r" for x in range(len(raw))]
starting_pos += [f"{x},{len(raw[0])-1}:l" for x in range(len(raw))]

activated = []

for s in starting_pos:
    used_tiles = {
        s.split(":")[0]: {
            "coord": [int(x) for x in s.split(":")[0].split(",")],
            "dirs": [s.split(":")[1]],
        }
    }

    active_beams = [s]

    # print(used_tiles)

    def check_if_used(coord: list, dir: str):
        global used_tiles
        if f"{coord[0]},{coord[1]}" in used_tiles:
            if dir in used_tiles[f"{coord[0]},{coord[1]}"]["dirs"]:
                return True
            else:
                used_tiles[f"{coord[0]},{coord[1]}"]["dirs"] += [dir]
        else:
            used_tiles[f"{coord[0]},{coord[1]}"] = {
                "coord": [coord[0], coord[1]],
                "dirs": [dir],
            }
        return False

    while len(active_beams) > 0:
        new_active = []
        for ab in active_beams:
            coord = [int(x) for x in ab.split(":")[0].split(",")]
            dir = ab.split(":")[1]
            this_move = dirs[dir]

            new_coord = [coord[0] + this_move[0], coord[1] + this_move[1]]
            new_y = new_coord[0]
            new_x = new_coord[1]

            if new_y not in range(len(raw)) or new_x not in range(len(raw[0])):
                continue
            elif raw[new_y][new_x] == ".":
                if check_if_used(new_coord, dir) == False:
                    new_active += [f"{new_y},{new_x}:{dir}"]
            elif raw[new_y][new_x] == "\\":
                if check_if_used(new_coord, dir) == False:
                    if dir == "r":
                        new_active += [f"{new_y},{new_x}:d"]
                    if dir == "l":
                        new_active += [f"{new_y},{new_x}:u"]
                    if dir == "u":
                        new_active += [f"{new_y},{new_x}:l"]
                    if dir == "d":
                        new_active += [f"{new_y},{new_x}:r"]
            elif raw[new_y][new_x] == "/":
                if check_if_used(new_coord, dir) == False:
                    if dir == "r":
                        new_active += [f"{new_y},{new_x}:u"]
                    if dir == "l":
                        new_active += [f"{new_y},{new_x}:d"]
                    if dir == "u":
                        new_active += [f"{new_y},{new_x}:r"]
                    if dir == "d":
                        new_active += [f"{new_y},{new_x}:l"]
            elif raw[new_y][new_x] == "|":
                if check_if_used(new_coord, dir) == False:
                    if dir in ["r", "l"]:
                        new_active += [f"{new_y},{new_x}:d"]
                        new_active += [f"{new_y},{new_x}:u"]
                    if dir in ["u", "d"]:
                        new_active += [f"{new_y},{new_x}:{dir}"]
            elif raw[new_y][new_x] == "-":
                if check_if_used(new_coord, dir) == False:
                    if dir in ["u", "d"]:
                        new_active += [f"{new_y},{new_x}:r"]
                        new_active += [f"{new_y},{new_x}:l"]
                    if dir in ["r", "l"]:
                        new_active += [f"{new_y},{new_x}:{dir}"]
        active_beams = new_active.copy()
        # break

        # print(active_beams)

    # print(used_tiles)
    # print([k for k in used_tiles])
    activated += [len(used_tiles)]

print(activated)
print(max(activated))
# checker = [["." for x in y] for y in raw]

# for y in range(len(raw)):
#     for x in range(len(raw[0])):
#         if f"{y},{x}" in used_tiles:
#             checker[y][x] = "#"

# import numpy as np

# print(np.array(checker))
