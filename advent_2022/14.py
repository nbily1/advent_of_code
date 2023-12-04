# %% 1

raw = []

with open("dev/advent_2022/14.txt", "r") as file:
    raw = [x.strip() for x in file]

# print(raw)

my_dict = {}

max_y = 0
floor_y = 0

for a in raw:
    insts = a.split(" -> ")
    for i in range(len(insts) - 1):
        coord = [int(x) for x in insts[i].split(",")]
        next_coord = [int(x) for x in insts[i + 1].split(",")]
        print(coord, "->", next_coord)

        if coord[0] != next_coord[0]:
            for x in range(
                min(coord[0], next_coord[0]), max(coord[0], next_coord[0]) + 1
            ):
                my_dict[f"{x},{coord[1]}"] = {"type": "R", "coord": [x, coord[1]]}
                if coord[1] > max_y:
                    max_y = coord[1]
        else:
            for y in range(
                min(coord[1], next_coord[1]), max(coord[1], next_coord[1]) + 1
            ):
                my_dict[f"{coord[0]},{y}"] = {"type": "R", "coord": [coord[0], y]}
                if y > max_y:
                    max_y = y

floor_y = max_y + 2

# print(my_dict.keys())
print(max_y)
print(floor_y)

# is_done = False
# starting_spot = [500, 0]
# grains = 0

# while is_done == False:
#     current_spot = [500, 0]
#     stopped = False
#     grains += 1
#     print(f"Sand Grain: {grains}")
#     while stopped == False:
#         print(current_spot)
#         if current_spot[1] == max_y:
#             is_done = True
#             break
#         elif f"{current_spot[0]},{current_spot[1]+1}" not in my_dict:
#             current_spot[1] = current_spot[1] + 1
#             continue
#         elif f"{current_spot[0]-1},{current_spot[1]+1}" not in my_dict:
#             current_spot[1] = current_spot[1] + 1
#             current_spot[0] = current_spot[0] - 1
#             continue
#         elif f"{current_spot[0]+1},{current_spot[1]+1}" not in my_dict:
#             current_spot[1] = current_spot[1] + 1
#             current_spot[0] = current_spot[0] + 1
#             continue
#         else:
#             stopped = True
#             print(f"{current_spot[0]},{current_spot[1]}")
#             my_dict[f"{current_spot[0]},{current_spot[1]}"] = {
#                 "type": "S",
#                 "coord": [current_spot[0], current_spot[1]],
#             }
#             print(my_dict[f"{current_spot[0]},{current_spot[1]}"])
#             break

# print(grains)

# %% 2

is_done = False
starting_spot = [500, 0]
grains = 0

while is_done == False:
    current_spot = [500, 0]
    stopped = False
    grains += 1
    print(f"Sand Grain: {grains}")
    while stopped == False:
        # print(current_spot)
        # if current_spot[1] == max_y:
        #     is_done = True
        #     break
        if (
            f"{current_spot[0]},{current_spot[1]+1}" not in my_dict
            and current_spot[1] + 1 < floor_y
        ):
            current_spot[1] = current_spot[1] + 1
            continue
        elif (
            f"{current_spot[0]-1},{current_spot[1]+1}" not in my_dict
            and current_spot[1] + 1 < floor_y
        ):
            current_spot[1] = current_spot[1] + 1
            current_spot[0] = current_spot[0] - 1
            continue
        elif (
            f"{current_spot[0]+1},{current_spot[1]+1}" not in my_dict
            and current_spot[1] + 1 < floor_y
        ):
            current_spot[1] = current_spot[1] + 1
            current_spot[0] = current_spot[0] + 1
            continue
        else:
            stopped = True
            # print(f"{current_spot[0]},{current_spot[1]}")
            my_dict[f"{current_spot[0]},{current_spot[1]}"] = {
                "type": "S",
                "coord": [current_spot[0], current_spot[1]],
            }
            print(my_dict[f"{current_spot[0]},{current_spot[1]}"])
            break
    if f"500,0" in my_dict:
        is_done = True
        break

print(grains)
