# %% 1

# raw = []

# with open("advent_2023/13.txt", "r") as file:
#     raw = [[y for y in x.strip()] for x in file]

# print(raw)

# patterns = []
# holder = []
# for x in raw:
#     if x != []:
#         holder += [x]
#     else:
#         patterns += [holder]
#         holder = []
# else:
#     patterns += [holder]


# print(patterns)

# found_ys = []
# found_xs = []

# for p in patterns:
#     is_found = False

#     xs = []
#     # print(p, "\n")
#     # for y in range(len(p)):
#     for x in range(len(p[0])):
#         xs += [[y[x] for y in p]]
#     # print(xs)

#     if is_found == False:
#         this_min = 0
#         this_max = len(xs) - 1
#         for i in range(len(xs) - 1):
#             go_left = i
#             go_right = i + 1
#             not_broken = True
#             while go_left >= this_min and go_right <= this_max and not_broken:
#                 check_l = [x for x in xs[go_left]]
#                 check_r = [x for x in xs[go_right]]
#                 if check_l == check_r:
#                     go_left -= 1
#                     go_right += 1
#                 else:
#                     not_broken = False

#             if not_broken:
#                 is_found = True
#                 found_xs += [i + 1]
#                 break

#     if is_found == False:
#         this_min = 0
#         this_max = len(p) - 1
#         for i in range(len(p) - 1):
#             go_up = i
#             go_down = i + 1
#             not_broken = True
#             while go_up >= this_min and go_down <= this_max and not_broken:
#                 check_u = [x for x in p[go_up]]
#                 check_d = [x for x in p[go_down]]
#                 if check_u == check_d:
#                     go_up -= 1
#                     go_down += 1
#                 else:
#                     not_broken = False

#             if not_broken:
#                 is_found = True
#                 found_ys += [i + 1]
#                 break

# print(found_xs)
# print(found_ys)
# print(sum(found_xs) + sum(found_ys) * 100)

# quit()

# %% 2
from copy import deepcopy


raw = []

with open("advent_2023/13.txt", "r") as file:
    raw = [[y for y in x.strip()] for x in file]

# print(raw)

patterns = []
holder = []
for x in raw:
    if x != []:
        holder += [x]
    else:
        patterns += [holder]
        holder = []
else:
    patterns += [holder]


# print(patterns)

init_ys = []
init_xs = []
found_ys = []
found_xs = []

for p in patterns:  # [1:2]:
    is_found = False
    found_init = False

    ghosts = [deepcopy(p)]
    # print(ghosts[0][0])

    for x in range(len(p[0])):
        for y in range(len(p)):
            this_ghost = deepcopy(p)
            this_ghost[y][x] = "." if this_ghost[y][x] == "#" else "#"
            ghosts += [deepcopy(this_ghost)]
    # print(ghosts)
    # quit()

    found_x = None
    found_y = None
    init_x = None
    init_y = None
    is_found = False

    for g in ghosts:
        # if is_found != False:
        #     break
        xs = []
        for x in range(len(g[0])):
            xs += [[y[x] for y in g]]
        # print(xs)

        if is_found == False:
            this_min = 0
            this_max = len(xs) - 1
            for i in range(len(xs) - 1):
                go_left = i
                go_right = i + 1
                not_broken = True
                while go_left >= this_min and go_right <= this_max and not_broken:
                    check_l = [x for x in xs[go_left]]
                    check_r = [x for x in xs[go_right]]
                    if check_l == check_r:
                        go_left -= 1
                        go_right += 1
                    else:
                        not_broken = False

                if not_broken:
                    if init_x == None and init_y == None:
                        # is_found = True
                        init_x = i
                        init_xs += [i + 1]
                        # print(i)
                        break
                    elif (found_x == None or i < found_x) and i != init_x:
                        is_found = True
                        # found_x = i
                        found_x = i
                        break

        if is_found == False:
            this_min = 0
            this_max = len(g) - 1
            for i in range(len(g) - 1):
                go_up = i
                go_down = i + 1
                not_broken = True
                while go_up >= this_min and go_down <= this_max and not_broken:
                    check_u = [x for x in g[go_up]]
                    check_d = [x for x in g[go_down]]
                    if check_u == check_d:
                        go_up -= 1
                        go_down += 1
                    else:
                        not_broken = False

                if not_broken:
                    if init_x == None and init_y == None:
                        # is_found = True
                        init_y = i
                        init_ys += [i + 1]
                        # print(i)
                        break
                    elif (found_y == None or i < found_y) and i != init_y:
                        is_found = True
                        # found_x = i
                        found_y = i
                        break

    if found_x != None:
        found_xs += [found_x + 1]
    else:
        found_ys += [found_y + 1]

print(found_xs, init_xs)
print(found_ys, init_ys)
print(sum(found_xs) + sum(found_ys) * 100)
