# %% 1

instructions = []
stacks_raw = []

with open("advent_2022/05.txt", "r") as file:
    instructions = [x.strip() for x in file if x[:4] == "move"]

with open("advent_2022/05.txt", "r") as file:
    stacks_raw = [x.strip("\n") for x in file if x[:4] != "move"]

stacks = {
    "1": [],
    "2": [],
    "3": [],
    "4": [],
    "5": [],
    "6": [],
    "7": [],
    "8": [],
    "9": [],
}

for i in range(len(stacks_raw) - 3, -1, -1):
    for j in range(1, 10):
        jstart = 4 * (j - 1)
        jend = 4 * j
        thisval = [stacks_raw[i][jstart:jend].strip().strip("[").strip("]")]
        if thisval != [""]:
            stacks[f"{j}"] += thisval

print(stacks)

for x in instructions:
    ins_list = x.split()
    quant = -int(ins_list[1])
    from_stack = ins_list[3]
    to_stack = ins_list[5]

    moving = stacks[from_stack][quant:]
    moving.reverse()
    stacks[to_stack] += moving
    stacks[from_stack] = stacks[from_stack][:quant]

print(stacks)

answer = ""

for k in stacks:
    answer += stacks[k][-1]

print(answer)

# %% 2

stacks = {
    "1": [],
    "2": [],
    "3": [],
    "4": [],
    "5": [],
    "6": [],
    "7": [],
    "8": [],
    "9": [],
}

for i in range(len(stacks_raw) - 3, -1, -1):
    for j in range(1, 10):
        jstart = 4 * (j - 1)
        jend = 4 * j
        thisval = [stacks_raw[i][jstart:jend].strip().strip("[").strip("]")]
        if thisval != [""]:
            stacks[f"{j}"] += thisval

print(stacks)

for x in instructions:
    ins_list = x.split()
    quant = -int(ins_list[1])
    from_stack = ins_list[3]
    to_stack = ins_list[5]

    moving = stacks[from_stack][quant:]
    stacks[to_stack] += moving
    stacks[from_stack] = stacks[from_stack][:quant]

print(stacks)

answer = ""

for k in stacks:
    answer += stacks[k][-1]

print(answer)
