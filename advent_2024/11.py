import functools


@functools.cache
def proc_stone(s: int):
    new_stones = []
    if s == 0:
        new_stones += [1]
    elif len(str(s)) % 2 == 0:
        str_s = str(s)
        ind = int(len(str_s) / 2)
        new_stones += [int(str_s[:ind]), int(str_s[ind:])]
    else:
        new_stones += [s * 2024]

    return new_stones


# %% Part 1

with open("advent_2024/11.txt", "r") as file:
    my_list = [int(x.strip()) for x in file.readline().split()]

print(my_list)

blink = 1

stones = my_list.copy()

while blink <= 25:
    new_stones = []
    for s in stones:
        new_stones += proc_stone(s)
    # print(new_stones)
    stones = new_stones.copy()
    if blink % 5 == 0:
        print(f"blinked {blink} times", len(stones))
    blink += 1

print(len(stones))

# %% Part 2

with open("advent_2024/11.txt", "r") as file:
    my_list = {int(x.strip()): 1 for x in file.readline().split()}

print(my_list)

blink = 1

stones = my_list.copy()

while blink <= 75:
    new_stones_dict = {}
    for s in stones:
        new_stones = proc_stone(s)
        for ns in set(new_stones):
            if ns in new_stones_dict:
                new_stones_dict[ns] += new_stones.count(ns) * stones[s]
            else:
                new_stones_dict[ns] = new_stones.count(ns) * stones[s]
    # print(new_stones_dict)
    stones = new_stones_dict.copy()
    if blink % 5 == 0:
        print(f"blinked {blink} times", sum(stones.values()))
    blink += 1


print(sum(stones.values()))
