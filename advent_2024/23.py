from itertools import combinations

# %% Part 1

with open("advent_2024/23.txt", "r") as file:
    my_list = [x.strip().split("-") for x in file]

# print(my_list)

conn_list = []
for c in range(len(my_list)):
    first = my_list[c]
    for c2 in range(c + 1, len(my_list)):
        second = my_list[c2]
        if first[0] in second or first[1] in second:
            this_set = list(set(first + second))
            this_set.sort()
        else:
            continue
        for c3 in range(c2 + 1, len(my_list)):
            third = my_list[c3]
            if third[0] in this_set and third[1] in this_set:
                pass
            else:
                continue
            if this_set not in conn_list and (
                this_set[0][0] == "t" or this_set[1][0] == "t" or this_set[2][0] == "t"
            ):
                conn_list += [this_set]

conn_list.sort()
print(len(conn_list))

# %% Part 2

with open("advent_2024/23.txt", "r") as file:
    my_list = [x.strip().split("-") for x in file]

# print(my_list)

my_dict = {}

best_rslt = []

for x in my_list:
    if x[0] not in my_dict:
        my_dict[x[0]] = {"list": [x[0], x[1]]}
    else:
        my_dict[x[0]]["list"] += [x[1]]

    if x[1] not in my_dict:
        my_dict[x[1]] = {"list": [x[0], x[1]]}
    else:
        my_dict[x[1]]["list"] += [x[0]]

for k in my_dict:
    # print(k)
    this_list = my_dict[k]["list"]

    my_dict[k]["combs"] = []

    for i in range(len(this_list)):
        my_dict[k]["combs"] = list(
            set([tuple(set(x)) for x in list(combinations(this_list, i))])
        )

    # my_dict[k]["combs"] = my_dict[k]["combs"][1:]

    for c in my_dict[k]["combs"]:
        eval_str = ""
        for d in c:
            eval_str += f"set(my_dict['{d}']['list'])&"

        eval_str = eval_str[:-1]

        outlist = eval(eval_str)
        if len(outlist) > len(best_rslt):
            best_rslt = list(outlist.copy())


# print(my_dict)
best_rslt.sort()
print(best_rslt)
print(",".join(best_rslt))
