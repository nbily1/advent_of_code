# %% 1

raw = []

with open("advent_2023/7.txt", "r") as file:
    raw = [x.strip().split() for x in file if x.strip() != ""]

print(raw)


def eval_hand(inp: str) -> int:
    rtn_val = 0

    card_rnk = "23456789TJQKA"

    adder = 0

    for i in range(len(inp)):
        rtn_val += 0.01 / (1000**i) * (card_rnk.index(inp[i]) + 1)

    inp = sorted(inp)

    matches = ""
    sprite = 0
    while sprite < 5:
        checker = inp[sprite]
        repeats = 1
        for i in range(sprite + 1, 5):
            if inp[i] == checker:
                repeats += 1
                sprite += 1
        matches += f"{repeats}"
        sprite += 1

    if matches == "5":
        rtn_val += 7
    elif "4" in matches:
        rtn_val += 6
    elif matches in ["32", "23"]:
        rtn_val += 5
    elif "3" in matches:
        rtn_val += 4
    elif "22" in "".join(sorted(matches)):
        rtn_val += 3
    elif "2" in matches:
        rtn_val += 2
    else:
        rtn_val += 1

    return rtn_val


for i in range(len(raw)):
    raw[i][1] = int(raw[i][1])
    raw[i] += [eval_hand(raw[i][0])]

values = sorted([x[2] for x in raw])
for i in range(len(raw)):
    raw[i] += [values.index(raw[i][2]) + 1]

tot_value = 0
for x in raw:
    tot_value += x[1] * x[3]

print(raw)
print(tot_value)


# %% 2

raw = []

with open("advent_2023/7.txt", "r") as file:
    raw = [x.strip().split() for x in file if x.strip() != ""]

print(raw)


def eval_hand(inp: str) -> int:
    rtn_val = 0

    card_rnk = "J23456789TQKA"

    adder = 0

    for i in range(len(inp)):
        rtn_val += 0.01 / (1000**i) * (card_rnk.index(inp[i]) + 1)

    inp = sorted(inp)
    js = len([x for x in inp if x == "J"])

    matches = ""
    sprite = 0
    while sprite < 5:
        checker = inp[sprite]
        if checker == "J":
            sprite += 1
            continue
        repeats = 1
        for i in range(sprite + 1, 5):
            if inp[i] == checker:
                repeats += 1
                sprite += 1
        matches += f"{repeats}"
        sprite += 1

    matches = sorted(matches, reverse=True)
    try:
        matches[0] = str(int(matches[0]) + js)
    except IndexError:  # This means we got all Js
        matches = "5"

    if "5" in matches:
        rtn_val += 7
    elif "4" in matches:
        rtn_val += 6
    elif "".join(matches) in ["32", "23"]:
        rtn_val += 5
    elif "3" in matches:
        rtn_val += 4
    elif "22" in "".join(sorted(matches)):
        rtn_val += 3
    elif "2" in matches:
        rtn_val += 2
    else:
        rtn_val += 1

    return rtn_val


for i in range(len(raw)):
    raw[i][1] = int(raw[i][1])
    raw[i] += [eval_hand(raw[i][0])]

values = sorted([x[2] for x in raw])
for i in range(len(raw)):
    raw[i] += [values.index(raw[i][2]) + 1]

tot_value = 0
for x in raw:
    tot_value += x[1] * x[3]

# print(raw)
print(tot_value)
