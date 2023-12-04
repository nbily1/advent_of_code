# %% 1
import re, json  # , pandas as pd

raw = []

with open("dev/advent_2022/16.txt", "r") as file:
    raw = [x.strip() for x in file]

# print(raw)

valves = {}

patt = r"^Valve ([A-Z]{2}) has flow rate=([0-9]+); tunnels? leads? to valves? (.+)$"

current_valve = "AA"

for x in raw:
    this_valve = re.sub(pattern=patt, repl=r"\1", string=x)
    flow_rate = int(re.sub(pattern=patt, repl=r"\2", string=x))
    next_tunnels = [
        x.strip() for x in re.sub(pattern=patt, repl=r"\3", string=x).split(",")
    ]

    valves[this_valve] = {"flow_rate": flow_rate, "next": next_tunnels, "status": "C"}

    # if current_valve == "":
    #     current_valve = this_valve

# print(valves)

shortest_paths = {}
valve_count = len(valves)


def path_gen(par: str, this_list: list, moves: int = 1):
    global shortest_paths
    global valves
    for v in this_list:
        if v not in shortest_paths[par] or moves < shortest_paths[par][v]:
            shortest_paths[par][v] = moves
            # print(shortest_paths[par], moves)
            if len(shortest_paths[par]) >= valve_count:
                return
    for v in this_list:
        path_gen(
            par=par,
            this_list=[
                x
                for x in valves[v]["next"]
                if x not in shortest_paths[par] or moves + 1 < shortest_paths[par][x]
            ],
            moves=moves + 1,
        )


for v in valves:
    shortest_paths[v] = {v: 0}
    path_gen(par=v, this_list=valves[v]["next"])

# print("")
# print(shortest_paths)
# print("")
# m = 0
# max_moves = 30

# paths = {
#     current_valve: {
#         "path": [],
#         "current": current_valve,
#         "moves_left": max_moves - m,
#         "active": True,
#         "value": 0,
#     }
# }
# paths[current_valve]["next"] = [
#     x
#     for x in valves
#     if valves[x]["flow_rate"] > 0 and x not in paths[current_valve]["path"]
# ]

# active_paths = 1

# while active_paths <= 30:
#     new_paths = {}
#     for par in paths:
#         if paths[par]["active"] == True:
#             for n in paths[par]["next"]:
#                 if paths[par]["moves_left"] > shortest_paths[paths[par]["current"]][n]:
#                     new_paths[f"{par},{n}"] = {
#                         "path": paths[par]["path"] + [n],
#                         "current": n,
#                         "moves_left": paths[par]["moves_left"]
#                         - shortest_paths[paths[par]["current"]][n]
#                         - 1,
#                     }
#                     new_paths[f"{par},{n}"]["next"] = [
#                         x
#                         for x in valves
#                         if valves[x]["flow_rate"] > 0
#                         and x not in new_paths[f"{par},{n}"]["path"]
#                         and new_paths[f"{par},{n}"]["moves_left"]
#                         > shortest_paths[new_paths[f"{par},{n}"]["current"]][x]
#                     ]
#                     new_paths[f"{par},{n}"]["active"] = (
#                         True
#                         if new_paths[f"{par},{n}"]["moves_left"] > 0
#                         and new_paths[f"{par},{n}"]["next"] != []
#                         else False
#                     )
#                     new_paths[f"{par},{n}"]["value"] = paths[par]["value"] + (
#                         new_paths[f"{par},{n}"]["moves_left"] * valves[n]["flow_rate"]
#                     )
#     paths = {**paths, **new_paths}
#     active_paths += 1
#     if active_paths % 10 == 0:
#         print(f"Finished round {active_paths}")

# # print(json.dumps(paths, indent=2))
# # print(pd.DataFrame(paths))

# highest_val = 0
# highest_path = ""

# for x in paths:
#     if paths[x]["value"] > highest_val:
#         highest_path = x
#         highest_val = paths[x]["value"]

# for p in range(2, len(highest_path) + 1, 3):
#     print(paths[highest_path[:p]])

# print(highest_path, highest_val)
# quit()

# %% 2

m = 0
max_moves = 26

