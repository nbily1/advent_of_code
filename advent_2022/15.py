from datetime import datetime
import re

# %% 1

raw = []

with open("dev/advent_2022/15.txt", "r") as file:
    raw = [x.strip() for x in file]

# print(raw)

my_dict = {}

for x in raw:
    s_x = int(
        re.sub(pattern=r"^Sensor at x=([-0-9]+), y=([-0-9]+):.+", repl=r"\1", string=x)
    )
    s_y = int(
        re.sub(pattern=r"^Sensor at x=([-0-9]+), y=([-0-9]+):.+", repl=r"\2", string=x)
    )
    b_x = int(
        re.sub(
            pattern=r".+closest beacon is at x=([-0-9]+), y=([-0-9]+)$",
            repl=r"\1",
            string=x,
        )
    )
    b_y = int(
        re.sub(
            pattern=r".+closest beacon is at x=([-0-9]+), y=([-0-9]+)$",
            repl=r"\2",
            string=x,
        )
    )

    my_dict[f"{s_x},{s_y}"] = {
        "type": "S",
        "coord": [s_x, s_y],
        "closest": [b_x, b_y],
        "dist": abs(s_x - b_x) + abs(s_y - b_y),
    }
    if f"{b_x},{b_y}" not in my_dict:
        my_dict[f"{b_x},{b_y}"] = {"type": "B", "coord": [b_x, b_y]}

print(my_dict)
print("")

# out_dict = my_dict.copy()

# blocked = 0
# target_y = 2000000

# for x in my_dict:
#     if my_dict[x]["type"] == "S":  # and x == "8,7":
#         print(f"\n{datetime.now()}: Starting Sensor {x}")

#         coord = my_dict[x]["coord"]
#         closest = my_dict[x]["closest"]

#         dist = abs(coord[0] - closest[0]) + abs(coord[1] - closest[1])
#         print(f"Distance: {dist}")

#         if target_y > coord[1] + dist and target_y < coord[1] - dist:
#             continue

#         shifts = []

#         y_shift = target_y - coord[1]

#         for x_shift in range(0, dist - abs(y_shift) + 1):
#             if x_shift + y_shift > dist or (x_shift == 0 and y_shift == 0):
#                 continue
#             shifts += [[x_shift, y_shift]]
#             if x_shift > 0:
#                 shifts += [[-x_shift, y_shift]]

#         print(f"{len(shifts)} shifts")

#         for shift in shifts:
#             shifted = [coord[0] + shift[0], coord[1] + shift[1]]
#             if f"{shifted[0]},{shifted[1]}" not in out_dict:
#                 out_dict[f"{shifted[0]},{shifted[1]}"] = {"type": "#", "coord": shifted}
#                 if shifted[1] == target_y:
#                     blocked += 1

#         print(f"{datetime.now()}: Finished Sensor {x}")


# print(blocked)

# %% 2


def in_another_area(inb: list, mydict: dict):
    for check in my_dict:
        if my_dict[check]["type"] == "S":
            if (
                abs(my_dict[check]["coord"][0] - inb[0])
                + abs(my_dict[check]["coord"][1] - inb[1])
                <= my_dict[check]["dist"]
            ):
                return True
    return False


lower_bound = 0
upper_bound = 4000000

out_dict = my_dict.copy()

for x in my_dict:
    if my_dict[x]["type"] == "S":
        print(f"\n{datetime.now()}: Starting Sensor {x}")

        coord = my_dict[x]["coord"]
        closest = my_dict[x]["closest"]
        dist = my_dict[x]["dist"]
        print(f"Distance: {dist}")

        out_dict[x]["dist"] = dist

        perimiters = []

        x_shift = 0
        while x_shift <= dist + 1:
            per = []
            per += [[coord[0] + x_shift, coord[1] + (dist + 1 - x_shift)]]
            if (dist + 1 - x_shift) != 0:
                per += [[coord[0] + x_shift, coord[1] - (dist + 1 - x_shift)]]
            if x_shift != 0:
                per += [[coord[0] - x_shift, coord[1] + (dist + 1 - x_shift)]]
            if x_shift != 0 and (dist + 1 - x_shift) != 0:
                per += [[coord[0] - x_shift, coord[1] - (dist + 1 - x_shift)]]

            perimiters += [
                z
                for z in per
                if z[0] >= lower_bound
                and z[1] >= lower_bound
                and z[0] <= upper_bound
                and z[1] <= upper_bound
                and in_another_area(z, my_dict) == False
            ]

            x_shift += 1

        out_dict[x]["perimiter"] = perimiters

        print(f"{datetime.now()}: Finished Sensor {x}")

print(out_dict)

perimiters = []

for x in out_dict:
    if out_dict[x]["type"] == "S":
        if out_dict[x]["perimiter"]:
            perimiters += out_dict[x]["perimiter"]

perimiters.sort()
print(perimiters)
for i in range(len(perimiters) - 3):
    if (
        perimiters[i] == perimiters[i + 1]
        and perimiters[i] == perimiters[i + 2]
        and perimiters[i] == perimiters[i + 3]
    ):
        print(f"{perimiters[i]} found 4 times!")
        print([perimiters[i], (perimiters[i][0] * 4000000) + perimiters[i][1]])
        quit()
