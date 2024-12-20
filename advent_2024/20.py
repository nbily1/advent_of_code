import heapq
from copy import deepcopy

# %% Part 1

with open("advent_2024/20.txt", "r") as file:
    grid = [[y for y in x.strip()] for x in file]

for y in grid:
    print("".join(y))

S = []
E = []

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "S":
            S = [y, x]
        elif grid[y][x] == "E":
            E = [y, x]

print(S, E)

dirs = {"n": [-1, 0], "e": [0, 1], "s": [1, 0], "w": [0, -1]}

cheats = []
for y in range(1, len(grid) - 1):
    for x in range(1, len(grid[0]) - 1):
        if grid[y][x] != "#":
            continue
        if (
            grid[y + dirs["n"][0]][x + dirs["n"][1]] != "#"
            and grid[y + dirs["s"][0]][x + dirs["s"][1]] != "#"
            and [y, x] not in cheats
        ):
            cheats += [[[y, x], "ns"]]
        elif (
            grid[y + dirs["e"][0]][x + dirs["e"][1]] != "#"
            and grid[y + dirs["w"][0]][x + dirs["w"][1]] != "#"
            and [y, x] not in cheats
        ):
            cheats += [[[y, x], "ew"]]

print(cheats)

lengths = []

h = []

visited = [[S, 0]]

heapq.heappush(h, (0, 0, {"pos": S, "path": [S], "indir": ""}))

this_grid = deepcopy(grid)
# this_grid[c[0]][c[1]] = "."

ticker = 0
compl = []
is_done = False
cheated = False
while len(h) > 0:
    this_h = heapq.heappop(h)

    score = this_h[0]
    pos = this_h[2]["pos"]
    path = this_h[2]["path"]
    indir = this_h[2]["indir"]

    for d in dirs:
        if (
            (indir == "n" and d == "s")
            or (indir == "e" and d == "w")
            or (indir == "s" and d == "n")
            or (indir == "w" and d == "e")
        ):
            continue

        this_dir = dirs[d]
        ghost = [pos[0] + this_dir[0], pos[1] + this_dir[1]]

        if this_grid[ghost[0]][ghost[1]] in path:
            continue

        if this_grid[ghost[0]][ghost[1]] == "#":
            continue

        new_path = path + [ghost]
        new_score = len(new_path)

        if ghost in [v[0] for v in visited]:
            continue
        else:
            visited += [[ghost, new_score]]

        if this_grid[ghost[0]][ghost[1]] == "E":
            compl = [
                [
                    score,
                    ticker,
                    {
                        "pos": ghost,
                        "path": new_path[:-1],
                        "indir": d,
                    },
                ]
            ]
            is_done = True
            prev_path = new_path.copy()
            break
        else:
            heapq.heappush(
                h,
                (
                    new_score,
                    ticker,
                    {"pos": ghost, "path": new_path, "indir": d},
                ),
            )

        ticker += 1

    if is_done:
        break

# print([c[0] for c in compl])
# print(min([c[0] for c in compl]))

cheapest_score = min([c[0] for c in compl])

best_paths = [c for c in compl if c[0] == cheapest_score]

# visited = []
# for c in best_paths:
#     # print(c)
#     for p in c[2]["path"]:
#         if p not in visited:
#             visited += [p]

compl_grid = [
    [
        (
            "O"
            if [y, x] in best_paths[0][2]["path"]
            else this_grid[y][x].replace(".", " ")
        )
        for x in range(len(this_grid[y]))
    ]
    for y in range(len(this_grid))
]

# for y in compl_grid:
#     print("".join(y))

# lengths += [len(visited)]
print(visited)

for c in cheats:
    to_remove = c[0]
    this_dirs = c[1]

    cutoff = []

    start_adder = 0

    for d in this_dirs:
        # print(d, dirs[d], [to_remove[0] + dirs[d][0], to_remove[1] + dirs[d][1]])
        cutoff += [
            x
            for x in visited
            if x[0] == [to_remove[0] + dirs[d][0], to_remove[1] + dirs[d][1]]
        ]
        if [to_remove[0] + dirs[d][0], to_remove[1] + dirs[d][1]] == S:
            start_adder = 1

    # print(cutoff)

    lengths += [abs(cutoff[0][1] - cutoff[1][1]) - 2 - start_adder]

    # quit()

