# %% 1

transmission = []

with open("dev/advent_2022/6.txt", "r") as file:
    transmission = file.read()

marker = ""
marker_loc = 0

for i in range(len(transmission)):
    thisdict = {}
    for j in range(4):
        thisdict[transmission[i + j]] = ""
    if len(thisdict) == 4:
        marker = transmission[i : i + 4]
        marker_loc = i + 4
        break
    else:
        continue

print(transmission)
print(marker, marker_loc)

# %% 2

for i in range(len(transmission)):
    thisdict = {}
    for j in range(14):
        thisdict[transmission[i + j]] = ""
    if len(thisdict) == 14:
        marker = transmission[i : i + 14]
        marker_loc = i + 14
        break
    else:
        continue

print(transmission)
print(marker, marker_loc)
