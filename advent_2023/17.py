raise Exception("not solved")

# %% 1

from copy import deepcopy

raw = []

with open("advent_2023/17.txt", "r") as file:
    raw = [[int(y) for y in x.strip()] for x in file if x.strip() != ""]

print(raw)

paths = []

active_blocks = [[0, 0]]

moves_to_try = [[1, 0], [-1, 0], [0, 1], [0, -1]]

y_range = range(0, len(raw))
x_range = range(0, len(raw[0]))

target_y = len(raw) - 1
target_x = len(raw[0]) - 1

blocks = {}

for y in y_range:
    for x in x_range:
        blocks[f"{y},{x}"] = {
            "coord": [y, x],
            "loss": raw[y][x],
            "path": [[]],
            "path_loss": [],
        }


print(blocks)

quit()

blocks["0,0"]["path_loss"] = [0]
blocks["0,0"]["path"] = [[[0, 0]]]

direct_loss = 0
direct_path = []

for y in range(1, len(raw)):
    direct_loss += raw[y][y - 1] + raw[y][y]
    direct_path += [[y, y - 1], [y, y]]
    # print([y, y], [y, y - 1])

# print(direct_loss)
# print(direct_path)

blocks[f"{len(raw)-1},{len(raw[0])-1}"]["path_loss"] = [direct_loss]
blocks[f"{len(raw)-1},{len(raw[0])-1}"]["path"] = [direct_path]

# print(blocks)
# quit()

while len(active_blocks) > 0:
    new_active_blocks = []
    for b in active_blocks:
        this_block_key = f"{b[0]},{b[1]}"
        curr_y = b[0]
        curr_x = b[1]

        paths = deepcopy(blocks[this_block_key]["path"])
        curr_losses = deepcopy(blocks[this_block_key]["path_loss"])

        # print(curr_losses)

        for m in moves_to_try:
            for i in range(len(paths)):
                path = deepcopy(paths[i])
                curr_loss = curr_losses[i]
                if len(path) >= 4:
                    prev_y = path[-4][0]
                    prev_x = path[-4][1]
                else:
                    prev_y = None
                    prev_x = None

                new_y = curr_y + m[0]
                new_x = curr_x + m[1]
                new_block_key = f"{new_y},{new_x}"

                # print("new", [new_y, new_x])
                if (
                    new_y not in y_range
                    or new_x not in x_range
                    or (new_y == curr_y and new_x == curr_x)
                    or (prev_y != None and abs(new_y - prev_y) > 3)
                    or (prev_x != None and abs(new_x - prev_x) > 3)
                    or [new_y, new_x] in path
                ):
                    continue

                for j in range(len(blocks[new_block_key]["path_loss"])):
                    exist_loss = blocks[new_block_key]["path_loss"][j]
                    exist_path = deepcopy(blocks[new_block_key]["path"][j])

                    new_path = deepcopy(path) + [[new_y, new_x]]
                    new_loss = curr_loss + raw[new_y][new_x]

                    if (
                        (exist_loss != None and new_loss > exist_loss)
                        or new_path in blocks[new_block_key]["path"]
                        or new_loss > direct_loss
                        or new_loss
                        > min(blocks[f"{len(raw)-1},{len(raw[0])-1}"]["path_loss"])
                    ):
                        continue

                    blocks[new_block_key]["path"].insert(j, new_path)
                    blocks[new_block_key]["path"] = blocks[new_block_key]["path"][:4]
                    blocks[new_block_key]["path_loss"].insert(j, new_loss)
                    blocks[new_block_key]["path_loss"] = blocks[new_block_key][
                        "path_loss"
                    ][:4]
                    if [new_y, new_x] not in new_active_blocks and [new_y, new_x] != [
                        len(raw) - 1,
                        len(raw[0]) - 1,
                    ]:
                        new_active_blocks += [[new_y, new_x]]
    active_blocks = deepcopy(new_active_blocks)
    print(len(active_blocks))
    if (
        len(blocks[f"{len(raw)-1},{len(raw[0])-1}"]["path_loss"]) == 4
        and len(active_blocks) < 5
    ):
        break

# for b in active_blocks:
#     print(blocks[f"{b[0]},{b[1]}"])
# print(active_blocks)

print(blocks[f"{len(raw)-1},{len(raw[0])-1}"])
print(min(blocks[f"{len(raw)-1},{len(raw[0])-1}"]["path_loss"]))
