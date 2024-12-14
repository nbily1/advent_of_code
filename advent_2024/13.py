# %% Part 1

with open("advent_2024/13.txt", "r") as file:
    my_list = [x.strip() for x in file]

broken = []

for i in range(0, len(my_list), 4):
    broken += [[my_list[i], my_list[i + 1], my_list[i + 2]]]

# print(broken)

my_dict = {}


for i in range(len(broken)):
    my_dict[i] = {
        "A": [
            int(x)
            for x in broken[i][0]
            .replace("Button A: ", "")
            .replace("X+", "")
            .replace("Y+", "")
            .split(", ")
        ],
        "B": [
            int(x)
            for x in broken[i][1]
            .replace("Button B: ", "")
            .replace("X+", "")
            .replace("Y+", "")
            .split(", ")
        ],
        "Prize": [
            int(x)
            for x in broken[i][2]
            .replace("Prize: ", "")
            .replace("X=", "")
            .replace("Y=", "")
            .split(", ")
        ],
    }

# print(my_dict)

for k in my_dict:
    x_a = my_dict[k]["A"][0]
    x_b = my_dict[k]["B"][0]
    y_a = my_dict[k]["A"][1]
    y_b = my_dict[k]["B"][1]
    x_prize = my_dict[k]["Prize"][0]
    y_prize = my_dict[k]["Prize"][1]

    curr_b = (y_prize * x_a - x_prize * y_a) / (-x_b * y_a + y_b * x_a)
    x_rem = x_prize - (curr_b * x_b)
    curr_a = x_rem / x_a

    if curr_b % 1 == 0:
        my_dict[k]["Solution"] = [curr_a, curr_b]
    else:
        my_dict[k]["Solution"] = None

# print(my_dict)

tokens = 0

for k in my_dict:
    if my_dict[k]["Solution"]:
        tokens += my_dict[k]["Solution"][0] * 3 + my_dict[k]["Solution"][1]

print(int(tokens))


# %% Part 2

with open("advent_2024/13.txt", "r") as file:
    my_list = [x.strip() for x in file]

broken = []

for i in range(0, len(my_list), 4):
    broken += [[my_list[i], my_list[i + 1], my_list[i + 2]]]

# print(broken)

my_dict = {}


for i in range(len(broken)):
    my_dict[i] = {
        "A": [
            int(x)
            for x in broken[i][0]
            .replace("Button A: ", "")
            .replace("X+", "")
            .replace("Y+", "")
            .split(", ")
        ],
        "B": [
            int(x)
            for x in broken[i][1]
            .replace("Button B: ", "")
            .replace("X+", "")
            .replace("Y+", "")
            .split(", ")
        ],
        "Prize": [
            int(x) + 10000000000000
            for x in broken[i][2]
            .replace("Prize: ", "")
            .replace("X=", "")
            .replace("Y=", "")
            .split(", ")
        ],
    }

# print(my_dict)

for k in my_dict:
    x_a = my_dict[k]["A"][0]
    x_b = my_dict[k]["B"][0]
    y_a = my_dict[k]["A"][1]
    y_b = my_dict[k]["B"][1]
    x_prize = my_dict[k]["Prize"][0]
    y_prize = my_dict[k]["Prize"][1]

    curr_b = (y_prize * x_a - x_prize * y_a) / (-x_b * y_a + y_b * x_a)
    my_dict[k][
        "Equation"
    ] = f"({y_prize} * {x_a} - {x_prize} * {y_a}) / (-{x_b} * {y_a} + {y_b} * {x_a})"
    x_rem = x_prize - (curr_b * x_b)
    curr_a = x_rem / x_a

    # curr_a = (y_prize * x_b - x_prize * y_b) / (-x_a * y_b + y_a * x_b)
    # my_dict[k][
    #     "Equation"
    # ] = f"({y_prize} * {x_b} - {x_prize} * {y_b}) / (-{x_a} * {y_b} + {y_a} * {x_b})"
    # x_rem = x_prize - (curr_a * x_a)
    # curr_b = x_rem / x_b

    if curr_b % 1 == 0 and curr_a % 1 == 0:
        my_dict[k]["Solution"] = [curr_a, curr_b]
    else:
        my_dict[k]["Solution"] = None

# print(my_dict)

tokens = 0

for k in my_dict:
    if my_dict[k]["Solution"]:
        tokens += my_dict[k]["Solution"][0] * 3 + my_dict[k]["Solution"][1]

print(int(tokens))
