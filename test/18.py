for i in range(0,7):
    for j in range(0,7):
        if (j == 1 or (i == 6 and j != 0 and j < 6)):
            print('*', end =' ')
        else:
            print(' ', end = ' ')
    print()