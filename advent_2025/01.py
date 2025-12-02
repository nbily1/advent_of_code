# %% Part 1
my_list = []

with open("advent_2025/01.txt", "r") as file:
    my_list = [(1 if x[0] == "R" else -1) * int(x[1:]) for x in file]

# print(my_list)

current_spot = 50
dial_len = 100
counter = 0

for x in my_list:
    if x > 0:
        current_spot = (current_spot + x) % dial_len
    else:
        current_spot = (current_spot + 100 + x) % dial_len

    if current_spot == 0:
        counter += 1

print(counter)


# %% Part 2
my_list = []

with open("advent_2025/01.txt", "r") as file:
    my_list = [(1 if x[0] == "R" else -1) * int(x[1:]) for x in file]

# print(my_list)

current_spot = 50
dial_len = 100
counter = 0

for x in my_list:
    old_spot = current_spot
    new_spot = current_spot + x

    # if new_spot <= 0 or new_spot > 99:
    #     counter += 1 + abs(x) // 100
    if new_spot > 99:
        counter += new_spot // 100
    elif new_spot <= 0:
        counter += (1 if old_spot > 0 else 0) + (abs(new_spot) // 100)

    if x > 0:
        current_spot = (current_spot + x) % dial_len
    else:
        current_spot = (current_spot + 100 + x) % dial_len
    # print(old_spot, x, new_spot, current_spot, counter)

print(counter)
