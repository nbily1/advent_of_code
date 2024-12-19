from functools import cache

# %% Part 1

with open("advent_2024/19.txt", "r") as file:
    patterns = [x.strip().split(", ") for x in file if "," in x][0]

with open("advent_2024/19.txt", "r") as file:
    designs = [x.strip() for x in file if "," not in x and x.strip() != ""]

print(patterns)
print(designs)


@cache
def checker(design: str) -> bool:
    for i in range(len(design), 0, -1):
        to_check = design[:i]
        if to_check in patterns:
            if i == len(design):
                return True
            else:
                if checker(design[i:]):
                    return True
    return False


possible = 0
for d in designs:
    if checker(d):
        possible += 1

print(possible)


# %% Part 2

with open("advent_2024/19.txt", "r") as file:
    patterns = [x.strip().split(", ") for x in file if "," in x][0]

with open("advent_2024/19.txt", "r") as file:
    designs = [x.strip() for x in file if "," not in x and x.strip() != ""]

# print(patterns)
# print(designs)


@cache
def checker(design: str) -> int:
    poss = 0
    for i in range(len(design), 0, -1):
        to_check = design[:i]
        if to_check in patterns:
            if i == len(design):
                poss += 1
            else:
                poss += checker(design[i:])
    return poss


possible = 0
for d in designs:
    possible += checker(d)

print(possible)
