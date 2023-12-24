# %% 1

import numpy as np

raw = []

with open("advent_2023/24.txt", "r") as file:
    raw = [
        [[int(z) for z in y.strip().split(", ")] for y in x.strip().split("@")]
        for x in file
        if x.strip() != ""
    ]

print(raw)

eqs = [
    [
        x[1][1] / x[1][0],
        (-(x[1][1] / x[1][0]) * x[0][0]) + x[0][1],
        (">" if x[1][0] > 0 else "<") + str(x[0][0]),
        (">" if x[1][1] > 0 else "<") + str(x[0][1]),
    ]
    for x in raw
]

print(eqs)

target_min = 200000000000000
target_max = 400000000000000

tested = []

will_collide = 0

for a in range(len(eqs)):
    for b in range(len(eqs)):
        if (
            a == b
            or [a, b] in tested
            or [b, a] in tested
            or (eqs[a][0] == eqs[b][0] and eqs[b][1] != eqs[a][1])
        ):
            continue

        x_solution = (eqs[b][1] - eqs[a][1]) / (eqs[a][0] - eqs[b][0])
        y_solution = eqs[a][0] * x_solution + eqs[a][1]
        in_future = (
            eval(str(x_solution) + eqs[a][2])
            and eval(str(x_solution) + eqs[b][2])
            and eval(str(y_solution) + eqs[a][3])
            and eval(str(y_solution) + eqs[b][3])
        )
        in_test_area = (
            x_solution >= target_min
            and x_solution <= target_max
            and y_solution >= target_min
            and y_solution <= target_max
        )
        tested += [[a, b]]
        # print(eqs[a], eqs[b], x_solution, y_solution, in_future)
        if in_future == True and in_test_area == True:
            will_collide += 1

print(will_collide)
