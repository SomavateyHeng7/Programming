List_1 = [2,4,10]
List_2 = [1,5,10,20]

for i in (List_2):
    for j in (List_1):
        if i*j < 100:
            print(f'{i*j:>3d}',end = ' ')
        else:
            print('***')
    print()
    