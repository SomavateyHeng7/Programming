for i in range(0,7):
    for j in range(0,7):
        if (j == 1 or ((i == 0 or i == 6)) and (j> 1 and j<6) or (i == 3 and j >1 and j < 5)):
            print('*', end =' ')
        else:
            print(' ', end = ' ')  
    print()