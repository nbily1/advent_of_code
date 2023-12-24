# %% 1

from copy import deepcopy

raw = []

with open("advent_2023/22.txt", "r") as file:
    raw = [[[int(z) for z in y.split(",")] for y in x.strip().split("~")] for x in file]

# print(raw)

max_z = max([max([x[0][2] for x in raw]), max([x[1][2] for x in raw])])

bricks = {}

for b in range(len(raw)):
    bricks[b] = {"raw": raw[b], "coords": [], "bottom": min(raw[b][0][2], raw[b][1][2])}
    for x in range(raw[b][0][0], raw[b][1][0] + 1):
        for y in range(raw[b][0][1], raw[b][1][1] + 1):
            for z in range(raw[b][0][2], raw[b][1][2] + 1):
                bricks[b]["coords"] += [[x, y, z]]

# print(bricks)

can_zap = 0

for z in range(max_z):
    for b in bricks:
        if bricks[b]["bottom"] == z:
            stopped = False
            while stopped != True:
                ghost = [[c[0], c[1], c[2] - 1] for c in bricks[b]["coords"]]
                if 0 in [g[2] for g in ghost]:
                    stopped = True
                    break
                for checker in bricks:
                    if checker == b:
                        continue
                    if any(map(lambda cube: cube in ghost, bricks[checker]["coords"])):
                        stopped = True
                        break
                else:
                    bricks[b]["coords"] = deepcopy(ghost)

print("\n", bricks)

critical_bricks = []

for b in bricks:
    ghost = [[c[0], c[1], c[2] - 1] for c in bricks[b]["coords"]]
    resting_on = []
    for checker in bricks:
        if checker == b:
            continue
        if any(map(lambda cube: cube in ghost, bricks[checker]["coords"])):
            resting_on += [checker]
    if len(resting_on) == 1 and resting_on not in critical_bricks:
        critical_bricks += [resting_on.copy()]

print("\n", critical_bricks)

can_zap = len(bricks) - len(critical_bricks)

print("\n", can_zap)
