list_of_lists = [['a', 1], ['b', 2], ['a', 1], ['b', 2], ['c', 3]]


new_list = []

for l in list_of_lists:
    if l not in new_list:
        new_list.append(l)

# 👇️ [['a', 1], ['b', 2], ['c', 3]]
print(new_list)