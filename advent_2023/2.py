# %% 1
import re

raw = []

with open("dev/advent_2023/2.txt", "r") as file:
    raw = [x.strip() for x in file]

print(raw)

games = {}

for x in raw:
    k = re.sub(r"[^\d]", "", x.split(":")[0])
    games[k] = []
    gms = x.split(":")[1].strip().split(";")
    for y in gms:
        games[k] += [{z.split()[1]: int(z.split()[0]) for z in y.split(",")}]

print(games)
cubes = {"red": 12, "green": 13, "blue": 14}

poss = []

for this_game in games:
    allowed = True
    for this_pull in games[this_game]:
        for z in this_pull:
            if this_pull[z] > cubes[z]:
                allowed = False
                break
        if allowed == False:
            break
    if allowed:
        poss += [int(this_game)]

print(poss)
print(sum(poss))

# %% 2

mins = []

for this_game in games:
    this_mins = {"red": 0, "green": 0, "blue": 0}
    for this_pull in games[this_game]:
        for z in this_pull:
            if this_pull[z] > this_mins[z]:
                this_mins[z] = this_pull[z]
    mins += [this_mins["red"] * this_mins["green"] * this_mins["blue"]]

print(mins)
print(sum(mins))
