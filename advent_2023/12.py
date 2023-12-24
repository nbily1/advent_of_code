# %% 1
# import re
# import itertools

# raw = []

# with open("advent_2023/12.txt", "r") as file:
#     raw = [[y for y in x.strip().split()] for x in file if x.strip() != ""]

# for i in range(len(raw)):
#     raw[i][1] = [int(x) for x in raw[i][1].split(",")]

# # print(raw)

# arrangs = []

# for x in raw:
#     springs = x[0]
#     patt = x[1]

#     poss = []
#     num_quests = len([q for q in springs if q == "?"])

#     opts = list(itertools.product(".#", repeat=num_quests))

#     this_match = r"^[^#]*"
#     for i in range(len(patt)):
#         this_match += (
#             r"#{" + f"{patt[i]}" + r"}" + (r"[^#]+" if i < len(patt) - 1 else r"[^#]*$")
#         )
#     # print(opts)
#     # print(this_match)

#     this_arrangs = 0
#     for opt in opts:
#         this_str = springs
#         for o in opt:
#             this_str = this_str.replace("?", o, 1)
#         if re.match(this_match, this_str):
#             this_arrangs += 1
#             # print(this_str)

#     arrangs += [this_arrangs]

# # print(arrangs)
# print(sum(arrangs))
