# %% Part 1

with open("advent_2024/14.txt", "r") as file:
    my_list = [x.strip().split() for x in file]

print(my_list)

x_len = 101  # 11
y_len = 103  # 7
turns_left = 100

robots = {}

for i in range(len(my_list)):
    robots[i] = {"p": [], "v": []}
    robots[i]["p"] = [int(x) for x in my_list[i][0].replace("p=", "").split(",")]
    robots[i]["v"] = [int(x) for x in my_list[i][1].replace("v=", "").split(",")]

print(robots)

grid = []

for y in range(y_len):
    grid.append(["." for _ in range(x_len)])

for r in robots.values():
    loc = r["p"]
    vel = r["v"]
    new_loc = [
        (loc[0] + vel[0] * turns_left) % x_len,
        (loc[1] + vel[1] * turns_left) % y_len,
    ]
    if grid[new_loc[1]][new_loc[0]] == ".":
        grid[new_loc[1]][new_loc[0]] = "1"
    else:
        grid[new_loc[1]][new_loc[0]] = str(int(grid[new_loc[1]][new_loc[0]]) + 1)

for y in grid:
    print("".join(y))

q1 = [
    [x for x in y[: int((x_len - 1) / 2)]] for y in grid[: int((y_len - 1) / 2)]
]  # noqa: E203
q2 = [
    [x for x in y[int((x_len + 1) / 2) :]] for y in grid[: int((y_len - 1) / 2)]
]  # noqa: E203
q3 = [
    [x for x in y[: int((x_len - 1) / 2)]] for y in grid[int((y_len + 1) / 2) :]
]  # noqa: E203
q4 = [
    [x for x in y[int((x_len + 1) / 2) :]] for y in grid[int((y_len + 1) / 2) :]
]  # noqa: E203

safety_score = 1

print("")
this_score = 0
for y in q1:
    print("".join(y))
    this_score += sum([int(x) for x in y if x != "."])
safety_score *= this_score

print("")
this_score = 0
for y in q2:
    print("".join(y))
    this_score += sum([int(x) for x in y if x != "."])
safety_score *= this_score

print("")
this_score = 0
for y in q3:
    print("".join(y))
    this_score += sum([int(x) for x in y if x != "."])
safety_score *= this_score

print("")
this_score = 0
for y in q4:
    print("".join(y))
    this_score += sum([int(x) for x in y if x != "."])
safety_score *= this_score

print(safety_score)


# %% Part 2

with open("advent_2024/14.txt", "r") as file:
    my_list = [x.strip().split() for x in file]

# print(my_list)

x_len = 101  # 11
y_len = 103  # 7
start_turn = 0
turns_left = 99999

robots = {}

x_vars = []
y_vars = []

for t in range(start_turn, turns_left + 1):
    for i in range(len(my_list)):
        robots[i] = {"p": [], "v": []}
        robots[i]["p"] = [int(x) for x in my_list[i][0].replace("p=", "").split(",")]
        robots[i]["v"] = [int(x) for x in my_list[i][1].replace("v=", "").split(",")]

    # print(robots)

    grid = []

    for y in range(y_len):
        grid.append(["." for _ in range(x_len)])

    for r in robots.values():
        loc = r["p"]
        vel = r["v"]
        new_loc = [
            (loc[0] + vel[0] * t) % x_len,
            (loc[1] + vel[1] * t) % y_len,
        ]
        if grid[new_loc[1]][new_loc[0]] == ".":
            grid[new_loc[1]][new_loc[0]] = "#"

    lft = [[x for x in y[: int((x_len - 1) / 2)]] for y in grid]
    rt = [
        [y[i] for i in range(len(y) - 1, int((x_len + 1) / 2) - 1, -1)] for y in grid
    ]  # noqa: E203

    found = False
    for y in grid:
        if "##############" in "".join(y):
            for y in grid:
                print("".join(y))
            print(t)
            found = True
            break

    if found:
        break
