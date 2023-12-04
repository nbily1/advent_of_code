# %% 1
import re

raw = []

with open("advent_2023/4.txt", "r") as file:
    raw = [x.strip() for x in file]

print(raw)

cards = {}

for x in raw:
    cards[re.sub(r"[^\d]", "", x.split(":")[0])] = [
        [int(y.strip()) for y in x.split(":")[1].split("|")[0].split(" ") if y != ""],
        [int(y.strip()) for y in x.split(":")[1].split("|")[1].split(" ") if y != ""],
        1,
    ]

print(cards)

# total_points = 0

# for k in cards:
#     card_points = 0
#     for n in cards[k][1]:
#         if n in cards[k][0]:
#             card_points += 1 if card_points == 0 else card_points
#     total_points += card_points

# print(total_points)

# %% 2

for k in cards:
    matches = 0
    for n in cards[k][1]:
        if n in cards[k][0]:
            matches += 1
    for m in range(matches):
        cards[f"{int(k) + m + 1}"][2] += cards[k][2]

total_cards = 0
for c in cards:
    total_cards += cards[c][2]

print(cards)

print(total_cards)
