# %% Part 1

with open("advent_2024/08.txt", "r") as file:
    my_list = [[y for y in x.strip()] for x in file]

# print(my_list)

freqs = []

max_y = len(my_list)
max_x = len(my_list[0])

for y in range(max_y):
    freqs += [x for x in list(set(my_list[y])) if x not in freqs and x != "."]

# print(freqs)

freq_dict = {f: {"antennas": [], "antinodes": []} for f in freqs}

for y in range(max_y):
    for x in range(max_x):
        this_val = my_list[y][x]

        if this_val != ".":
            freq_dict[this_val]["antennas"] += [[y, x]]

# print(freq_dict)

unq_antinodes = []

for f in freq_dict:
    this_antennas = freq_dict[f]["antennas"]

    for i in range(len(this_antennas)):
        a = this_antennas[i]
        for j in range(i + 1, len(this_antennas)):  # noqa:E203
            a0 = this_antennas[j]
            if a0 == a:
                continue

            y_diff = a[0] - a0[0]
            x_diff = a[1] - a0[1]

            an1 = [a[0] + y_diff, a[1] + x_diff]
            an2 = [a0[0] - y_diff, a0[1] - x_diff]

            if (
                an1 not in freq_dict[f]["antinodes"]
                and an1[0] >= 0
                and an1[1] >= 0
                and an1[0] < max_y
                and an1[1] < max_x
            ):
                freq_dict[f]["antinodes"] += [an1]
                if an1 not in unq_antinodes:
                    unq_antinodes += [an1]
            if (
                an2 not in freq_dict[f]["antinodes"]
                and an2[0] >= 0
                and an2[1] >= 0
                and an2[0] < max_y
                and an2[1] < max_x
            ):
                freq_dict[f]["antinodes"] += [an2]
                if an2 not in unq_antinodes:
                    unq_antinodes += [an2]

# print(freq_dict)
# print(unq_antinodes)
print(len(unq_antinodes))


# %% Part 2

with open("advent_2024/08.txt", "r") as file:
    my_list = [[y for y in x.strip()] for x in file]

# print(my_list)

freqs = []

max_y = len(my_list)
max_x = len(my_list[0])

for y in range(max_y):
    freqs += [x for x in list(set(my_list[y])) if x not in freqs and x != "."]

# print(freqs)

freq_dict = {f: {"antennas": [], "antinodes": []} for f in freqs}

for y in range(max_y):
    for x in range(max_x):
        this_val = my_list[y][x]

        if this_val != ".":
            freq_dict[this_val]["antennas"] += [[y, x]]

# print(freq_dict)

unq_antinodes = []

for f in freq_dict:
    this_antennas = freq_dict[f]["antennas"]

    for i in range(len(this_antennas)):
        a = this_antennas[i]
        for j in range(i + 1, len(this_antennas)):  # noqa:E203
            a0 = this_antennas[j]
            if a0 == a:
                continue

            y_diff = a[0] - a0[0]
            x_diff = a[1] - a0[1]

            # print(a, a0, y_diff, x_diff)

            an1 = a
            an2 = a0

            while an1[0] >= 0 and an1[1] >= 0 and an1[0] < max_y and an1[1] < max_x:

                if (
                    an1 not in freq_dict[f]["antinodes"]
                    and an1[0] >= 0
                    and an1[1] >= 0
                    and an1[0] < max_y
                    and an1[1] < max_x
                ):
                    freq_dict[f]["antinodes"] += [an1]
                    if an1 not in unq_antinodes:
                        unq_antinodes += [an1]

                an1 = [an1[0] + y_diff, an1[1] + x_diff]

            while an2[0] >= 0 and an2[1] >= 0 and an2[0] < max_y and an2[1] < max_x:
                if (
                    an2 not in freq_dict[f]["antinodes"]
                    and an2[0] >= 0
                    and an2[1] >= 0
                    and an2[0] < max_y
                    and an2[1] < max_x
                ):
                    freq_dict[f]["antinodes"] += [an2]
                    if an2 not in unq_antinodes:
                        unq_antinodes += [an2]

                an2 = [an2[0] - y_diff, an2[1] - x_diff]


# print(freq_dict)
# print(unq_antinodes)
print(len(unq_antinodes))
