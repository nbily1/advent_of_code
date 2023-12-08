# %% 1

raw = []
inst = ""

with open("advent_2023/8.txt", "r") as file:
    raw = [x.strip() for x in file if x.strip() != ""]

inst = [int(x) for x in raw[0].replace("L", "0").replace("R", "1")]
raw = raw[1:]

mydict = {}
for x in raw:
    thiskey = x.split("=")[0].strip()
    thisvals = [
        y.strip()
        for y in x.split("=")[1].strip().replace("(", "").replace(")", "").split(",")
    ]
    mydict[thiskey] = thisvals

# print(inst)
# print(mydict)

curr_pos = "AAA"
target = "ZZZ"
moves = 0
curr_inst = 0

while curr_pos != target:
    moves += 1
    curr_pos = mydict[curr_pos][inst[curr_inst]]
    curr_inst = (curr_inst + 1) % len(inst)

print(moves)

# %% 2
from math import lcm

curr_pos = [x for x in mydict if x[-1] == "A"]
target = "Z"
moves = 0
curr_inst = 0
is_finished = False

print(curr_pos)

moves = []

for this_cur_pos in curr_pos:
    this_moves = 0
    curr_inst = 0
    while this_cur_pos[-1] != target:
        this_moves += 1
        this_cur_pos = mydict[this_cur_pos][inst[curr_inst]]
        curr_inst = (curr_inst + 1) % len(inst)
    moves += [this_moves]

print(moves)
print(lcm(*moves))
