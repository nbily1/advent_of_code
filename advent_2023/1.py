# %% 1
import re

raw = []

with open("advent_2023/1.txt", "r") as file:
    raw = [x.strip() for x in file]

print(raw)

nums = []

for x in raw:
    dig = re.sub(r"[^\d]", "", x)
    # print(dig)
    nums += [int(dig[0] + dig[-1])]

print(nums)
print(sum(nums))

# %% 2
digs = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
}

nums = []

for x in raw:
    for i in range(50):
        y = x
        firstnum = 0
        lastnum = len(x)

        for j in range(len(x)):
            try:
                v = int(x[j])
                firstnum = j
                break
            except:
                pass

        for j in range(len(x), -1, -1):
            try:
                v = int(x[j])
                lastnum = j
                break
            except:
                pass

        for start in range(firstnum):
            for end in range(firstnum + 1):
                # print(x[start:end])
                if x[start:end] in digs:
                    matched = x[start:end]
                    y = x.replace(matched, digs[matched], 1)
                    break

        x = y

        for start in range(len(x), lastnum - 1, -1):
            for end in range(len(x), lastnum - 1, -1):
                # print(x[start:end])
                if x[start:end] in digs:
                    matched = x[start:end]
                    y = x.replace(matched, digs[matched], 1)
                    break
        x = y

    dig = re.sub(r"[^\d]", "", x)
    # print(dig)
    print(x, int(dig[0] + dig[-1]))
    nums += [int(dig[0] + dig[-1])]

print(nums)
print(sum(nums))
