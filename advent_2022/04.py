# %% 1

assignment_list = []

with open("advent_2022/04.txt", "r") as file:
    assignment_list = [x.strip() for x in file]

overlaps = 0

for x in assignment_list:
    x = [int(y) for y in x.replace("-", ",").split(",")]

    if (x[0] <= x[2] and x[1] >= x[3]) or (x[2] <= x[0] and x[3] >= x[1]):
        overlaps += 1

print(overlaps)

# %% 2

overlaps = 0

for x in assignment_list:
    x = [int(y) for y in x.replace("-", ",").split(",")]

    if (
        (x[0] <= x[2] and x[1] >= x[3])
        or (x[2] <= x[0] and x[3] >= x[1])
        or (x[0] in range(x[2], x[3] + 1))
        or (x[1] in range(x[2], x[3] + 1))
        or (x[2] in range(x[0], x[1] + 1))
        or (x[3] in range(x[0], x[1] + 1))
    ):
        overlaps += 1

print(overlaps)
