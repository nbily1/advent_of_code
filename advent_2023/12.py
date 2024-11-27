raise Exception("part 2 not solved")

# %% 1
# import re
# import itertools

# raw = []

# with open("advent_2023/12.txt", "r") as file:
#     raw = [[y for y in x.strip().split()] for x in file if x.strip() != ""]

# for i in range(len(raw)):
#     raw[i][1] = [int(x) for x in raw[i][1].split(",")]

# # print(raw)

# arrangs = []

# for x in raw:
#     springs = x[0]
#     patt = x[1]

#     poss = []
#     num_quests = len([q for q in springs if q == "?"])

#     opts = list(itertools.product(".#", repeat=num_quests))

#     this_match = r"^[^#]*"
#     for i in range(len(patt)):
#         this_match += (
#             r"#{" + f"{patt[i]}" + r"}" + (r"[^#]+" if i < len(patt) - 1 else r"[^#]*$")
#         )
#     # print(opts)
#     # print(this_match)

#     this_arrangs = 0
#     for opt in opts:
#         this_str = springs
#         for o in opt:
#             this_str = this_str.replace("?", o, 1)
#         if re.match(this_match, this_str):
#             this_arrangs += 1
#             # print(this_str)

#     arrangs += [this_arrangs]

# # print(arrangs)
# print(sum(arrangs))

# %% 2
import re
import itertools
from functools import lru_cache

import os, sys

from multiprocessing import Pool, get_context
import multiprocessing as mp

# print(raw)
# quit()

# reduce the number of question marks
#  from the ends
# count consecutive # - if only 1 occurrence in patt, go ahead and fill
# if longest pattern present, change adjacent ? to .

# arrangs = []
# all_opts = 0


# for x in raw:  # [2:3]:
def doacalc(x):
    springs = x[0]
    patt = x[1]

    print(springs, patt, len([q for q in springs if q == "?"]))

    if x[2] == x[3]:  # pattern and string are same length, so there is only one option
        return 1

    longest = "#" * max(patt)
    if (
        longest in springs
    ):  # if "longest" is already present, ensure it's surrounded by .s
        springs = springs.replace(
            "?" + longest,
            "." + longest,
        )
        springs = springs.replace(
            longest + "?",
            longest + ".",
        )

    this_match = r"^[^#]*"
    for i in range(len(patt)):
        this_match += (
            r"[#?]{"
            + f"{patt[i]}"
            + r"}"
            + (r"[^#]+" if i < len(patt) - 1 else r"[^#]*$")
        )
    # print(this_match)
    this_match = re.compile(this_match)

    for i in range(len(springs)):
        if springs[i] == "?":
            if re.match(this_match, springs[:i] + "#" + springs[i + 1 :]) and re.match(
                this_match, springs[:i] + "." + springs[i + 1 :]
            ):
                pass
            elif re.match(this_match, springs[:i] + "#" + springs[i + 1 :]):
                springs = springs[:i] + "#" + springs[i + 1 :]
            else:
                springs = springs[:i] + "." + springs[i + 1 :]

    if len([q for q in springs if q == "?"]) == 0:
        return 1

    print(springs, patt, len([q for q in springs if q == "?"]))

    # @lru_cache()
    def checker(instr, inpatt, c, leninpatt, final_match) -> int:
        ismatch = re.match(final_match, instr.replace("?", "."))
        if c >= len(instr) - 1 or ismatch:
            if ismatch:
                # print(instr)
                return 1
            else:
                return 0

        while c < len(instr) and instr[c] != "?":
            c += 1

        num_matches = 0

        hash = re.match(inpatt, instr[:c] + "#" + instr[c + 1 :])
        dot = re.match(inpatt, instr[:c] + "." + instr[c + 1 :])

        if hash:
            # print(instr[:c] + "#" + instr[c + 1 :])
            num_matches += checker(
                instr[:c] + "#" + instr[c + 1 :], inpatt, c, leninpatt, final_match
            )
        if dot:
            # print(instr[:c] + "." + instr[c + 1 :])
            num_matches += checker(
                instr[:c] + "." + instr[c + 1 :], inpatt, c, leninpatt, final_match
            )

        return num_matches

    this_match = r"^[^#]*"
    for i in range(len(patt)):
        this_match += (
            r"[#?]{"
            + f"{patt[i]}"
            + r"}"
            + (r"[^#]+" if i < len(patt) - 1 else r"[^#]*$")
        )
    # print(this_match)
    this_match = re.compile(this_match)

    final_match = r"^[^#]*"
    for i in range(len(patt)):
        final_match += (
            r"#{" + f"{patt[i]}" + r"}" + (r"[^#]+" if i < len(patt) - 1 else r"[^#]*$")
        )
    final_match = re.compile(final_match)

    return checker(springs, this_match, 0, len(patt), final_match)

    # print(checker.cache_info())

    # continue


if __name__ == "__main__":
    raw = []

    with open("advent_2023/12.txt", "r") as file:
        raw = [[y for y in x.strip().split()] for x in file if x.strip() != ""]

    for i in range(len(raw)):
        raw[i][0] = ((raw[i][0] + "?") * 5)[:-1]
        raw[i][1] = (
            [int(x) for x in raw[i][1].split(",")]
            + [int(x) for x in raw[i][1].split(",")]
            + [int(x) for x in raw[i][1].split(",")]
            + [int(x) for x in raw[i][1].split(",")]
            + [int(x) for x in raw[i][1].split(",")]
        )
        raw[i] += [len(raw[i][0])]
        raw[i] += [sum([x + 1 for x in raw[i][1]]) - 1]

    pool = get_context("spawn").Pool(processes=1)
    results = [pool.apply_async(doacalc, args=(x,)) for x in raw]
    arrangs = [p.get() for p in results]
    pool.close()

    # print(arrangs)
    # print(all_opts)
    print(sum(arrangs))
