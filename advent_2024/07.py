import itertools

# %% Part 1

with open("advent_2024/07.txt", "r") as file:
    my_list = [x.replace(":", "").strip().split() for x in file]

# print(my_list)

my_dict = {}

for i in range(len(my_list)):
    my_dict[i] = {
        "answer": my_list[i][0],
        "operands": my_list[i][1:],
        "num_operators": len(my_list[i][1:]) - 1,
        "equals": 0,
    }

longest_list = max([len(x) - 2 for x in my_list])

# print(my_dict)

ops = ["*", "+"]

ops_combos = []

for i in range(1, longest_list + 1):
    ops_combos += list(itertools.product(ops, repeat=i))

# print(ops_combos)

true_test_values = []

for k in my_dict:
    this_answer = int(my_dict[k]["answer"])
    operands = my_dict[k]["operands"]
    num_operators = my_dict[k]["num_operators"]

    operators = [list(x) for x in ops_combos if len(x) == num_operators]

    # print(operators)
    # print(operands)

    found_a_match = False

    for o in operators:
        test_str = (
            "(" * num_operators
            + operands[0]
            + ")".join([o[i - 1] + operands[i] for i in range(1, num_operators + 1)])
            + ")"
        )

        # print(test_str)
        # continue

        if eval(test_str) == this_answer:
            found_a_match = True
            break

    if found_a_match:
        true_test_values += [this_answer]

# print(true_test_values)
print(sum(true_test_values))

# %% Part 1

with open("advent_2024/07.txt", "r") as file:
    my_list = [x.replace(":", "").strip().split() for x in file]

# print(my_list)

my_dict = {}

for i in range(len(my_list)):
    my_dict[i] = {
        "answer": my_list[i][0],
        "operands": my_list[i][1:],
        "num_operators": len(my_list[i][1:]) - 1,
        "equals": 0,
    }

longest_list = max([len(x) - 2 for x in my_list])

# print(my_dict)

ops = ["*", "+", "|"]

ops_combos = []

for i in range(1, longest_list + 1):
    ops_combos += list(itertools.product(ops, repeat=i))

# print(ops_combos)

true_test_values = []

for k in my_dict:
    this_answer = int(my_dict[k]["answer"])
    operands = my_dict[k]["operands"]
    num_operators = my_dict[k]["num_operators"]

    operators = [list(x) for x in ops_combos if len(x) == num_operators]

    # print(operators)
    # print(operands)

    found_a_match = False

    for o in operators:

        test_str = [operands[0]] + [
            o[i - 1] + operands[i] for i in range(1, num_operators + 1)
        ]

        # print(test_str)
        # continue

        running_calc = int(test_str[0])

        for x in test_str[1:]:
            if x[0] == "+":
                running_calc += int(x[1:])
            elif x[0] == "*":
                running_calc = running_calc * int(x[1:])
            elif x[0] == "|":
                running_calc = int(str(running_calc) + str(x[1:]))

        # print(test_str, running_calc, this_answer)

        if running_calc == this_answer:
            found_a_match = True
            break

    if found_a_match:
        true_test_values += [this_answer]

# print(true_test_values)
print(sum(true_test_values))
