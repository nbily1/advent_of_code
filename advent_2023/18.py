# %% 1
from copy import deepcopy

raw = []

with open("advent_2023/18.txt", "r") as file:
    raw = [[y for y in x.strip().split()] for x in file if x.strip() != ""]

for x in raw:
    x[1] = int(x[1])
    x[2] = x[2][1:-1]

print(raw)

moves = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}

curr_coord = [0, 0]

coords = [[0, 0]]

max_y = 0
max_x = 0
min_y = 0
min_x = 0

for x in raw:
    this_move = moves[x[0]]
    for i in range(x[1]):
        curr_coord = [curr_coord[0] + this_move[0], curr_coord[1] + this_move[1]]
        if curr_coord not in coords:
            coords += [curr_coord]
            if curr_coord[0] > max_y:
                max_y = curr_coord[0]
            if curr_coord[0] < min_y:
                min_y = curr_coord[0]
            if curr_coord[1] > max_x:
                max_x = curr_coord[1]
            if curr_coord[1] < min_x:
                min_x = curr_coord[1]

# print(coords)
print(min_y, max_y, min_x, max_x)

top_cell = [x for x in coords if x[0] == min_y and [x[0] + 1, x[1]] not in coords][0]

# print(top_cell)

inside = [[top_cell[0] + 1, top_cell[1]]]
active_cells = [[top_cell[0] + 1, top_cell[1]]]

# print(inside)

# For the grid, start from -1,-1
# fill in all directions until we reach max_x+1,max_y+1
# all of the resulting tiles are outside the hole
# find all coords from that are not outside

while len(active_cells) > 0:
    holder = []
    for x in active_cells:
        tester = [x[0] + 1, x[1]]
        if (
            tester[0] <= max_y
            and tester[0] >= min_y
            and tester not in inside
            and tester not in coords
            and tester not in holder
        ):
            inside += [tester]
            holder += [tester]

        tester = [x[0] - 1, x[1]]
        if (
            tester[0] <= max_y
            and tester[0] >= min_y
            and tester not in inside
            and tester not in coords
            and tester not in holder
        ):
            inside += [tester]
            holder += [tester]

        tester = [x[0], x[1] + 1]
        if (
            tester[1] <= max_x
            and tester[1] >= min_x
            and tester not in inside
            and tester not in coords
            and tester not in holder
        ):
            inside += [tester]
            holder += [tester]

        tester = [x[0], x[1] - 1]
        if (
            tester[1] <= max_x
            and tester[1] >= min_x
            and tester not in inside
            and tester not in coords
            and tester not in holder
        ):
            inside += [tester]
            holder += [tester]
    active_cells = deepcopy(holder)

# print("\n")
# print(inside)
print(len(inside) + len(coords))


# %% 2

raw = []

with open("advent_2023/18.txt", "r") as file:
    raw = [[y for y in x.strip().split()] for x in file if x.strip() != ""]

for x in raw:
    x[0] = x[2][-2]
    x[1] = int(x[2][2:-2], 16)
    x[2] = x[2][1:-1]

print(raw)

moves = {"3": [-1, 0], "1": [1, 0], "2": [0, -1], "0": [0, 1]}

curr_coord = [0, 0]

coords = [[0, 0]]

rim_length = 0

for x in raw:
    this_move = moves[x[0]]
    curr_coord = [
        curr_coord[0] + this_move[0] * x[1],
        curr_coord[1] + this_move[1] * x[1],
    ]
    rim_length += x[1]
    coords += [curr_coord]

max_y = max([x[0] for x in coords])
max_x = max([x[1] for x in coords])
min_y = min([x[0] for x in coords])
min_x = min([x[1] for x in coords])

if min_y < 1:
    for x in range(len(coords)):
        coords[x][0] += abs(min_y) + 1

if min_x < 1:
    for x in range(len(coords)):
        coords[x][1] += abs(min_x) + 1


print(coords)
print(min_y, max_y, min_x, max_x)

shoelace = 0

for c in range(len(coords) - 1):
    shoelace += (coords[c][0] + coords[c + 1][0]) * (coords[c][1] - coords[c + 1][1])

print(rim_length)

print(shoelace / 2 + rim_length / 2 + 1)