# quit()
print(lengths)

savings = {}
big_savings = 0
for le in lengths:
    this_saving = le
    if this_saving in savings:
        savings[this_saving] += 1
    else:
        savings[this_saving] = 1
    if this_saving >= 100:
        big_savings += 1

print(savings)
print(big_savings)


# %% Part 2

with open("advent_2024/20.txt", "r") as file:
    grid = [[y for y in x.strip()] for x in file]

for y in grid:
    print("".join(y))

S = []
E = []

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "S":
            S = [y, x]
        elif grid[y][x] == "E":
            E = [y, x]

print(S, E)

dirs = {"n": [-1, 0], "e": [0, 1], "s": [1, 0], "w": [0, -1]}

lengths = []

h = []

visited = [[S, 1]]

heapq.heappush(h, (0, 0, {"pos": S, "path": [S], "indir": ""}))

this_grid = deepcopy(grid)

ticker = 0
compl = []
is_done = False
cheated = False
while len(h) > 0:
    this_h = heapq.heappop(h)

    score = this_h[0]
    pos = this_h[2]["pos"]
    path = this_h[2]["path"]
    indir = this_h[2]["indir"]

    for d in dirs:
        if (
            (indir == "n" and d == "s")
            or (indir == "e" and d == "w")
            or (indir == "s" and d == "n")
            or (indir == "w" and d == "e")
        ):
            continue

        this_dir = dirs[d]
        ghost = [pos[0] + this_dir[0], pos[1] + this_dir[1]]

        if this_grid[ghost[0]][ghost[1]] in path:
            continue

        if this_grid[ghost[0]][ghost[1]] == "#":
            continue

        new_path = path + [ghost]
        new_score = len(new_path)

        if ghost in [v[0] for v in visited]:
            continue
        else:
            visited += [[ghost, new_score]]

        if this_grid[ghost[0]][ghost[1]] == "E":
            compl = [
                [
                    score,
                    ticker,
                    {
                        "pos": ghost,
                        "path": new_path[:-1],
                        "indir": d,
                    },
                ]
            ]
            is_done = True
            prev_path = new_path.copy()
            break
        else:
            heapq.heappush(
                h,
                (
                    new_score,
                    ticker,
                    {"pos": ghost, "path": new_path, "indir": d},
                ),
            )

        ticker += 1

    if is_done:
        break

# print([c[0] for c in compl])
# print(min([c[0] for c in compl]))

cheapest_score = min([c[0] for c in compl])

best_paths = [c for c in compl if c[0] == cheapest_score]

compl_grid = [
    [
        (
            "O"
            if [y, x] in best_paths[0][2]["path"]
            else this_grid[y][x].replace(".", " ")
        )
        for x in range(len(this_grid[y]))
    ]
    for y in range(len(this_grid))
]

# for y in compl_grid:
#     print("".join(y))

print(visited)


cheat_length = 20
cheat_jumps = []
for y in range(-cheat_length, cheat_length + 1):
    for x in range(-cheat_length, cheat_length + 1):
        if abs(y) + abs(x) <= cheat_length and abs(y) + abs(x) > 1:
            cheat_jumps += [[[y, x], abs(y) + abs(x)]]
# print(cheat_jumps)

for i in range(len(visited)):
    this_pos = visited[i][0]
    this_ps = visited[i][1]

    for c in cheat_jumps:
        dest = [this_pos[0] + c[0][0], this_pos[1] + c[0][1]]
        if (
            dest[0] < 1
            or dest[1] < 1
            or dest[0] > len(grid) - 1
            or dest[1] > len(grid[0]) - 1
            or grid[dest[0]][dest[1]] == "#"
        ):
            continue
        dest_v = [v for v in visited[i:] if v[0] == dest and v[1] > this_ps + c[1]]
        if dest_v:
            lengths += [abs(this_ps - dest_v[0][1]) - c[1]]

    if i % 100 == 0:
        print(i)

# quit()
print(lengths)

savings = {}
big_savings = 0
for le in lengths:
    this_saving = le
    if le < 50:
        continue
    if this_saving in savings:
        savings[this_saving] += 1
    else:
        savings[this_saving] = 1
    if this_saving >= 100:
        big_savings += 1

# print(savings)
print(big_savings)
