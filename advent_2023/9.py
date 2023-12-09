# %% 1

raw = []

with open("advent_2023/9.txt", "r") as file:
    raw = [[[int(y) for y in x.strip().split()]] for x in file if x.strip() != ""]

# print(raw)

for i in range(len(raw)):
    while min(raw[i][-1]) != 0 or max(raw[i][-1]) != 0:  # sum(raw[i][-1]) != 0:  #
        raw[i].append(
            [raw[i][-1][x + 1] - raw[i][-1][x] for x in range(len(raw[i][-1]) - 1)]
        )
    else:
        raw[i][-1].append(0)

    for j in range(len(raw[i]) - 2, -1, -1):
        raw[i][j].append(raw[i][j][-1] + raw[i][j + 1][-1])
        # print(raw[i][j])

# print(raw)

last_vals = [x[0][-1] for x in raw]

print("\n", last_vals)
print(sum(last_vals))

# %% 2

raw = []

with open("advent_2023/9.txt", "r") as file:
    raw = [[[int(y) for y in x.strip().split()]] for x in file if x.strip() != ""]

# print(raw)

for i in range(len(raw)):
    while min(raw[i][-1]) != 0 or max(raw[i][-1]) != 0:  # sum(raw[i][-1]) != 0:  #
        raw[i].append(
            [raw[i][-1][x + 1] - raw[i][-1][x] for x in range(len(raw[i][-1]) - 1)]
        )
    else:
        raw[i][-1].insert(0, 0)

    for j in range(len(raw[i]) - 2, -1, -1):
        raw[i][j].insert(0, raw[i][j][0] - raw[i][j + 1][0])
        # print(raw[i][j])

# print(raw)

first_vals = [x[0][0] for x in raw]

print("\n", first_vals)
print(sum(first_vals))
