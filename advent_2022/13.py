# %% 1

raw = []

with open("dev/advent_2022/13.txt", "r") as file:
    raw = [x.strip() for x in file]

# print(raw)

raw_lists = []

for i in range(0, len(raw), 3):
    raw_lists += [[eval(raw[i]), eval(raw[i + 1])]]

print("\n", raw_lists[:2])
print("")

results = []

is_true = False
is_false = False


def compare(l: int | list, r: int | list) -> bool:
    global is_true
    global is_false

    if is_true:
        return True
    if is_false:
        return False

    l_type = type(l).__name__
    r_type = type(r).__name__

    if l_type != r_type:
        if l_type == "int":
            l = [l]
            l_type = "list"
        if r_type == "int":
            r = [r]
            r_type = "list"

    if l_type == "int" and r_type == "int":
        print(f"\t- Compare {l} vs {r}")
        if l > r:
            is_false = True
            return False
        if l < r:
            is_true = True
            return True
    else:
        try:
            for i in range(len(l)):
                if is_true == True:
                    return True
                if is_false == True:
                    return False
                if compare(l[i], r[i]) == False:
                    is_false = True
                    return False
        except IndexError:
            print("\t- Right side out of values")
            is_false = True
            return False

        if is_true:
            return True
        if is_false:
            return False

        if len(r) > len(l):
            print("\t- Left side out of values")
            is_true = True
            return True

    if is_true:
        return True
    if is_false:
        return False

    return True


runs = 0
passes = 0
passed = []

for i in range(len(raw_lists)):
    is_true = False
    is_false = False
    print(raw_lists[i][0])
    print(raw_lists[i][1])
    runs += 1
    result = compare(raw_lists[i][0], raw_lists[i][1])
    if result == True:
        passes += 1
        passed += [i + 1]

    print(result)
    print("")

print(f"Total Runs: {runs}")
print(f"Total Passes: {passes}")
print(f"Passed: {passed}")
print(sum(passed))

# %% 2

divider_1 = [[2]]
divider_2 = [[6]]

out_lists = [divider_1] + [divider_2]

raw_lists = []

for x in raw:
    if x != "":
        raw_lists += [eval(x)]

print("\n", raw_lists[:5])
print("")

for x in raw_lists:
    inserted = False
    for i in range(len(out_lists)):
        is_true = False
        is_false = False
        if compare(x, out_lists[i]) == True:
            out_lists.insert(i, [x])
            inserted = True
            break
        else:
            continue
    if inserted == False:
        out_lists += [x]

divider_locs = [0, 0]

for i in range(len(out_lists)):
    if out_lists[i] == divider_1:
        divider_locs[0] = i + 1
    elif out_lists[i] == divider_2:
        divider_locs[1] = i + 1

print(divider_locs, divider_locs[0] * divider_locs[1])
