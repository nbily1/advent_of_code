raise Exception("Not solved yet :-(")

# %% 1
import re, json  # , pandas as pd
from math import floor
from copy import deepcopy

raw = []

with open("advent_2022/19.txt", "r") as file:
    raw = [x.strip() for x in file]

# print(raw)

patt = r"^Blueprint ([0-9]+): Each ore robot costs ([0-9]+) ([a-z]+). Each clay robot costs ([0-9]+) ([a-z]+). Each obsidian robot costs ([0-9]+) ([a-z]+) and ([0-9]+) ([a-z]+). Each geode robot costs ([0-9]+) ([a-z]+) and ([0-9]+) ([a-z]+).$"

blueprints = {}

for x in raw:
    this_bp = re.sub(pattern=patt, repl=r"\1", string=x)
    orecost1 = int(re.sub(pattern=patt, repl=r"\2", string=x))
    oreresource1 = re.sub(pattern=patt, repl=r"\3", string=x)
    claycost1 = int(re.sub(pattern=patt, repl=r"\4", string=x))
    clayresource1 = re.sub(pattern=patt, repl=r"\5", string=x)
    obsidiancost1 = int(re.sub(pattern=patt, repl=r"\6", string=x))
    obsidianresource1 = re.sub(pattern=patt, repl=r"\7", string=x)
    obsidiancost2 = int(re.sub(pattern=patt, repl=r"\8", string=x))
    obsidianresource2 = re.sub(pattern=patt, repl=r"\9", string=x)
    geodecost1 = int(re.sub(pattern=patt, repl=r"\10", string=x))
    geoderesource1 = re.sub(pattern=patt, repl=r"\11", string=x)
    geodecost2 = int(re.sub(pattern=patt, repl=r"\12", string=x))
    geoderesource2 = re.sub(pattern=patt, repl=r"\13", string=x)
    blueprints[this_bp] = {
        "-": {"ore": 0},
        "ore": {oreresource1: orecost1},
        "clay": {clayresource1: claycost1},
        "obsidian": {
            obsidianresource1: obsidiancost1,
            obsidianresource2: obsidiancost2,
        },
        "geode": {
            geoderesource1: geodecost1,
            geoderesource2: geodecost2,
        },
    }

robots = {"ore": 1, "clay": 0, "obsidian": 0, "geode": 0}
resources = {"ore": 0, "clay": 0, "obsidian": 0, "geode": 0}

print(blueprints)

paths = [{"robots": robots, "resources": resources}]

print(paths)

blueprint = "2"

has_clay = False
has_obsidian = False
has_geode = False

for minute in range(1, 25):
    new_paths = []

    ore_clay_opt = (
        blueprints[blueprint]["obsidian"]["ore"]
        / blueprints[blueprint]["obsidian"]["clay"]
    )
    ore_obsidian_opt = (
        blueprints[blueprint]["geode"]["ore"]
        / blueprints[blueprint]["geode"]["obsidian"]
    )

    for x in paths:
        # check which robots we can build
        check_options = [rob for rob in blueprints[blueprint]]
        check_options.reverse()
        to_remove = []
        for rob in check_options:
            for res in blueprints[blueprint][rob]:
                if (
                    blueprints[blueprint][rob][res] > x["resources"][res]
                    and rob not in to_remove
                ):
                    to_remove += [rob]
        # print(to_remove)
        for i in to_remove:
            check_options.remove(i)
        if "geode" in check_options:
            check_options = ["geode", "-"]
        elif "obsidian" in check_options and (
            x["resources"]["obsidian"] == 0
            or x["resources"]["ore"] / x["resources"]["obsidian"] < ore_obsidian_opt
        ):
            check_options = ["obsidian", "-"]
        elif "clay" in check_options and (
            x["resources"]["clay"] == 0
            or x["resources"]["ore"] / x["resources"]["clay"] < ore_clay_opt
        ):
            check_options = ["clay", "-"]
        # print(check_options)

        for o in check_options:
            this_option = deepcopy(x)
            if o != "-":
                this_option["robots"][o] += 1
                if o == "clay" and has_clay == False:
                    has_clay = True
                if o == "obsidian" and has_obsidian == False:
                    has_obsidian = True
                if o == "geode" and has_geode == False:
                    has_geode = True
            for res in blueprints[blueprint][o]:
                this_option["resources"][res] -= blueprints[blueprint][o][res]
            for rob in x["robots"]:
                this_option["resources"][rob] += x["robots"][rob]
            # print(this_option)
            if this_option not in new_paths:
                new_paths += [deepcopy(this_option)]

        for p in new_paths:
            # if has_clay == True:
            #     if p["robots"]["clay"] == 0:
            #         new_paths.remove(p)
            #         continue
            if has_obsidian == True:
                if p["robots"]["obsidian"] == 0:
                    new_paths.remove(p)
                    continue
            if has_geode == True:
                if p["robots"]["geode"] == 0:
                    new_paths.remove(p)

    # print("\nNew Paths: ", new_paths, "\n")
    paths = deepcopy(new_paths)
    print(f"Finished minute {minute}", len(paths))

# print(paths)

max_geodes = 0
best_path = {}
for p in paths:
    if p["resources"]["geode"] > max_geodes:
        max_geodes = p["resources"]["geode"]
        best_path = deepcopy(p)

print(max_geodes, "\n", best_path)
