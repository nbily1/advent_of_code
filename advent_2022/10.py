# %% 1

reg_raw = []

with open("advent_2022/10.txt", "r") as file:
    reg_raw = [x.strip().split() for x in file]

cyc = []

for x in reg_raw:
    cyc += [0]
    if x[0] == "addx":
        cyc += [int(x[1])]

# print(reg_raw)
# print(cyc)

final = {"0": 1}

for i in range(len(cyc)):
    final[f"{i+1}"] = final[f"{i}"] + cyc[i]

print(final)

strength = 0

for i in range(20, 221, 40):
    strength += i * final[f"{i-1}"]
    print(i, final[f"{i-1}"])

print(strength)

# %% 2

for i in range(20, 221, 40):
    line = ""
    for c in range(40):
        if final[f"{c + i-20}"] >= c - 1 and final[f"{c + i-20}"] <= c + 1:
            line += "#"
        else:
            line += "."
    print(line)