paths = {
    f"{current_valve}{current_valve}": [
        {
            "path": [],
            "current": current_valve,
            "moves_left": max_moves - m,
            "active": True,
            "value": 0,
        },
        {
            "path": [],
            "current": current_valve,
            "moves_left": max_moves - m,
            "active": True,
            "value": 0,
        },
    ]
}
paths[f"{current_valve}{current_valve}"][0]["next"] = [
    x
    for x in valves
    if valves[x]["flow_rate"] > 0
    and x not in paths[f"{current_valve}{current_valve}"][0]["path"]
]
paths[f"{current_valve}{current_valve}"][1]["next"] = [
    x
    for x in valves
    if valves[x]["flow_rate"] > 0
    and x not in paths[f"{current_valve}{current_valve}"][1]["path"]
]

print(paths)
# quit()

active_paths = 1

while active_paths <= 26:
    new_paths = {}
    for par in paths:
        if paths[par][0]["active"] == False and paths[par][1]["active"] == False:
            continue
        if len(par) < 4 + ((active_paths - 1) * 5):
            continue
        for x in paths[par][0]["next"] + [".."]:
            for y in paths[par][1]["next"] + [".."]:
                if x != y:
                    new_paths[f"{par},{x}{y}"] = [
                        {
                            "path": paths[par][0]["path"] + [x],
                            "current": x,
                            "moves_left": paths[par][0]["moves_left"]
                            - shortest_paths[paths[par][0]["current"]][x]
                            - 1,
                        }
                        if paths[par][0]["active"] == True and x != ".."
                        else {**paths[par][0]},
                        {
                            "path": paths[par][1]["path"] + [y],
                            "current": y,
                            "moves_left": paths[par][1]["moves_left"]
                            - shortest_paths[paths[par][1]["current"]][y]
                            - 1,
                        }
                        if paths[par][1]["active"] == True and y != ".."
                        else {**paths[par][1]},
                    ]

                    for i in [0, 1]:
                        if paths[par][i]["active"] == True and (
                            (i == 0 and x != "..") or (i == 1 and y != "..")
                        ):
                            # for n in paths[par][i]["next"]:
                            if (
                                paths[par][i]["moves_left"]
                                > shortest_paths[paths[par][i]["current"]][
                                    x if i == 0 else y
                                ]
                            ):
                                # new_paths[f"{par},{n}"][i] = {
                                #     "path": paths[par][i]["path"] + [n],
                                #     "current": n,
                                #     "moves_left": paths[par][i]["moves_left"]
                                #     - shortest_paths[paths[par][i]["current"]][n]
                                #     - 1,
                                # }
                                new_paths[f"{par},{x}{y}"][i]["next"] = [
                                    z
                                    for z in valves
                                    if valves[z]["flow_rate"] > 0
                                    and z not in new_paths[f"{par},{x}{y}"][i]["path"]
                                    and z
                                    not in new_paths[f"{par},{x}{y}"][1 - i]["path"]
                                    and new_paths[f"{par},{x}{y}"][i]["moves_left"]
                                    > shortest_paths[
                                        new_paths[f"{par},{x}{y}"][i]["current"]
                                    ][z]
                                ]
                                new_paths[f"{par},{x}{y}"][i]["active"] = (
                                    True
                                    if new_paths[f"{par},{x}{y}"][i]["moves_left"] > 0
                                    and new_paths[f"{par},{x}{y}"][i]["next"] != []
                                    else False
                                )
                                new_paths[f"{par},{x}{y}"][i]["value"] = paths[par][i][
                                    "value"
                                ] + (
                                    new_paths[f"{par},{x}{y}"][i]["moves_left"]
                                    * valves[x if i == 0 else y]["flow_rate"]
                                )
                        else:
                            new_paths[f"{par},{x}{y}"][i]["active"] = False
                            new_paths[f"{par},{x}{y}"][i]["next"] = []
    paths = {**paths, **new_paths}
    if active_paths % 1 == 0:
        print(f"Finished round {active_paths}")
    active_paths += 1

# print(json.dumps(paths, indent=2))
# print(pd.DataFrame(paths))

highest_val = 0
highest_path = ""

for x in paths:
    if paths[x][0]["value"] + paths[x][1]["value"] > highest_val:
        highest_path = x
        highest_val = paths[x][0]["value"] + paths[x][1]["value"]

for p in range(4, len(highest_path) + 1, 5):
    print(paths[highest_path[:p]])

print(highest_path, highest_val)
quit()
