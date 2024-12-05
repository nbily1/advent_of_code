from operator import itemgetter
import itertools

# %% Part 1

# with open("advent_2024/05.txt", "r") as file:
#     my_list = [y.split('/') for y in '/'.join([x.strip() for x in file]).split('//')]

# ordr=[x.split('|') for x in my_list[0]]
# upd = [x.split(',') for x in my_list[1]]

# # print(my_list)
# # print(ordr)
# # print(upd)

# corr = []
# incorr = []

# for u in upd:
#     is_ok = True
#     # print("\n",u)
#     for o in ordr:
#         to_check = [x for x in u.copy() if x in o]
#         # print(to_check, o)
#         if to_check == o or len(to_check) <=1:
#             continue
#         else:
#             is_ok = False
#             break
#     if is_ok is True:
#         corr += [u]
#     else:
#         incorr += [u]

# print("\n",corr)
# print("\n",incorr)

# mdl = []
# for c in corr:
#     i = round((len(c)-1)/2)
#     mdl += [int(c[i])]

# # print(mdl)
# print(sum(mdl))


# %% Part 2

with open("advent_2024/05.txt", "r") as file:
    my_list = [y.split('/') for y in '/'.join([x.strip() for x in file]).split('//')]

ordr=[x.split('|') for x in my_list[0]]
upd = [x.split(',') for x in my_list[1]]

# print(my_list)
# print(ordr)
# print(upd)

all_vals = list(set([x[0] for x in ordr] + [x[1] for x in ordr]))

my_dict = {x: {'l':[],'r':[]} for x in all_vals}

for k in my_dict:
    my_dict[k]['l'] = [x[0] for x in ordr if x[1]==k]
    my_dict[k]['r'] = [x[1] for x in ordr if x[0]==k]

print(my_dict)

corr = []
incorr = []

for u in upd:
    is_ok = True
    # print("\n",u)
    for o in ordr:
        to_check = [x for x in u.copy() if x in o]
        # print(to_check, o)
        if to_check == o or len(to_check) <=1:
            continue
        else:
            is_ok = False
            break
    if is_ok is True:
        corr += [u]
    else:
        incorr += [u]

# print("\n",corr)
print("\n",incorr)

corrected = []

def try_catch(inpt:str):
    try:
        return out_list.index(inpt)+1
    except ValueError:
        return 0


for x in incorr:
    in_list = x.copy()
    print(in_list)
    out_list = [in_list[0]]
    for i in range(1,len(in_list)):
        test = in_list[i]
        l_ind = max([try_catch(y) for y in my_dict[test]['l']]+[0])
        out_list.insert(l_ind,test)
        print(test,l_ind,out_list)
    corrected += [out_list]

mdl = []
for c in corrected:
    i = round((len(c)-1)/2)
    mdl += [int(c[i])]

# print(mdl)
print(sum(mdl))