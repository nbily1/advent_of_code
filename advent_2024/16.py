import heapq

# %% Part 1

with open("advent_2024/16.txt", "r") as file:
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

h = []

heapq.heappush(h, (0, 0, {"pos": S, "path": [S], "indir": "", "turns": 0}))

cheapest = [[S, 0, ""]]

ticker = 0
compl = []
while len(h) > 0:
    this_h = heapq.heappop(h)

    score = this_h[0]
    pos = this_h[2]["pos"]
    path = this_h[2]["path"]
    indir = this_h[2]["indir"]
    turns = this_h[2]["turns"]

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

        if grid[ghost[0]][ghost[1]] in path:
            continue

        if grid[ghost[0]][ghost[1]] == "#":
            continue

        new_path = path + [ghost]
        new_turns = turns
        if d != indir and indir != "":
            new_turns += 1
        new_score = len(new_path) + new_turns * 1000

        not_cheapest = False
        for c in range(len(cheapest)):
            if ghost == cheapest[c][0] and d == cheapest[c][2]:
                if new_score > cheapest[c][1]:
                    not_cheapest = True
                else:
                    _ = cheapest.pop(c)
                break

        if not_cheapest:
            continue

        cheapest += [[ghost, new_score, d]]

        if grid[ghost[0]][ghost[1]] == "E":
            compl += [
                [
                    score,
                    ticker,
                    {
                        "pos": ghost,
                        "path": new_path[:-1],
                        "indir": d,
                        "turns": new_turns,
                    },
                ]
            ]
        else:
            heapq.heappush(
                h,
                (
                    new_score,
                    ticker,
                    {"pos": ghost, "path": new_path, "indir": d, "turns": new_turns},
                ),
            )

        ticker += 1

print([c[0] for c in compl])
print(min([c[0] for c in compl]))

cheapest_score = min([c[0] for c in compl])

best_paths = [c for c in compl if c[0] == cheapest_score]


visited = []
for c in best_paths:
    print(c)
    for p in c[2]["path"]:
        if p not in visited:
            visited += [p]

compl_grid = [
    [
        "O" if [y, x] in best_paths[0][2]["path"] else grid[y][x].replace(".", " ")
        for x in range(len(grid[y]))
    ]
    for y in range(len(grid))
]

for y in compl_grid:
    print("".join(y))

print(len(visited) + 1)
