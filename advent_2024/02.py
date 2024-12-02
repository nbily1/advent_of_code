# %% Part 1
my_list = []

with open("advent_2024/02.txt", "r") as file:
    my_list = [[int(y) for y in x.strip().split()] for x in file]

# print(my_list)

tot_safe = 0

for x in my_list:

    is_safe = True

    if x[0] > x[1]:
        for i in range(len(x) - 1):
            if abs(x[i] - x[i + 1]) <= 3 and x[i] > x[i + 1]:
                continue
            else:
                is_safe = False
                break
    else:
        for i in range(len(x) - 1):
            if abs(x[i] - x[i + 1]) <= 3 and x[i] < x[i + 1]:
                continue
            else:
                is_safe = False
                break

    if is_safe:
        tot_safe += 1

print(tot_safe)

# %% Part 2
my_list = []

with open("advent_2024/02.txt", "r") as file:
    my_list = [[int(y) for y in x.strip().split()] for x in file]

# print(my_list)

tot_safe = 0

for x in my_list:

    # print(x)

    is_safe = True
    is_safe2 = True

    if x[0] > x[1]:
        for i in range(len(x) - 1):
            if abs(x[i] - x[i + 1]) <= 3 and x[i] > x[i + 1]:
                continue
            else:
                is_safe = False
                break
    else:
        for i in range(len(x) - 1):
            if abs(x[i] - x[i + 1]) <= 3 and x[i] < x[i + 1]:
                continue
            else:
                is_safe = False
                break

    if is_safe is False:
        for j in range(len(x)):
            new_x = x.copy()
            new_x.pop(j)
            # print(new_x)
            # new_x.remove(new_x(j))
            is_safe2 = False
            count_safe = 0

            if new_x[0] > new_x[1]:
                for i in range(len(new_x) - 1):
                    if abs(new_x[i] - new_x[i + 1]) <= 3 and new_x[i] > new_x[i + 1]:
                        count_safe += 1
                        continue
                    else:
                        break
            else:
                for i in range(len(new_x) - 1):
                    if abs(new_x[i] - new_x[i + 1]) <= 3 and new_x[i] < new_x[i + 1]:
                        count_safe += 1
                        continue
                    else:
                        break

            if count_safe == len(new_x) - 1:
                is_safe2 = True
                break

    # print(is_safe, is_safe2)

    if is_safe or is_safe2:
        tot_safe += 1

print(tot_safe)
