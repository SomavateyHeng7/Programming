ListA = [3,4,5]
ListB = [3,4,5,6,7]
temp = ListB.copy()
check = True

for i in ListA:
    if i not in ListB:
        check = False
        break
    else:
        temp.remove(i)
if check:
    print('Yes')
else:
    print('No')

