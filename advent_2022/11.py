from math import floor
import re

# %% 1

raw = []

with open("advent_2022/11.txt", "r") as file:
    raw = [x.strip() for x in file]

print(raw)

# monkeys = {}

# for i in range(len(raw)):
#     if raw[i][:6] == "Monkey":
#         monkey = raw[i].split()[1].strip(":")
#         items = [int(x) for x in raw[i + 1].split(":")[1].split(",")]
#         operation = (
#             "(" + raw[i + 2].split(":")[1].replace("new = ", "").strip() + ") / 3"
#         )
#         test = int(raw[i + 3].split()[-1])
#         if_true = raw[i + 4][-1]
#         if_false = raw[i + 5][-1]
#         print(monkey, items, operation, test, if_true, if_false)
#         monkeys[monkey] = {
#             "items": items,
#             "operation": operation,
#             "test": test,
#             "if_true": if_true,
#             "if_false": if_false,
#             "business": 0,
#         }
# print("")
# print(monkeys)

# for turn in range(20):
#     for m in monkeys:
#         for i in monkeys[m]["items"]:
#             final_worry = floor(eval(monkeys[m]["operation"].replace("old", str(i))))
#             if final_worry % monkeys[m]["test"] == 0:
#                 monkeys[f"{monkeys[m]['if_true']}"]["items"] += [final_worry]
#             else:
#                 monkeys[f"{monkeys[m]['if_false']}"]["items"] += [final_worry]

#             monkeys[m]["business"] += 1
#             monkeys[m]["items"] = monkeys[m]["items"][1:]
# print("")
# print(monkeys)

# business = [0, 0]

# top_two = ["0", "0"]

# for m in monkeys:
#     this_business = monkeys[m]["business"]
#     if this_business >= business[0]:
#         business[1] = business[0]
#         business[0] = this_business
#         top_two[1] = top_two[0]
#         top_two[0] = m
#     elif this_business >= business[1]:
#         business[1] = this_business
#         top_two[1] = m

# print(business, business[0] * business[1])
# print(top_two)

# %% 2

monkeys = {}

for i in range(len(raw)):
    if raw[i][:6] == "Monkey":
        monkey = raw[i].split()[1].strip(":")
        items = [int(x) for x in raw[i + 1].split(":")[1].split(",")]
        operation = (
            "("
            + raw[i + 2].split(":")[1].replace("new = ", "").strip()
            + ")"  # Do not divide by 3
        )
        test = int(raw[i + 3].split()[-1])
        if_true = raw[i + 4][-1]
        if_false = raw[i + 5][-1]
        print(monkey, items, operation, test, if_true, if_false)
        monkeys[monkey] = {
            "items": items,
            "operation": operation,
            "test": test,
            "if_true": if_true,
            "if_false": if_false,
            "business": 0,
        }
print("")
print(monkeys)

lcm = 1
for m in monkeys:
    lcm = lcm * monkeys[m]["test"]

for turn in range(10000):
    for m in monkeys:
        for i in monkeys[m]["items"]:
            final_worry = eval(monkeys[m]["operation"].replace("old", str(i)))
            if final_worry > lcm:
                final_worry = final_worry % lcm
            if final_worry % monkeys[m]["test"] == 0:
                monkeys[f"{monkeys[m]['if_true']}"]["items"] += [final_worry]
            else:
                monkeys[f"{monkeys[m]['if_false']}"]["items"] += [final_worry]

            monkeys[m]["business"] += 1
            monkeys[m]["items"] = monkeys[m]["items"][1:]
print("")
print(monkeys)

business = [0, 0]

top_two = ["0", "0"]

for m in monkeys:
    this_business = monkeys[m]["business"]
    if this_business >= business[0]:
        business[1] = business[0]
        business[0] = this_business
        top_two[1] = top_two[0]
        top_two[0] = m
    elif this_business >= business[1]:
        business[1] = this_business
        top_two[1] = m

print(business, business[0] * business[1])
print(top_two)
