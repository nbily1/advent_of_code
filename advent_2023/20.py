raise Exception("part 2 not solved")

# %% 1

from copy import deepcopy
import re

raw = []

with open("advent_2023/20.txt", "r") as file:
    raw = [x.strip() for x in file if x.strip() != ""]

print(raw)

config = {}

regex_patt = re.compile(r"^(%|&)?([a-z]+) -> (.+)$")

for x in raw:
    k = re.sub(regex_patt, r"\2", x)
    config[k] = {
        "module": k,
        "type": re.sub(regex_patt, r"\1", x),
        "dests": re.sub(regex_patt, r"\3", x).split(", "),
    }
    if config[k]["type"] == "%":
        config[k]["status"] = False
    if config[k]["type"] == "&":
        config[k]["memory"] = {}
        for y in config:
            if k in config[y]["dests"]:
                config[k]["memory"][y] = "low"

config["button"] = {"module": "button", "type": "", "dests": ["broadcaster"]}
for mod in list(config.keys()):
    if config[mod]["type"] == "&":
        for dest in config[mod]["dests"]:
            if dest not in config:
                config[dest] = {"module": dest, "type": "", "dests": []}

print(config)


def flip_flop(module, pulse) -> str:
    global config
    if pulse == "high":
        return None
    else:
        if config[module]["status"] == False:
            config[module]["status"] = True
            return "high"
        else:
            config[module]["status"] = False
            return "low"


def conjunction(module, pulse, source) -> str:
    global config
    config[module]["memory"][source] = pulse
    if "low" not in [v for v in list(config[module]["memory"].values())]:
        return "low"
    else:
        return "high"


low_pulses = 0
high_pulses = 0

for i in range(1000):
    curr_mods = [["button", "low", "button"]]

    while len(curr_mods) > 0:
        new_mods = []
        for m in curr_mods:
            this_mod = m[0]
            in_pulse = m[1]

            if config[this_mod]["type"] == "":
                this_pulse = "low"
                for d in config[this_mod]["dests"]:
                    low_pulses += 1
                    # print(f"{this_mod} -{this_pulse}-> {d}")
                    new_mods += [[d, this_pulse, this_mod]]
            elif config[this_mod]["type"] == "%":
                this_pulse = flip_flop(this_mod, in_pulse)
                for d in config[this_mod]["dests"]:
                    if this_pulse == "low":
                        low_pulses += 1
                    elif this_pulse == "high":
                        high_pulses += 1

                    if this_pulse != None:
                        # print(f"{this_mod} -{this_pulse}-> {d}")
                        new_mods += [[d, this_pulse, this_mod]]
            elif config[this_mod]["type"] == "&":
                this_pulse = conjunction(this_mod, in_pulse, m[2])
                for d in config[this_mod]["dests"]:
                    if this_pulse == "low":
                        low_pulses += 1
                    elif this_pulse == "high":
                        high_pulses += 1

                    if this_pulse != None:
                        # print(f"{this_mod} -{this_pulse}-> {d}")
                        new_mods += [[d, this_pulse, this_mod]]

        curr_mods = deepcopy(new_mods)
        # print(config)

print(low_pulses)
print(high_pulses)
print(low_pulses * high_pulses)
