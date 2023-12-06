# %% 1

raw = []

with open("advent_2023/6.txt", "r") as file:
    raw = [
        [int(y) for y in x.split(":")[1].strip().split()]
        for x in file
        if x.strip() != ""
    ]

print(raw)

winners = []

for i in range(len(raw[0])):
    record = raw[1][i]
    time_limit = raw[0][i]
    this_winners = []
    for m in range(raw[0][i]):
        dist = (time_limit - m) * m
        if dist > record:
            this_winners += [[m, dist]]
    if len(this_winners) > 0:
        winners += [len(this_winners)]

print(winners)
answer = 1
for x in winners:
    answer = answer * x

print(answer)

# %% 2

raw = []

with open("advent_2023/6.txt", "r") as file:
    raw = [
        [int(x.split(":")[1].strip().replace(" ", ""))] for x in file if x.strip() != ""
    ]

print(raw)

winners = []

for i in range(len(raw[0])):
    record = raw[1][i]
    time_limit = raw[0][i]
    this_winners = []
    for m in range(raw[0][i]):
        dist = (time_limit - m) * m
        if dist > record:
            this_winners += [[m, dist]]

    if len(this_winners) > 0:
        winners += [len(this_winners)]

print(winners)
answer = 1
for x in winners:
    answer = answer * x

print(answer)
