# %% 1

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priorities = {}
for x in range(len(letters)):
    priorities[letters[x]] = x + 1

sack_list = []

with open("dev/advent_2022/3.txt", "r") as file:
    sack_list = [x.strip() for x in file]

commons = []

for x in sack_list:
    divider = int((len(x)) / 2)
    commons.append([y for y in x[:divider] if y in [z for z in x[divider:]]][0])

print(commons)

tot_score = 0

for x in commons:
    tot_score += priorities[x]

print(tot_score)

# %% 2

commons = []
for i in range(0, len(sack_list), 3):
    i0 = i
    i1 = i + 1
    i2 = i + 2
    commons.append(
        [
            y
            for y in sack_list[i0]
            if y in [z for z in sack_list[i1]] and y in [z for z in sack_list[i2]]
        ][0]
    )

print(commons)

tot_score = 0

for x in commons:
    tot_score += priorities[x]

print(tot_score)
