# %% 1
import re, json  # , pandas as pd
from math import floor

raw = []

with open("dev/advent_2022/17.txt", "r") as file:
    raw = [x.strip() for x in file.readline()]


jets = raw.copy()
# for x in raw:
#     jets += [x, "v"]

# print(jets)

max_rocks = 1000000000000
left_limit = -2
right_limit = 4
current_height = 0
current_shape = -1
current_sprite = 0

used_cells = [[x, 0] for x in range(left_limit, right_limit + 1)]
# print(used_cells)

shapes = [
    [[0, 4], [1, 4], [2, 4], [3, 4]],  # -
    [[0, 5], [1, 5], [2, 5], [1, 4], [1, 6]],  # +
    [[0, 4], [1, 4], [2, 4], [2, 5], [2, 6]],  # ⅃
    [[0, 4], [0, 5], [0, 6], [0, 7]],  # |
    [[0, 4], [0, 5], [1, 4], [1, 5]],  # o
]

first_rock = []
check_sprite = []
found_pattern = False

rocks = 0

while rocks < max_rocks:
    this_shape = [
        [x[0], x[1] + current_height] for x in shapes[rocks % len(shapes)].copy()
    ]
    # print(this_shape)

    is_stuck = False

    while is_stuck == False:
        move = jets[current_sprite % (len(jets))]

        # print(jets[current_sprite % (len(jets) - 1)])

        if move == ">":
            ghost = [[x[0] + 1, x[1]] for x in this_shape.copy()]
            if max([x[0] for x in ghost.copy()]) > right_limit or any(
                i in ghost for i in used_cells
            ):
                pass
            else:
                this_shape = ghost.copy()
        elif move == "<":
            ghost = [[x[0] - 1, x[1]] for x in this_shape.copy()]
            if min([x[0] for x in ghost.copy()]) < left_limit or any(
                i in ghost for i in used_cells
            ):
                pass
            else:
                this_shape = ghost.copy()

        ghost = [[x[0], x[1] - 1] for x in this_shape.copy()]
        if any(i in ghost for i in used_cells):
            is_stuck = True

            used_cells += this_shape
            current_height = max([x[1] for x in used_cells.copy()])

            # print("\t", this_shape)
        else:
            this_shape = ghost.copy()

        current_sprite = (current_sprite + 1) % len(jets)
    for coord in used_cells:
        if coord[1] < current_height - 100:
            used_cells.remove(coord)

    if (rocks + 1) % len(shapes) == 0 and rocks > 0:
        if len(check_sprite) == 0:
            check_sprite += [
                [
                    current_sprite - 1,
                    rocks,
                    current_height,
                    [x[0] for x in this_shape.copy()],
                ]
            ]
        elif [current_sprite - 1, [x[0] for x in this_shape.copy()]] not in [
            [x[0], x[3]] for x in check_sprite
        ]:
            check_sprite += [
                [
                    current_sprite - 1,
                    rocks,
                    current_height,
                    [x[0] for x in this_shape.copy()],
                ]
            ]
        elif [current_sprite - 1, [x[0] for x in this_shape.copy()]] in [
            [x[0], x[3]] for x in check_sprite
        ] and found_pattern == False:
            check_sprite += [
                [
                    current_sprite - 1,
                    rocks,
                    current_height,
                    [x[0] for x in this_shape.copy()],
                ]
            ]
            check_sprite = [x for x in check_sprite if x[0] == current_sprite - 1]
            found_pattern = True
            print(check_sprite)
            patt_len = check_sprite[1][1] - check_sprite[0][1]
            height_diff = check_sprite[1][2] - check_sprite[0][2]
            remainder = (max_rocks - check_sprite[1][1]) % patt_len
            times = floor((max_rocks - check_sprite[1][1]) / patt_len)
            used_cells = [
                [x[0], x[1] + ((height_diff * times))]  # - check_sprite[0][2])]
                for x in used_cells.copy()
            ]
            rocks = max_rocks - remainder
            current_height = max([x[1] for x in used_cells.copy()])
            print(patt_len, height_diff, remainder, times, rocks, current_height)

    rocks += 1

# print(used_cells)
print(current_height)
