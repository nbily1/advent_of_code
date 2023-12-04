# %% 1

forest = []

with open("dev/advent_2022/8.txt", "r") as file:
    forest = [x.strip() for x in file]

print(forest)

grid_width = len(forest)
grid_height = len(forest[0])

print(grid_width, grid_height)

fwd = range(0, grid_width)
bwd = range(grid_width - 1, 0, -1)

lr = []
td = []
rl = []
bu = []

# lr - fwd,fwd - i,j
for i in fwd:
    tallest = 0
    for j in fwd:
        thisone = int(forest[i][j])
        if thisone > tallest or i == 0:
            tallest = thisone
            lr += [f"{i},{j}"]

print(lr)

# td - fwd,fwd - j,i
for j in fwd:
    tallest = 0
    for i in fwd:
        thisone = int(forest[i][j])
        if thisone > tallest or j == 0:
            tallest = thisone
            td += [f"{i},{j}"]

print(td)

# bu - bwd,bwd - i,j
for i in bwd:
    tallest = 0
    for j in bwd:
        thisone = int(forest[i][j])
        if thisone > tallest or j == 98:
            tallest = thisone
            bu += [f"{i},{j}"]

print(bu)

# rl - bwd,bwd - i,j
for j in bwd:
    tallest = 0
    for i in bwd:
        thisone = int(forest[i][j])
        if thisone > tallest or i == 98:
            tallest = thisone
            rl += [f"{i},{j}"]

print(rl)

visible = lr
visible += [x for x in td if x not in visible]
visible += [x for x in rl if x not in visible]
visible += [x for x in bu if x not in visible]

print(visible)
print(len(visible))

# %% 2

trees_dict = {}

for i in fwd:
    for j in fwd:
        if i in [0, 98] or j in [0, 98]:
            continue

        base_tree = forest[i][j]

        # up
        up = 0
        for y in range(i - 1, -1, -1):
            check_tree = forest[y][j]
            if check_tree <= base_tree:
                up += 1
            if check_tree >= base_tree:
                break

        # down
        down = 0
        for y in range(i + 1, grid_height):
            check_tree = forest[y][j]
            if check_tree <= base_tree:
                down += 1
            if check_tree >= base_tree:
                break

        # left
        left = 0
        for x in range(j - 1, -1, -1):
            check_tree = forest[i][x]
            if check_tree <= base_tree:
                left += 1
            if check_tree >= base_tree:
                break

        # right
        right = 0
        for x in range(j + 1, grid_height):
            check_tree = forest[i][x]
            if check_tree <= base_tree:
                right += 1
            if check_tree >= base_tree:
                break

        trees_dict[f"{i},{j}"] = [[up, down, left, right], up * down * left * right]

print(trees_dict)

best_tree = ""
max_score = 0

for x in trees_dict:
    if trees_dict[x][1] > max_score:
        best_tree = x
        max_score = trees_dict[x][1]

print(best_tree, max_score)
