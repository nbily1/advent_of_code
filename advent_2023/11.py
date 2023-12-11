# %% 1

raw = []

with open("advent_2023/11.txt", "r") as file:
    raw = [[y for y in x.strip()] for x in file if x.strip() != ""]

# for y in raw:
#     print(y)

y_len = len(raw)
x_len = len(raw[0])


# Add rows as needed
ys_to_add = []
for y in range(y_len):
    this_row = sorted(raw[y])
    if this_row[0] == "." and this_row[-1] == ".":
        ys_to_add += [y]

for y in sorted(ys_to_add, reverse=True):
    raw.insert(y, ["." for x in range(x_len)])

# Add columns as needed
xs_to_add = []
for x in range(x_len):
    this_col = sorted([y[x] for y in raw])
    if this_col[0] == "." and this_col[-1] == ".":
        xs_to_add += [x]

for x in sorted(xs_to_add, reverse=True):
    for y in range(len(raw)):
        raw[y].insert(x, ".")

# print("\n")
# for y in raw:
#     print(y)

galaxies = {}

for y in range(len(raw)):
    for x in range(len(raw[0])):
        if raw[y][x] == "#":
            galaxies[f"{y},{x}"] = {"coord": [y, x], "moves": {}}

calced = []
total_moves = 0

for s in galaxies:
    for e in galaxies:
        if s == e or s + e in calced:
            continue
        this_moves = abs(galaxies[s]["coord"][0] - galaxies[e]["coord"][0]) + abs(
            galaxies[s]["coord"][1] - galaxies[e]["coord"][1]
        )
        galaxies[s]["moves"][e] = this_moves
        calced += [s + e]
        calced += [e + s]
        total_moves += this_moves

# print(galaxies)
print(total_moves)

# %% 2

raw = []

with open("advent_2023/11.txt", "r") as file:
    raw = [[y for y in x.strip()] for x in file if x.strip() != ""]

# for y in raw:
#     print(y)

y_len = len(raw)
x_len = len(raw[0])


# Add rows as needed
ys_to_add = []
for y in range(y_len):
    this_row = sorted(raw[y])
    if this_row[0] == "." and this_row[-1] == ".":
        ys_to_add += [y]

# Add columns as needed
xs_to_add = []
for x in range(x_len):
    this_col = sorted([y[x] for y in raw])
    if this_col[0] == "." and this_col[-1] == ".":
        xs_to_add += [x]

# print("\n")
# for y in raw:
#     print(y)

galaxies = {}

for y in range(len(raw)):
    for x in range(len(raw[0])):
        if raw[y][x] == "#":
            galaxies[f"{y},{x}"] = {"coord": [y, x], "moves": {}}

calced = []
total_moves = 0

for s in galaxies:
    for e in galaxies:
        if s == e or s + e in calced:
            continue
        this_moves = abs(galaxies[s]["coord"][0] - galaxies[e]["coord"][0]) + abs(
            galaxies[s]["coord"][1] - galaxies[e]["coord"][1]
        )

        # find any points where our path overlaps ys_to_add and xs_to_add
        y_overlap = [
            y
            for y in range(
                min([galaxies[s]["coord"][0], galaxies[e]["coord"][0]]),
                max([galaxies[s]["coord"][0], galaxies[e]["coord"][0]]),
            )
            if y in ys_to_add
        ]

        x_overlap = [
            x
            for x in range(
                min([galaxies[s]["coord"][1], galaxies[e]["coord"][1]]),
                max([galaxies[s]["coord"][1], galaxies[e]["coord"][1]]),
            )
            if x in xs_to_add
        ]

        # if there is an overlap, we have to expand by factor of 1 million
        if y_overlap:
            this_moves += len(y_overlap) * 999999
        if x_overlap:
            this_moves += len(x_overlap) * 999999

        galaxies[s]["moves"][e] = this_moves
        calced += [s + e]
        calced += [e + s]
        total_moves += this_moves

print(total_moves)
