# %% 1

from copy import deepcopy

raw = []

with open("advent_2023/19.txt", "r") as file:
    raw = [x.strip() for x in file]

is_parts = False

wfs = {}
parts = {}

for x in raw:
    if is_parts == False:
        if x == "":
            is_parts = True
            continue

        wf_name = x.split("{")[0]
        rules_txt = x.split("{")[1][:-1]
        rules_dict = {}
        for y in [x for x in rules_txt.split(",")]:
            if len(y.split(":")) == 2:
                rules_dict[y.split(":")[0]] = y.split(":")[1]
            else:
                rules_dict["1==1"] = y
        wfs[wf_name] = rules_dict
    else:
        parts_dict = {}
        for y in [x for x in x[1:-1].split(",")]:
            parts_dict[y.split("=")[0]] = y.split("=")[1]
        parts[x] = parts_dict

# print(wfs)
# print(parts)

accepted = []
accepted_sum = 0

for p in parts:
    curr_rule = "in"

    x = parts[p]["x"]
    m = parts[p]["m"]
    a = parts[p]["a"]
    s = parts[p]["s"]

    while curr_rule not in ["A", "R"]:
        for check in wfs[curr_rule]:
            curr_check = (
                check.replace("x", x).replace("m", m).replace("a", a).replace("s", s)
            )
            # print(curr_rule, check, curr_check)
            if eval(curr_check) == True:
                curr_rule = wfs[curr_rule][check]
                if curr_rule == "A":
                    accepted += [p]
                    accepted_sum += sum([int(x), int(m), int(a), int(s)])
                break
            else:
                continue
            break

print(accepted)
print(accepted_sum)

# %% 2

curr_wf = "in"

rules = []


def create_rules(incoming: list, target_key: str, target_index: int):
    global wfs
    global rules

    true_condition = incoming + [list(wfs[target_key].keys())[target_index]]
    true_target_key = wfs[target_key][list(wfs[target_key].keys())[target_index]]
    true_target_index = 0

    false_condition = incoming + [
        "not (" + list(wfs[target_key].keys())[target_index] + ")"
    ]
    if false_condition[-1] != "not (1==1)":
        false_target_key = target_key
        false_target_index = target_index + 1
    else:
        false_target_key = "R"
        false_target_index = 0

    # print(true_condition, true_target_key, true_target_index)
    # print(false_condition, false_target_key, false_target_index)

    if true_target_key not in ["A", "R"]:
        create_rules(true_condition, true_target_key, true_target_index)
    elif true_target_key == "A":
        rules += [true_condition]

    if false_condition[-1] != "not (1==1)" and false_target_key not in ["A", "R"]:
        create_rules(false_condition, false_target_key, false_target_index)
    elif false_target_key == "A":
        rules += [false_condition]


create_rules([], "in", 0)

print(len(rules))


def check_rules(in_rules, letter):
    if in_rules == []:
        return 4000
    passes = 0
    for v in range(1, 4001):
        passing = True
        for r in in_rules:
            if eval(r.replace(letter, str(v))) == False:
                passing = False
        if passing == True:
            passes += 1
    return passes


final_result = 0

for r in rules:
    x_rules = [x for x in r if "x" in x]
    m_rules = [x for x in r if "m" in x]
    a_rules = [x for x in r if "a" in x]
    s_rules = [x for x in r if "s" in x]

    this_result = (
        check_rules(x_rules, "x")
        * check_rules(m_rules, "m")
        * check_rules(a_rules, "a")
        * check_rules(s_rules, "s")
    )

    final_result += this_result

    print(x_rules, m_rules, a_rules, s_rules, this_result)

print(final_result)
