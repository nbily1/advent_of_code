# %% 1

ls = []

with open("advent_2022/07.txt", "r") as file:
    ls = [x.strip() for x in file]

# print(ls)

thispath = "/"
filelist = []
file_dict = {}

# print(file_dict)

# quit()

for x in ls:
    x = x.split()

    if x[0] == "$":
        if x[1] == "cd" and x[2] != "/":
            if x[2] != "..":
                thispath += x[2] + "/"
            else:
                thispath = "/".join(thispath.split("/")[:-2]) + "/"
    elif x[0][0] in "1234567890":
        filelist += [[thispath + x[1], int(x[0])]]

    # print(thispath)

# print(filelist)


for x in filelist:
    thisdir = x[0].split("/")[1:-1]
    for y in range(0, len(thisdir) + 1):
        # print("/" + "/".join(thisdir[:y]))
        # continue
        try:
            file_dict["/" + "/".join(thisdir[:y])] += x[1]
        except KeyError:
            file_dict["/" + "/".join(thisdir[:y])] = x[1]

print(file_dict)


total_size = 0

for x in file_dict:
    if file_dict[x] <= 100000:
        total_size += file_dict[x]

print(total_size)

# %% 2

total_disk = 70000000
needed_space = 30000000
used_space = file_dict["/"]

needed_to_delete = needed_space - (total_disk - used_space)

# print(total_disk)
# print(needed_space)
# print(used_space)
print(needed_to_delete)

to_delete = "/"
delete_size = used_space

for x in file_dict:
    if file_dict[x] <= delete_size and file_dict[x] >= needed_to_delete:
        to_delete = x
        delete_size = file_dict[x]

print(to_delete, delete_size)
