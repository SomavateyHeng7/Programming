ListA = [3,5,7,8,9,0]
ListB = [5,0,0]
temp_A = ListA.copy()
temp_B = ListB.copy()
check = True

if len(ListA) < len(ListB):
    for i in ListA:
        if i not in temp_B:
            check = False
            break
        else:
            temp_B.remove(i)
    if check:
        print(f'Output: Yes {ListA} appears in {ListB}.')
    else:
        print(f'Output: Not all {ListA} appears in {ListB}.')
else:
    for i in ListB:
        if i not in temp_A:
            check = False
            break
        else:
            temp_A.remove(i)
    if check:
        print(f'Output: Yes {ListB} appears in {ListA}.')
    else:
        print(f'Output: Not all {ListB} appears in {ListA}.')
 