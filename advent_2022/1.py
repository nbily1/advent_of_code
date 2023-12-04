# %% 1

elf_list = []
elf_dict = {"1": 0}

with open("dev/advent_2022/1.txt", "r") as file:
    elf_list = [x.strip() for x in file.readlines()]

elf_id = 1
max_elf = 1
max_elf_val = 0

for x in elf_list:
    if x != "":
        elf_dict[f"{elf_id}"] += int(x)
    else:
        if elf_dict[f"{elf_id}"] > max_elf_val:
            max_elf = elf_id
            max_elf_val = elf_dict[f"{elf_id}"]
        elf_id += 1
        elf_dict[f"{elf_id}"] = 0
        continue

# print(elf_list)
print(elf_dict)
print(max_elf, max_elf_val)

# %% 2

top3_elf = [0, 0, 0]
top3_elf_val = [0, 0, 0]

for x in elf_dict:
    if elf_dict[x] > top3_elf_val[0]:
        top3_elf_val[2] = top3_elf_val[1]
        top3_elf[2] = top3_elf[1]
        top3_elf_val[1] = top3_elf_val[0]
        top3_elf[1] = top3_elf[0]
        top3_elf_val[0] = elf_dict[x]
        top3_elf[0] = x
    elif elf_dict[x] > top3_elf_val[1]:
        top3_elf_val[2] = top3_elf_val[1]
        top3_elf[2] = top3_elf[1]
        top3_elf_val[1] = elf_dict[x]
        top3_elf[1] = x
    elif elf_dict[x] > top3_elf_val[2]:
        top3_elf_val[2] = elf_dict[x]
        top3_elf[2] = x

print(top3_elf, top3_elf_val)

tot_score = 0
for x in top3_elf_val:
    tot_score += x

print(tot_score)
