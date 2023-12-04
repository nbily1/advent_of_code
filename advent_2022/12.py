# %% 1

raw = []

with open("dev/advent_2022/12.txt", "r") as file:
    raw = [x.strip() for x in file]

# print(raw)

letters = "abcdefghijklmnopqrstuvwxyz"

alts = {"S": 1, "E": 26}
for i in range(len(letters)):
    alts[letters[i]] = i + 1
# print(alts)

spots = {}
tot_spots = len(raw) * len(raw[0])
filled_spots = 1

e_spot = ""

# for y in range(len(raw)):
#     for x in range(len(raw[y])):
#         pos = f"{y},{x}"
#         spots[pos] = {"moves": 0 if raw[y][x] == "S" else None, "alt": alts[raw[y][x]]}

#         if raw[y][x] == "E":
#             e_spot = f"{y},{x}"

# # print(spots)

# while filled_spots < tot_spots and spots[e_spot]["moves"] == None:
#     temp_moves = {}
#     for y in range(len(raw)):
#         for x in range(len(raw[y])):
#             pos = f"{y},{x}"

#             if spots[f"{y},{x}"]["moves"] != None:
#                 continue

#             this_alt = spots[f"{y},{x}"]["alt"]

#             shortest = None

#             try:
#                 up_pos = spots[f"{int(y-1)},{x}"]
#                 if up_pos["alt"] >= this_alt - 1 and up_pos["moves"] != None:
#                     if shortest == None:
#                         shortest = up_pos["moves"] + 1
#                     else:
#                         shortest = min(shortest, up_pos["moves"] + 1)
#             except:
#                 pass

#             try:
#                 down_pos = spots[f"{int(y+1)},{x}"]
#                 if down_pos["alt"] >= this_alt - 1 and down_pos["moves"] != None:
#                     if shortest == None:
#                         shortest = down_pos["moves"] + 1
#                     else:
#                         shortest = min(shortest, down_pos["moves"] + 1)
#             except:
#                 pass

#             try:
#                 left_pos = spots[f"{y},{int(x-1)}"]
#                 if left_pos["alt"] >= this_alt - 1 and left_pos["moves"] != None:
#                     if shortest == None:
#                         shortest = left_pos["moves"] + 1
#                     else:
#                         shortest = min(shortest, left_pos["moves"] + 1)
#             except:
#                 pass

#             try:
#                 right_pos = spots[f"{y},{int(x+1)}"]
#                 if right_pos["alt"] >= this_alt - 1 and right_pos["moves"] != None:
#                     if shortest == None:
#                         shortest = right_pos["moves"] + 1
#                     else:
#                         shortest = min(shortest, right_pos["moves"] + 1)
#             except:
#                 pass

#             if shortest != None:
#                 temp_moves[f"{y},{x}"] = shortest
#                 filled_spots += 1

#     for t in temp_moves:
#         spots[t]["moves"] = temp_moves[t]
#     print(filled_spots, tot_spots)

# print(spots[e_spot]["moves"])


# %% 2

spots = {}
tot_spots = len(raw) * len(raw[0])
filled_spots = 1

e_spot = ""

for y in range(len(raw)):
    for x in range(len(raw[y])):
        pos = f"{y},{x}"
        spots[pos] = {"moves": 0 if raw[y][x] == "S" else None, "alt": alts[raw[y][x]]}
        if raw[y][x] == "a":
            spots[pos]["moves"] = 0
            filled_spots += 1

        if raw[y][x] == "E":
            e_spot = f"{y},{x}"

# print(spots)

while filled_spots < tot_spots and spots[e_spot]["moves"] == None:
    temp_moves = {}
    for y in range(len(raw)):
        for x in range(len(raw[y])):
            pos = f"{y},{x}"

            if spots[f"{y},{x}"]["moves"] != None:
                continue

            this_alt = spots[f"{y},{x}"]["alt"]

            shortest = None

            try:
                up_pos = spots[f"{int(y-1)},{x}"]
                if up_pos["alt"] >= this_alt - 1 and up_pos["moves"] != None:
                    if shortest == None:
                        shortest = up_pos["moves"] + 1
                    else:
                        shortest = min(shortest, up_pos["moves"] + 1)
            except:
                pass

            try:
                down_pos = spots[f"{int(y+1)},{x}"]
                if down_pos["alt"] >= this_alt - 1 and down_pos["moves"] != None:
                    if shortest == None:
                        shortest = down_pos["moves"] + 1
                    else:
                        shortest = min(shortest, down_pos["moves"] + 1)
            except:
                pass

            try:
                left_pos = spots[f"{y},{int(x-1)}"]
                if left_pos["alt"] >= this_alt - 1 and left_pos["moves"] != None:
                    if shortest == None:
                        shortest = left_pos["moves"] + 1
                    else:
                        shortest = min(shortest, left_pos["moves"] + 1)
            except:
                pass

            try:
                right_pos = spots[f"{y},{int(x+1)}"]
                if right_pos["alt"] >= this_alt - 1 and right_pos["moves"] != None:
                    if shortest == None:
                        shortest = right_pos["moves"] + 1
                    else:
                        shortest = min(shortest, right_pos["moves"] + 1)
            except:
                pass

            if shortest != None:
                temp_moves[f"{y},{x}"] = shortest
                filled_spots += 1

    for t in temp_moves:
        spots[t]["moves"] = temp_moves[t]
    print(filled_spots, tot_spots)

print(spots[e_spot]["moves"])
