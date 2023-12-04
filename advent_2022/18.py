# %% 1
import re, json  # , pandas as pd
from math import floor

raw = []

with open("dev/advent_2022/18.txt", "r") as file:
    raw = [[int(y) for y in x.strip().split(",")] for x in file]


# print(raw)

# faces = 0

# for cube in raw:
#     if [cube[0] + 1, cube[1], cube[2]] not in raw:
#         faces += 1
#     if [cube[0] - 1, cube[1], cube[2]] not in raw:
#         faces += 1

#     if [cube[0], cube[1] + 1, cube[2]] not in raw:
#         faces += 1
#     if [cube[0], cube[1] - 1, cube[2]] not in raw:
#         faces += 1

#     if [cube[0], cube[1], cube[2] + 1] not in raw:
#         faces += 1
#     if [cube[0], cube[1], cube[2] - 1] not in raw:
#         faces += 1

# print(faces)

# %% 2

facing = []

for cube in raw:
    if (
        [cube[0] + 1, cube[1], cube[2]] not in raw
        or [cube[0] - 1, cube[1], cube[2]] not in raw
    ) and cube not in facing:
        facing += [cube]

    if (
        [cube[0], cube[1] + 1, cube[2]] not in raw
        or [cube[0], cube[1] - 1, cube[2]] not in raw
    ) and cube not in facing:
        facing += [cube]

    if (
        [cube[0], cube[1], cube[2] + 1] not in raw
        or [cube[0], cube[1], cube[2] - 1] not in raw
    ) and cube not in facing:
        facing += [cube]

print(facing)
print(len(raw), len(facing))

print(min([x[0] for x in facing]), max([x[0] for x in facing]))
print(min([x[1] for x in facing]), max([x[1] for x in facing]))
print(min([x[2] for x in facing]), max([x[2] for x in facing]))

outside = [[-2, -2, -2]]

# For the 20x20x20 cube, start from -2,-2,-2 through 22,22,22
# fill in all directions until we reach to outer edge
# do the same exercise form part 1 to find the

while [22, 22, 22] not in outside:
    for x in outside:
        tester = [x[0] + 1, x[1], x[2]]
        if (
            tester[0] <= 22
            and tester[0] >= -2
            and tester not in outside
            and tester not in facing
        ):
            outside += [tester]

        tester = [x[0] - 1, x[1], x[2]]
        if (
            tester[0] <= 22
            and tester[0] >= -2
            and tester not in outside
            and tester not in facing
        ):
            outside += [tester]

        tester = [x[0], x[1] + 1, x[2]]
        if (
            tester[1] <= 22
            and tester[1] >= -2
            and tester not in outside
            and tester not in facing
        ):
            outside += [tester]

        tester = [x[0], x[1] - 1, x[2]]
        if (
            tester[1] <= 22
            and tester[1] >= -2
            and tester not in outside
            and tester not in facing
        ):
            outside += [tester]

        tester = [x[0], x[1], x[2] + 1]
        if (
            tester[2] <= 22
            and tester[2] >= -2
            and tester not in outside
            and tester not in facing
        ):
            outside += [tester]

        tester = [x[0], x[1], x[2] - 1]
        if (
            tester[2] <= 22
            and tester[2] >= -2
            and tester not in outside
            and tester not in facing
        ):
            outside += [tester]

faces = 0

for cube in outside:
    if (
        cube[0] + 1 >= -1
        and cube[0] + 1 <= 21
        and [cube[0] + 1, cube[1], cube[2]] not in outside
    ):
        faces += 1
    if (
        cube[0] - 1 >= -1
        and cube[0] - 1 <= 21
        and [cube[0] - 1, cube[1], cube[2]] not in outside
    ):
        faces += 1

    if (
        cube[1] + 1 >= -1
        and cube[1] + 1 <= 21
        and [cube[0], cube[1] + 1, cube[2]] not in outside
    ):
        faces += 1
    if (
        cube[1] - 1 >= -1
        and cube[1] - 1 <= 21
        and [cube[0], cube[1] - 1, cube[2]] not in outside
    ):
        faces += 1

    if (
        cube[2] + 1 >= -1
        and cube[2] + 1 <= 21
        and [cube[0], cube[1], cube[2] + 1] not in outside
    ):
        faces += 1
    if (
        cube[2] - 1 >= -1
        and cube[2] - 1 <= 21
        and [cube[0], cube[1], cube[2] - 1] not in outside
    ):
        faces += 1

print(faces)
