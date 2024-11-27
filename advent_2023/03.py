# %% 1
# import re

raw = []

with open("advent_2023/03.txt", "r") as file:
    raw = [x.strip() for x in file]

print(raw)

digs = []
count_digs = []
help_digs = []

my_y = 0

for y in raw:
    sprite = 0
    while sprite < len(y):
        this_dig = ""
        if y[sprite] in "1234567890":
            for checker in range(sprite, len(y)):
                if y[checker] in "1234567890":
                    this_dig += y[checker]
                    if checker == len(y) - 1:
                        sprite = checker
                        break
                else:
                    sprite = checker
                    break
        if this_dig != "":
            counted = False
            for i in range(my_y - 1, my_y + 2):
                if i < 0 or i >= len(raw) or counted == True:
                    continue
                else:
                    for j in range(sprite - len(this_dig) - 1, sprite + 1):
                        if j < 0 or j >= len(y) or counted == True:
                            continue
                        elif raw[i][j] not in "1234567890.":
                            help_digs += [
                                [
                                    this_dig,
                                    [my_y, sprite - len(this_dig)],
                                    [i, j],
                                    raw[i][j],
                                ]
                            ]
                            counted = True
                            count_digs += [int(this_dig)]
                            break

            digs += [this_dig]
        sprite += 1
    my_y += 1

# print(digs)
print(count_digs)
print(sum(count_digs))

print(len(digs), len(count_digs))

print(help_digs)
quit()

# %% 2

digs = []
count_digs = []
help_digs = []

my_y = 0

for y in raw:
    sprite = 0
    while sprite < len(y):
        this_dig = ""
        if y[sprite] in "1234567890":
            for checker in range(sprite, len(y)):
                if y[checker] in "1234567890":
                    this_dig += y[checker]
                    if checker == len(y) - 1:
                        sprite = checker
                        break
                else:
                    sprite = checker
                    break
        if this_dig != "":
            counted = False
            for i in range(my_y - 1, my_y + 2):
                if i < 0 or i >= len(raw):  # or counted == True:
                    continue
                else:
                    for j in range(sprite - len(this_dig) - 1, sprite + 1):
                        if j < 0 or j >= len(y):
                            continue
                        elif raw[i][j] == "*":
                            help_digs += [
                                [
                                    this_dig,
                                    [my_y, sprite - len(this_dig)],
                                    [i, j],
                                    raw[i][j],
                                ]
                            ]
                            counted = True
                            count_digs += [int(this_dig)]
                            break

            digs += [this_dig]
        sprite += 1
    my_y += 1

# print(digs)
# print(count_digs)
# print(sum(count_digs))

# print(len(digs), len(count_digs))

print(help_digs)

gears = {}

for x in help_digs:
    if f"{x[2]}" not in gears:
        gears[f"{x[2]}"] = [int(x[0])]
    else:
        gears[f"{x[2]}"] += [int(x[0])]

print(gears)
print(len(gears))

to_remove = []

ratios = 0

for x in gears:
    if len(gears[x]) != 2:
        to_remove += [x]
    else:
        ratios += gears[x][0] * gears[x][1]

for x in to_remove:
    gears.pop(x)

print(len(gears))

print(ratios)
