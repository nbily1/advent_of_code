# %% 1

perms = {
    "A X": 1 + 3,
    "A Y": 2 + 6,
    "A Z": 3 + 0,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 1 + 6,
    "C Y": 2 + 0,
    "C Z": 3 + 3,
}

round_list = []

with open("advent_2022/2.txt", "r") as file:
    round_list = [x.strip() for x in file]

tot_score = 0

for x in round_list:
    tot_score += perms[x]

print(tot_score)

# %% 2

perms = {
    "A X": 3 + 0,
    "A Y": 1 + 3,
    "A Z": 2 + 6,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 2 + 0,
    "C Y": 3 + 3,
    "C Z": 1 + 6,
}

tot_score = 0

for x in round_list:
    tot_score += perms[x]

print(tot_score)
