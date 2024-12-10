# %% Part 1

with open("advent_2024/09.txt", "r") as file:
    my_list = [y for y in [x.strip() for x in file][0]]

# print(my_list)

is_file = True
file_id = 0
my_list1 = []

for i in range(len(my_list)):
    if is_file:
        my_list1 += [str(file_id)] * int(my_list[i])
        file_id += 1
        is_file = False
    else:
        my_list1 += ["."] * int(my_list[i])
        is_file = True

# print(my_list1)

outlist = my_list1

ticker = 0
while ticker < len(outlist):
    recheck = False
    while outlist[-1] == ".":
        outlist = outlist[:-1]
        recheck = True
    if recheck:
        continue

    if outlist[ticker] == ".":
        outlist[ticker] = outlist.pop(-1)
    ticker += 1

# print(outlist[:30])

checksum = 0
for i in range(len(outlist)):
    checksum += i * int(outlist[i])

print(checksum)


# %% Part 2

with open("advent_2024/09.txt", "r") as file:
    my_list = [y for y in [x.strip() for x in file][0]]

# print(my_list)

is_file = True
file_id = 0
my_list1 = []

for i in range(len(my_list)):
    if is_file:
        if int(my_list[i]) > 0:
            my_list1 += [[str(file_id)] * int(my_list[i])]
        file_id += 1
        is_file = False
    else:
        if int(my_list[i]) > 0:
            my_list1 += [["."] * int(my_list[i])]
        is_file = True

# print(my_list1[:30])
# print(my_list1[-30:])

outlist = my_list1

backticker = -1

while backticker > -len(outlist):

    if outlist[backticker][0] == "." or len(outlist[backticker]) >= 10:
        backticker -= 1

    ticker = 0

    while ticker < len(outlist) + backticker:

        if outlist[ticker][0] == ".":
            if (
                len(outlist[backticker]) <= len(outlist[ticker])
                and outlist[backticker][0] != "."
            ):
                diff = len(outlist[ticker]) - len(outlist[backticker])
                outlist[ticker] = outlist[backticker]
                outlist[backticker] = ["."] * len(outlist[backticker])
                if diff > 0:
                    outlist.insert(ticker + 1, ["."] * diff)
                break
        ticker += 1

        if ticker >= len(outlist) + backticker:
            break

    backticker -= 1

# print(outlist[:30])
# print(outlist[-30:])

final_list = []

for x in outlist:
    final_list += x

# print(final_list[:30])
# print(final_list[-30:])

checksum = 0
for i in range(len(final_list)):
    try:
        checksum += i * int(final_list[i])
    except Exception:
        pass

print(checksum)
