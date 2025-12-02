from math import floor

# %% Part 1

with open("advent_2024/22.txt", "r") as file:
    my_list = [int(x.strip()) for x in file]

print(my_list)

outlist = []

for sn in my_list:
    nsn = sn
    for _ in range(2000):
        nsn = ((nsn * 64) ^ nsn) % 16777216
        nsn = (floor(nsn / 32) ^ nsn) % 16777216
        nsn = ((nsn * 2048) ^ nsn) % 16777216
    # print(nsn)
    outlist += [nsn]

print("\n", sum(outlist))

# %% Part 2

# with open("advent_2024/22.txt", "r") as file:
#     my_list = [int(x.strip()) for x in file]

# print(my_list)

# outlist = []
# last_digs = []
# diffs = []
# patts = []

# for i in range(len(my_list)):

#     nsn = my_list[i]

#     outlist += [[nsn]]
#     last_digs += [[int(str(nsn)[-1])]]
#     diffs += [[0]]
#     patts += [[[0, 0, 0, 0]]]

#     for _ in range(2000):
#         nsn = ((nsn * 64) ^ nsn) % 16777216
#         nsn = (floor(nsn / 32) ^ nsn) % 16777216
#         nsn = ((nsn * 2048) ^ nsn) % 16777216
#         # print(nsn)
#         outlist[i] += [nsn]
#         last_digs[i] += [int(str(nsn)[-1])]
#         try:
#             diffs[i] += [last_digs[i][-1] - last_digs[i][-2]]
#         except IndexError:
#             pass
#         try:
#             patts[i] += [[diffs[i][-4], diffs[i][-3], diffs[i][-2], diffs[i][-1]]]
#         except IndexError:
#             patts[i] += [[0, 0, 0, 0]]

# print(outlist)
# print(last_digs)
# print(diffs)
# print(patts)

# unq_patts = []
# for p in patts:
#     for i in range(5, len(p)):
#         if p[i] not in unq_patts:
#             unq_patts += [p[i]]

# print(unq_patts)

# best_patt = []
# best_sum = 0
# for u in unq_patts:
#     ticker = 4
#     this_sum = 0
#     for p in range(len(patts)):
#         try:
#             i2 = patts[p].index(u, ticker)
#             ticker = i2
#             this_sum += last_digs[p][i2]
#         except ValueError:
#             pass
#     if this_sum > best_sum:
#         best_sum = this_sum
#         best_patt = u

# print(best_patt)
# print(best_sum)
