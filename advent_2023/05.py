# %% 1
from datetime import datetime

print(datetime.now())

raw = []

with open("advent_2023/05.txt", "r") as file:
    raw = [x.strip() for x in file if x.strip() != ""]

print(raw)

seeds = [[int(x)] for x in raw[0].split(":")[1].strip().split()]

# print(seeds)

maps = {}
curkey = ""

for x in raw[1:]:
    if x[0] not in "0123456789":
        maps[x[:-1]] = []
        curkey = x[:-1]
    else:
        maps[curkey] += [[int(y) for y in x.split()]]

print(maps)

mapped = {k: [] for k in maps}

for k in maps:
    for l in range(len(maps[k])):
        start = maps[k][l][1]
        rnge = maps[k][l][1] + maps[k][l][2]
        diff = maps[k][l][1] - maps[k][l][0]
        mapped[k] += [[start, rnge, diff]]

# print(mapped)

# this_seed = 0

# while this_seed < len(seeds):
#     for k in mapped:
#         is_found = False
#         for m in range(len(mapped[k])):
#             if (
#                 seeds[this_seed][-1] >= mapped[k][m][0]
#                 and seeds[this_seed][-1] <= mapped[k][m][1]
#             ):
#                 seeds[this_seed] += [seeds[this_seed][-1] - mapped[k][m][2]]
#                 is_found = True
#                 break
#         if is_found == False:
#             seeds[this_seed] += [seeds[this_seed][-1]]
#     this_seed += 1

# print(seeds)

# print(min([x[-1] for x in seeds]))

# %% 2

seeds = []

vals = [[int(x)] for x in raw[0].split(":")[1].strip().split()]
for i in range(0, len(vals), 2):
    seeds += [[vals[i][0], vals[i][0] + vals[i + 1][0]]]

# print(seeds)

this_seed = 0

lowest = None

ranges_to_check = seeds.copy()

for k in mapped:
    new_ranges = []
    r = 0
    while r < len(ranges_to_check):
        r_s = ranges_to_check[r][0]
        r_e = ranges_to_check[r][1]
        for n in mapped[k]:
            n_s = n[0]
            n_e = n[1]
            if r_s in range(n_s, n_e + 1) and r_e in range(
                n_s, n_e + 1
            ):  # n contains r
                new_ranges += [[r_s - n[2], r_e - n[2]]]
                break
            elif r_s < n_s and r_e in range(n_s, n_e + 1):  # r left overlaps n
                new_ranges += [[n_s - n[2], r_e - n[2]]]
                r_e = n_s
            elif r_s in range(n_s, n_e + 1) and r_e > n_e:  # r right overlaps n
                new_ranges += [[r_s - n[2], n_e - n[2]]]
                r_s = n_e
            elif n_s in range(r_s, r_e + 1) and n_e in range(
                r_s, r_e + 1
            ):  # r contains n
                new_ranges += [[n_s - n[2], n_e - n[2]]]
                r_e = n_s
                ranges_to_check += [[n_e, r_e]]
            elif n == mapped[k][-1]:  # no overlap
                new_ranges += [[r_s, r_e]]
        r += 1
    ranges_to_check = new_ranges.copy()
    print(k, min([x[0] for x in new_ranges]))

lowest = None

for i in range(len(ranges_to_check)):
    if i == 0:
        lowest = ranges_to_check[i][0]
    elif ranges_to_check[i][0] < lowest and ranges_to_check[i][0] != 0:
        lowest = ranges_to_check[i][0]

print(lowest)

print(datetime.now())
