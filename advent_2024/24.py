# %% Part 1

with open("advent_2024/24.txt", "r") as file:
    wires_raw = [x.strip().split(": ") for x in file if ":" in x]

with open("advent_2024/24.txt", "r") as file:
    gates_raw = [x.strip().split() for x in file if "->" in x]

# print(wires_raw)
# print(gates_raw)

wires = {w[0]: int(w[1]) for w in wires_raw}
gates = {x[4]: {"gate": x[1], "wires": [x[0], x[2]]} for x in gates_raw}

print(wires)
print(gates)

gates_list = [k for k in gates]

while len(gates_list) > 0:
    this_gate = gates_list.pop(0)
    this_test = gates[this_gate]

    if this_test["wires"][0] in wires and this_test["wires"][1] in wires:
        rslt = 0
        if this_test["gate"] == "AND":
            rslt = int(wires[this_test["wires"][0]] and wires[this_test["wires"][1]])
        if this_test["gate"] == "OR":
            rslt = int(wires[this_test["wires"][0]] or wires[this_test["wires"][1]])
        if this_test["gate"] == "XOR":
            rslt = int(wires[this_test["wires"][0]] != wires[this_test["wires"][1]])
        wires[this_gate] = rslt
    else:
        gates_list += [this_gate]

wires_rslt = [k for k in wires if k.startswith("z")]
wires_rslt.sort(reverse=True)

rslt_list = "".join([str(wires[w]) for w in wires_rslt])
print(rslt_list)
print(int(rslt_list, 2))


# %% Part 1

# with open("advent_2024/24.txt", "r") as file:
#     wires_raw = [x.strip().split(": ") for x in file if ":" in x]

# with open("advent_2024/24.txt", "r") as file:
#     gates_raw = [x.strip().split() for x in file if "->" in x]

# # print(wires_raw)
# # print(gates_raw)

# wires = {w[0]: int(w[1]) for w in wires_raw}
# gates = {x[4]: {"gate": x[1], "wires": [x[0], x[2]]} for x in gates_raw}

# print(wires)
# print(gates)

# gates_list = [k for k in gates]

# while len(gates_list) > 0:
#     this_gate = gates_list.pop(0)
#     this_test = gates[this_gate]

#     if this_test["wires"][0] in wires and this_test["wires"][1] in wires:
#         rslt = 0
#         if this_test["gate"] == "AND":
#             rslt = int(wires[this_test["wires"][0]] and wires[this_test["wires"][1]])
#         if this_test["gate"] == "OR":
#             rslt = int(wires[this_test["wires"][0]] or wires[this_test["wires"][1]])
#         if this_test["gate"] == "XOR":
#             rslt = int(wires[this_test["wires"][0]] != wires[this_test["wires"][1]])
#         wires[this_gate] = rslt
#     else:
#         gates_list += [this_gate]

# wires_rslt = [k for k in wires if k.startswith("z")]
# wires_rslt.sort(reverse=True)

# x_rslt = [k for k in wires if k.startswith("x")]
# x_rslt.sort(reverse=True)
# y_rslt = [k for k in wires if k.startswith("y")]
# y_rslt.sort(reverse=True)

# rslt_list = "".join([str(wires[w]) for w in wires_rslt])
# x_list = "".join([str(wires[w]) for w in x_rslt])
# y_list = "".join([str(wires[w]) for w in y_rslt])
# print(x_list)
# print(y_list)
# print(bin(int(x_list, 2) & int(y_list, 2))[2:])
# print(int(x_list, 2) & int(y_list, 2))
# print(rslt_list)
# print(int(rslt_list, 2))
