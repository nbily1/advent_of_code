import heapq

# %% Part 1

# with open("advent_2024/18.txt", "r") as file:
#     my_list = [[int(y) for y in x.split(",")] for x in file]

# # print(my_list)

# max_y = 70
# max_x = 70
# S = [0, 0]
# E = [max_x, max_y]

# # print(S, E)

# dirs = {"w": [-1, 0], "s": [0, 1], "e": [1, 0], "n": [0, -1]}


# grid = [
#     ["." if [x, y] not in my_list[:1024] else "#" for x in range(max_x + 1)]
#     for y in range(max_y + 1)
# ]

# for y in grid:
#     print("".join(y))

# h = []

# heapq.heappush(h, (0, 0, {"pos": S, "path": [S], "indir": ""}))

# ticker = 0

# cheapest = [[S, 0, ""]]
# visited = [[S]]

# ticker = 0
# compl = []
# while len(h) > 0:
#     is_done = False
#     this_h = heapq.heappop(h)

#     score = this_h[0]
#     pos = this_h[2]["pos"]
#     path = this_h[2]["path"]
#     indir = this_h[2]["indir"]

#     for d in dirs:
#         if (
#             (indir == "n" and d == "s")
#             or (indir == "e" and d == "w")
#             or (indir == "s" and d == "n")
#             or (indir == "w" and d == "e")
#         ):
#             continue

#         this_dir = dirs[d]
#         ghost = [pos[0] + this_dir[0], pos[1] + this_dir[1]]

#         if ghost[0] < 0 or ghost[1] < 0:
#             continue

#         if ghost[0] > max_x or ghost[1] > max_y:
#             continue

#         if grid[ghost[0]][ghost[1]] in path:
#             continue

#         if grid[ghost[0]][ghost[1]] == "#":
#             continue

#         new_path = path + [ghost]
#         new_score = len(new_path)

#         if ghost in visited:
#             continue
#         else:
#             visited += [ghost]

#         # not_cheapest = False
#         # for c in range(len(cheapest)):
#         #     if ghost == cheapest[c][0] and d == cheapest[c][2]:
#         #         if new_score > cheapest[c][1]:
#         #             not_cheapest = True
#         #         else:
#         #             _ = cheapest.pop(c)
#         #         break

#         # if not_cheapest:
#         #     continue

#         cheapest += [[ghost, new_score, d]]

#         if ghost == E:
#             compl += [
#                 [
#                     score,
#                     ticker,
#                     {
#                         "pos": ghost,
#                         "path": new_path[:-1],
#                         "indir": d,
#                     },
#                 ]
#             ]
#             is_done = True
#             break
#         else:
#             heapq.heappush(
#                 h,
#                 (
#                     new_score,
#                     ticker,
#                     {"pos": ghost, "path": new_path, "indir": d},
#                 ),
#             )

#         ticker += 1

#     if is_done:
#         break

# # print([c[0] for c in compl])
# print(min([c[0] for c in compl]))


# %% Part 1

with open("advent_2024/18.txt", "r") as file:
    my_list = [[int(y) for y in x.split(",")] for x in file]

# print(my_list)

max_y = 70
max_x = 70
S = [0, 0]
E = [max_x, max_y]

# print(S, E)

dirs = {"w": [-1, 0], "s": [0, 1], "e": [1, 0], "n": [0, -1]}

prev_path = []

for m in range(1024, len(my_list)):

    if prev_path != [] and my_list[m] not in prev_path:
        continue

    grid = [
        ["." if [x, y] not in my_list[: m + 1] else "#" for x in range(max_x + 1)]
        for y in range(max_y + 1)
    ]

    # for y in grid:
    #     print("".join(y))

    h = []

    heapq.heappush(h, (0, 0, {"pos": S, "path": [S], "indir": ""}))

    ticker = 0

    visited = [[S]]

    ticker = 0
    compl = []
    while len(h) > 0:
        is_done = False
        this_h = heapq.heappop(h)

        score = this_h[0]
        pos = this_h[2]["pos"]
        path = this_h[2]["path"]
        indir = this_h[2]["indir"]

        for d in dirs:
            if (
                (indir == "n" and d == "s")
                or (indir == "e" and d == "w")
                or (indir == "s" and d == "n")
                or (indir == "w" and d == "e")
            ):
                continue

            this_dir = dirs[d]
            ghost = [pos[0] + this_dir[0], pos[1] + this_dir[1]]

            if ghost[0] < 0 or ghost[1] < 0:
                continue

            if ghost[0] > max_x or ghost[1] > max_y:
                continue

            if grid[ghost[1]][ghost[0]] in path:
                continue

            if grid[ghost[1]][ghost[0]] == "#":
                continue

            new_path = path + [ghost]
            new_score = len(new_path)

            if ghost in visited:
                continue
            else:
                visited += [ghost]

            if ghost == E:
                compl = [
                    [
                        score,
                        ticker,
                        {
                            "pos": ghost,
                            "path": new_path[:-1],
                            "indir": d,
                        },
                    ]
                ]
                is_done = True
                prev_path = new_path.copy()
                break
            else:
                heapq.heappush(
                    h,
                    (
                        new_score,
                        ticker,
                        {"pos": ghost, "path": new_path, "indir": d},
                    ),
                )

            ticker += 1

        if is_done:
            break

    # print([c[0] for c in compl])
    try:
        print(m, min([c[0] for c in compl]))
        # print(prev_path)
    except ValueError:
        print("Broken!", my_list[m])
        break
