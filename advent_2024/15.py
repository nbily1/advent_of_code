# %% Part 1

with open("advent_2024/15.txt", "r") as file:
    grid = [[y for y in x.strip()] for x in file if x[0] == "#"]

with open("advent_2024/15.txt", "r") as file:
    instructions = "".join([x.strip() for x in file if x[0] != "#" and x[0] != "\n"])

robot_loc = []
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "@":
            robot_loc = [y, x]
            break


for y in grid:
    print("".join(y))
# print(instructions)
# print(robot_loc)

dirs = {"^": [-1, 0], ">": [0, 1], "v": [1, 0], "<": [0, -1]}

for i in instructions:
    this_dir = dirs[i]

    ghost = [robot_loc[0] + this_dir[0], robot_loc[1] + this_dir[1]]

    if grid[ghost[0]][ghost[1]] == "#":
        pass
    elif grid[ghost[0]][ghost[1]] == ".":
        grid[ghost[0]][ghost[1]] = "@"
        grid[robot_loc[0]][robot_loc[1]] = "."
        robot_loc = ghost.copy()
    elif grid[ghost[0]][ghost[1]] == "O":
        is_done = False
        can_move = False
        next_ghost = ghost.copy()
        while True:
            next_ghost = [next_ghost[0] + this_dir[0], next_ghost[1] + this_dir[1]]
            if grid[next_ghost[0]][next_ghost[1]] == "#":
                break
            elif grid[next_ghost[0]][next_ghost[1]] == ".":
                can_move = True
                break
            elif grid[next_ghost[0]][next_ghost[1]] == "O":
                continue
        if can_move:
            grid[ghost[0]][ghost[1]] = "@"
            grid[robot_loc[0]][robot_loc[1]] = "."
            grid[next_ghost[0]][next_ghost[1]] = "O"
            robot_loc = ghost.copy()

print("")
for y in grid:
    print("".join(y))

boxes = []

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "O":
            boxes += [[y, x]]

gps_sum = sum([100 * b[0] + b[1] for b in boxes])
print(gps_sum)


# %% Part 2

# with open("advent_2024/15.txt", "r") as file:
#     grid = [
#         [
#             y
#             for y in x.strip()
#             .replace("#", "##")
#             .replace("O", "[]")
#             .replace(".", "..")
#             .replace("@", "@.")
#         ]
#         for x in file
#         if x[0] == "#"
#     ]

# with open("advent_2024/15.txt", "r") as file:
#     instructions = "".join([x.strip() for x in file if x[0] != "#" and x[0] != "\n"])

# robot_loc = []
# for y in range(len(grid)):
#     for x in range(len(grid[0])):
#         if grid[y][x] == "@":
#             robot_loc = [y, x]
#             break


# for y in grid:
#     print("".join(y))
# # print(instructions)
# # print(robot_loc)

# # quit()

# dirs = {"^": [-1, 0], ">": [0, 1], "v": [1, 0], "<": [0, -1]}
# counter = 1


# # def check_next(dir: list, to_move: list) -> list:
# #     building = []
# #     for tm in to_move[-1]:
# #         if grid[tm[0] + dir[0], tm[1] + dir[1]] == "[]":
# #         if grid[tm[0] + dir[0], tm[1] + dir[1]] == "#":
# #             return []


# for i in instructions:  # [:75]:
#     this_dir = dirs[i]

#     ghost = [robot_loc[0] + this_dir[0], robot_loc[1] + this_dir[1]]
#     # print(ghost)

#     if grid[ghost[0]][ghost[1]] == "#":
#         pass
#     elif grid[ghost[0]][ghost[1]] == ".":
#         grid[ghost[0]][ghost[1]] = "@"
#         grid[robot_loc[0]][robot_loc[1]] = "."
#         robot_loc = ghost.copy()
#     elif grid[ghost[0]][ghost[1]] in "[]":
#         is_done = False
#         can_move = False
#         next_ghost = ghost.copy()
#         while True:
#             to_continue = False
#             next_ghost = [next_ghost[0] + this_dir[0], next_ghost[1] + this_dir[1]]
#             if grid[next_ghost[0]][next_ghost[1]] == "#":
#                 break
#             elif grid[next_ghost[0]][next_ghost[1]] == ".":
#                 can_move = True
#                 break
#             elif grid[next_ghost[0]][next_ghost[1]] in "[]":
#                 continue
#         if can_move:
#             if i in "<>":
#                 for x in range(
#                     min([ghost[1] + 1, next_ghost[1]]),
#                     max([ghost[1] + 1, next_ghost[1]]),
#                     2,
#                 ):
#                     print(ghost, next_ghost)
#                     grid[next_ghost[0]][x] = "["
#                     grid[next_ghost[0]][x + 1] = "]"
#             elif i in "^v":
#                 to_move = [[tuple(ghost.copy())]]
#                 print(to_move)
#                 if grid[ghost[0]][ghost[1]] == "[":
#                     to_move[0] += [tuple([ghost[0], ghost[1] + 1])]
#                 elif grid[ghost[0]][ghost[1]] == "]":
#                     to_move[0] += [tuple([ghost[0], ghost[1] - 1])]

