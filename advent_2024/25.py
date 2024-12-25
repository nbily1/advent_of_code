# %% Part 1

with open("advent_2024/25.txt", "r") as file:
    my_list = [x.split("\n") for x in file.read().split("\n\n")]

# print(my_list)

locks = []
keys = []

for x in my_list:
    this_map = []
    if x[0] == "#####":
        for i in range(len(x[0])):
            this_map += [[y[i] for y in x].count(".")]
        locks += [this_map]
    elif x[-1] == "#####":
        for i in range(len(x[0])):
            this_map += [[y[i] for y in x].count("#")]
        keys += [this_map]

# print("locks", locks)
# print("keys", keys)

fits = 0
for lo in locks:
    for k in keys:
        if min([lo[i] - k[i] for i in range(len(lo))]) >= 0:
            fits += 1

print(fits)
