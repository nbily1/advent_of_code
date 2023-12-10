# %% 1

raw = []

with open("advent_2023/10.txt", "r") as file:
    raw = [[y for y in x.strip()] for x in file if x.strip() != ""]

print(raw)

moves = {
    # y,x
    "|": [[1, 0], [-1, 0]],
    "-": [[0, 1], [0, -1]],
    "L": [[-1, 0], [0, 1]],
    "J": [[-1, 0], [0, -1]],
    "7": [[1, 0], [0, -1]],
    "F": [[1, 0], [0, 1]],
    "S": [[1, 0], [-1, 0], [0, 1], [0, -1]],
}

mydict = {}

start_coord = []

for y in range(len(raw)):
    for x in range(len(raw[y])):
        if raw[y][x] != ".":
            mydict[f"{y},{x}"] = {
                "symbol": raw[y][x],
                "coord": [y, x],
                "moves": moves[raw[y][x]],
            }
            if raw[y][x] == "S":
                start_coord = [y, x]

# print(mydict)
print(start_coord)

paths = [[start_coord]]
looped = False

print("paths:", paths)

while looped == False:
    active_paths = []
    for p in paths:
        last_coord = p[-1]
        # print("p:", p)
        # print("last_coord:", last_coord)
        txt_coord = f"{last_coord[0]},{last_coord[1]}"
        these_moves = mydict[txt_coord]["moves"]

        for move in these_moves:
            move_coord = [last_coord[0] + move[0], last_coord[1] + move[1]]
            txt_move = f"{move_coord[0]},{move_coord[1]}"
            try:
                if (
                    move[0] != 0
                    and move[0] * -1 in [x[0] for x in mydict[txt_move]["moves"]]
                ) or (
                    move[1] != 0
                    and move[1] * -1 in [x[1] for x in mydict[txt_move]["moves"]]
                ):
                    if move_coord not in p:
                        active_paths += [p + [move_coord]]
                    if mydict[txt_move]["symbol"] == "S" and len(p) > 2:
                        looped = True
                        active_paths = [p]
                        break
                    # if len(p) > 15:
                    #     looped = True
            except KeyError:
                pass
        # print("active_paths:", active_paths)
    paths = active_paths.copy()
    # print("paths:", paths)

print(paths)
print(len(paths[0]) / 2)

# %% 2

new_paths = []
paths = paths[0]

# open corridors that have no empty tile path by adding half-coordinates

for i in range(len(paths)):
    new_paths += [paths[i]]
    next_coord = paths[i + 1] if i < len(paths) - 1 else paths[0]
    if paths[i][0] == next_coord[0]:
        new_paths += [
            [paths[i][0], paths[i][1] + ((next_coord[1] - paths[i][1]) * 0.5)]
        ]
    else:
        new_paths += [
            [paths[i][0] + ((next_coord[0] - paths[i][0]) * 0.5), paths[i][1]]
        ]

print(new_paths)

max_y = len(raw) + 1
max_x = len(raw[0]) + 1

outside = [[-1, -1]]

# For the grid, start from -1,-1
# fill in all directions until we reach max_x+1,max_y+1 (at 0.5 intervals)
# all of the resulting tiles are outside the pipe
# find all coords from raw that are not outside and not the pipe itself

while [max_y, max_x] not in outside:
    for x in outside:
        tester = [x[0] + 0.5, x[1]]
        if (
            tester[0] <= max_y
            and tester[0] >= -1
            and tester not in outside
            and tester not in new_paths
        ):
            outside += [tester]

        tester = [x[0] - 0.5, x[1]]
        if (
            tester[0] <= max_y
            and tester[0] >= -1
            and tester not in outside
            and tester not in new_paths
        ):
            outside += [tester]

        tester = [x[0], x[1] + 0.5]
        if (
            tester[1] <= max_x
            and tester[1] >= -1
            and tester not in outside
            and tester not in new_paths
        ):
            outside += [tester]

        tester = [x[0], x[1] - 0.5]
        if (
            tester[1] <= max_x
            and tester[1] >= -1
            and tester not in outside
            and tester not in new_paths
        ):
            outside += [tester]

# print(outside)

inside = []

for y in range(len(raw)):
    for x in range(len(raw[y])):
        if [y, x] not in outside and [y, x] not in new_paths:
            inside += [[y, x]]

print("\n")
# print(inside)
print(len(inside))
