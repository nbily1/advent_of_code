# %% 1
# import re
# import itertools

raw = []

with open("advent_2023/15.txt", "r") as file:
    raw = [[y for y in x.strip().split(",")] for x in file if x.strip() != ""]

raw = raw[0].copy()

# print(raw)

results = []

for i in raw:
    curr_val = 0

    # Determine the ASCII code for the current character of the string.
    this_patt = [ord(c) for c in i]
    # print(this_patt)

    for v in this_patt:
        # Increase the current value by the ASCII code you just determined.
        curr_val += v

        # Set the current value to itself multiplied by 17.
        curr_val *= 17

        # Set the current value to the remainder of dividing itself by 256.
        curr_val = curr_val % 256

    results += [curr_val]

print(results)
print(sum(results))

# %% 2
import re

boxes = {}
for i in range(256):
    boxes[i] = []

lenses = {x.replace("=", " "): None for x in raw if "=" in x}

print(lenses)

for i in raw:
    this_label = re.sub(r"[^a-z]", "", i)

    hash_val = 0
    # Determine the ASCII code for the current character of the string.
    this_patt = [ord(c) for c in this_label]
    # print(this_patt)
    for v in this_patt:
        # Increase the current value by the ASCII code you just determined.
        hash_val += v
        # Set the current value to itself multiplied by 17.
        hash_val *= 17
        # Set the current value to the remainder of dividing itself by 256.
        hash_val = hash_val % 256
    # print(hash_val)

    if "-" in i:
        for k in lenses:
            if re.sub(r"[^a-z]", "", k) == this_label and lenses[k] == hash_val:
                boxes[hash_val].remove(k)
                lenses[k] = None
                break
    else:
        this_lens = i.replace("=", " ")
        for l in range(len(boxes[hash_val])):
            if re.sub(r"[^a-z]", "", boxes[hash_val][l]) == this_label:
                lenses[boxes[hash_val][l]] = None
                boxes[hash_val].remove(boxes[hash_val][l])
                boxes[hash_val].insert(l, this_lens)
                break
        else:
            boxes[hash_val] += [this_lens]
        lenses[this_lens] = hash_val

print(lenses)
print(boxes)

results = []

for l in lenses:
    if lenses[l] == None:
        pass
    else:
        this_result = (
            (1 + lenses[l])
            * (1 + boxes[lenses[l]].index(l))
            * int(re.sub(r"[^\d]", "", l))
        )
        results += [this_result]

print(results)
print(sum(results))