#                 next_to_move = [tuple([m[0] + this_dir[0], m[1]]) for m in to_move[-1]]
#                 next_syms = "".join([grid[m[0]][m[1]] for m in next_to_move])

#                 while "#" not in next_syms and ("[" in next_syms or "]" in next_syms):
#                     print("a", to_move)
#                     print("b", next_to_move)
#                     print("c", next_syms)
#                     for n in range(len(next_to_move)):
#                         if grid[next_to_move[n][0]][next_to_move[n][1]] == "[":
#                             if [
#                                 [next_to_move[n][0], next_to_move[n][1] + 1]
#                             ] not in next_to_move:
#                                 next_to_move += [
#                                     tuple([next_to_move[n][0], next_to_move[n][1] + 1])
#                                 ]
#                         elif grid[next_to_move[n][0]][next_to_move[n][1]] == "]":
#                             if [
#                                 [next_to_move[n][0], next_to_move[n][1] - 1]
#                             ] not in next_to_move:
#                                 next_to_move += [
#                                     tuple([next_to_move[n][0], next_to_move[n][1] - 1])
#                                 ]

#                     to_move = [list(set(m)) for m in to_move]  # this needs to be unique

#                     print("c", to_move)
#                     print("d", next_to_move)

#                     check_syms = "".join(
#                         [grid[m[0] + this_dir[0]][m[1]] for m in next_to_move]
#                     )
#                     if "#" in check_syms:
#                         to_move = []
#                         can_move = False
#                         to_continue = False
#                         break
#                     elif "[" in check_syms or "]" in check_syms:
#                         print(
#                             "e",
#                             "".join(
#                                 [grid[m[0] + this_dir[0]][m[1]] for m in next_to_move]
#                             ),
#                         )
#                         to_move += [
#                             [
#                                 m
#                                 for m in list(set(tuple(z) for z in next_to_move))
#                                 if grid[m[0]][m[1]] in "[]"
#                             ]
#                         ]
#                         to_continue = True
#                     else:
#                         to_move += [  # this needs to be unique
#                             [
#                                 m
#                                 for m in list(set(tuple(z) for z in next_to_move))
#                                 if grid[m[0]][m[1]] in "[]"
#                             ]
#                         ]
#                     print("f", to_move)
#                     print("g", next_to_move)

#                     next_to_move = [
#                         tuple([m[0] + this_dir[0], m[1]]) for m in to_move[-1]
#                     ]
#                     next_syms = "".join([grid[m[0]][m[1]] for m in next_to_move])
#                     # if to_continue is False:
#                     # break

#                 # print("a", to_move)
#                 # print("b", next_to_move)
#                 # print(to_move)
#                 to_move.reverse()
#                 print("h", to_move)

#                 if can_move and "#" not in next_syms:
#                     for t in to_move:
#                         # print(t)
#                         print("".join([grid[m[0] + this_dir[0]][m[1]] for m in t]))
#                         for m in t:
#                             # print(m)
#                             this_symbol = grid[m[0]][m[1]]
#                             grid[m[0] + this_dir[0]][m[1]] = this_symbol
#                             grid[m[0]][m[1]] = "."
#                 else:
#                     can_move = False
#                     counter += 1
#                     continue
#             if can_move:
#                 grid[ghost[0]][ghost[1]] = "@"
#                 grid[robot_loc[0]][robot_loc[1]] = "."
#                 robot_loc = ghost.copy()

#     # if counter >= 300:
#     #     print("\n", counter, i)
#     #     for y in grid:
#     #         print("".join(y))

#     breaked = False
#     for y in grid:
#         for x in range(1, len(y) - 1):
#             if y[x] == "[" and y[x + 1] != "]":
#                 breaked = True
#             if y[x + 1] == "]" and y[x] != "[":
#                 breaked = True
#     if breaked:
#         print("\n", counter, i)
#         for y in grid:
#             print("".join(y))
#         quit()

#     counter += 1

# boxes = []

# print("\n", counter, i)
# for y in grid:
#     print("".join(y))

# for y in range(len(grid)):
#     for x in range(len(grid[0])):
#         if grid[y][x] == "[":
#             boxes += [[y, x]]

# gps_sum = sum([100 * b[0] + b[1] for b in boxes])
# print(gps_sum)
# print(len(instructions))

# # 1442758 is too high
