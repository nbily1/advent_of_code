# %% Part 1
my_list = []

with open("advent_2024/01.txt", "r") as file:
    my_list = [[int(y) for y in x.strip().split()] for x in file]

# print(my_list)

l_list = [x[0] for x in my_list]
r_list = [x[1] for x in my_list]

l_list.sort()
r_list.sort()

# print(l_list, r_list)

tot_diff = 0

for i in range(len(l_list)):
    diff = r_list[i] - l_list[i]

    tot_diff += abs(diff)

print(tot_diff)

# %% Part 2
my_list = []

with open("advent_2024/01.txt", "r") as file:
    my_list = [[int(y) for y in x.strip().split()] for x in file]

# print(my_list)

l_list = [x[0] for x in my_list]
r_list = [x[1] for x in my_list]

tot_sim = 0

for x in l_list:
    sim = x * len([y for y in r_list if y == x])
    tot_sim += sim

print(tot_sim)
