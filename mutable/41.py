def MoDuplicate(int_list):
    newlist = []
    seen = set()
    for item in int_list:
        if item not in seen:
            seen.add(item)
            newlist.append(item)
        else:
            if item % 2 ==0:
                newlist.append(item*20)
            else:
                newlist.append(item*10)
    return newlist

int_list = [1,1,3,5,4,5,4,9,4,8,6]
out_li = MoDuplicate(int_list)
print(out_li)


def Version2MoDuplicate(list2):
    seen = set()
    for i in range(len(list2)):
        if list2[i] not in seen:
            seen.add(list2[i])
        else:
            if list2[i] % 2 == 0:
                list2[i] *= 20
            else:
                list2[i] *= 10

list2 = [1,1,3,5,4,5,4,9,4,8,6]
Version2MoDuplicate(list2)
print(list2)
