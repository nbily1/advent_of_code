# %% 1

from copy import deepcopy

raw = []

with open("advent_2023/23.txt", "r") as file:
    raw = [[y for y in x.strip()] for x in file if x.strip() != ""]

print(raw)

starter = [0, raw[0].index(".")]
target = [len(raw) - 1, raw[len(raw) - 1].index(".")]

y_range = range(0, len(raw))
x_range = range(0, len(raw[0]))

legal_moves = {"v": [1, 0], "^": [-1, 0], ">": [0, 1], "<": [0, -1]}
all_moves = list(legal_moves.values())

print(starter, target)

paths = [[starter]]
finished_paths = []

print(paths)


active_paths = True

while active_paths == True:
    new_paths = []
    active_paths = False
    for path in paths:
        curr_coord = path[-1]
        curr_y = curr_coord[0]
        curr_x = curr_coord[1]
        for m in all_moves:
            new_y = curr_y + m[0]
            new_x = curr_x + m[1]

            if (
                new_y not in y_range
                or new_x not in x_range
                or raw[new_y][new_x] == "#"
                or [new_y, new_x] in path
                or (raw[new_y][new_x] in "v^><" and m != legal_moves[raw[new_y][new_x]])
            ):
                continue
            else:
                if [new_y, new_x] != target:
                    new_paths += [deepcopy(path) + [[new_y, new_x]]]
                else:
                    finished_paths += [deepcopy(path) + [[new_y, new_x]]]
                # print("new paths", new_paths, path)
    if len(new_paths) > 0:
        active_paths = True
        paths = deepcopy(new_paths)
        print(len(paths))
        # quit()

# print(finished_paths)
print([len(x) - 1 for x in finished_paths])
print(max([len(x) - 1 for x in finished_paths]))
