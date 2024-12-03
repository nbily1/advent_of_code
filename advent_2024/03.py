import re

# %% Part 1

with open("advent_2024/03.txt", "r") as file:
    my_string = "".join([x for x in file])

# print(my_string)

patt = re.compile(pattern=r"mul\(\d{1,3},\d{1,3}\)")

matches = re.findall(pattern=patt, string=my_string)

# print(matches)

digs = re.compile(r"\d+")

nums = [re.findall(pattern=digs, string=x) for x in matches]

# print(nums)

result = sum([int(x[0]) * int(x[1]) for x in nums])

print(result)

# %% Part 1

with open("advent_2024/03.txt", "r") as file:
    my_string = "".join([x for x in file])

# print(my_string)

patt = re.compile(pattern=r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))")

matches = re.findall(pattern=patt, string=my_string)

# print(matches)

keepers = []

i = 0
tracker = True

for i in range(len(matches)):
    if matches[i] == "don't()":
        tracker = False
        continue
    if matches[i] == "do()":
        tracker = True
        continue

    if tracker is True:
        keepers += [matches[i]]

# print(keepers)

digs = re.compile(r"\d+")

nums = [re.findall(pattern=digs, string=x) for x in keepers]

# print(nums)

result = sum([int(x[0]) * int(x[1]) for x in nums])

print(result)
