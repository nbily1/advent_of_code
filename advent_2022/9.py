# %% 1

moves_raw = []

with open("advent_2022/9.txt", "r") as file:
    moves_raw = [x.strip().split() for x in file]

moves = []

for x in moves_raw:
    moves += [[x[0], int(x[1])]]

print(moves)

h_pos = [0, 0]
t_pos = [0, 0]

tail_positions = ["0,0"]

for m in moves:
    for i in range(m[1]):
        this_move = -1 if m[0] in ["L", "U"] else 1

        if m[0] in ["R", "L"]:
            h_pos[1] += this_move
        elif m[0] in ["D", "U"]:
            h_pos[0] += this_move

        x_diff = h_pos[1] - t_pos[1]
        y_diff = h_pos[0] - t_pos[0]

        if abs(x_diff) + abs(y_diff) > 2:
            t_pos[0] += y_diff / abs(y_diff)
            t_pos[1] += x_diff / abs(x_diff)
        elif abs(x_diff) > 1:
            t_pos[1] += this_move
        elif abs(y_diff) > 1:
            t_pos[0] += this_move

        tail_positions += [f"{int(t_pos[0])},{int(t_pos[1])}"]

print(tail_positions)

tail_unique = ["0,0"]

for x in tail_positions:
    if x not in tail_unique:
        tail_unique += [x]

print(tail_unique[:10])

print(len(tail_positions))
print(len(tail_unique))

# %% 2

h_pos = [0, 0]
t_pos = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

tail_positions = ["0,0"]

for m in moves:
    for i in range(m[1]):
        this_move = -1 if m[0] in ["L", "U"] else 1

        if m[0] in ["R", "L"]:
            h_pos[1] += this_move
        elif m[0] in ["D", "U"]:
            h_pos[0] += this_move

        for t in range(len(t_pos)):
            if t == 0:
                this_h = h_pos
            else:
                this_h = t_pos[t - 1]

            x_diff = this_h[1] - t_pos[t][1]
            y_diff = this_h[0] - t_pos[t][0]

            if abs(x_diff) + abs(y_diff) > 2:
                t_pos[t][0] += y_diff / abs(y_diff)
                t_pos[t][1] += x_diff / abs(x_diff)
            elif abs(x_diff) > 1:
                t_pos[t][1] += x_diff / 2
            elif abs(y_diff) > 1:
                t_pos[t][0] += y_diff / 2

        tail_positions += [f"{int(t_pos[8][0])},{int(t_pos[8][1])}"]
        # print(t_pos)

print(tail_positions)

tail_unique = ["0,0"]

for x in tail_positions:
    if x not in tail_unique:
        tail_unique += [x]

print(tail_unique[:10])

print(len(tail_positions))
print(len(tail_unique))
