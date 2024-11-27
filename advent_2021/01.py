# %% Part 1
my_list = []

with open("advent_2021/01.txt", "r") as file:
    my_list = [int(x.strip()) for x in file]

# print(my_list)

prev_val = 0
curr_val = 0

increased = 0

for x in my_list:
    if x > prev_val and prev_val != 0:
        increased += 1

    prev_val = x

print(increased)


# %% Part 2
my_list = []

with open("advent_2021/01.txt", "r") as file:
    my_list = [int(x.strip()) for x in file]

# print(my_list)

my_comb_list = []

for i in range(len(my_list)):
    if i <= len(my_list) - 3:
        my_comb_list += [my_list[i] + my_list[i + 1] + my_list[i + 2]]

print(my_comb_list)

prev_val = 0
curr_val = 0

increased = 0

for x in my_comb_list:
    if x > prev_val and prev_val != 0:
        increased += 1

    prev_val = x

print(increased)
