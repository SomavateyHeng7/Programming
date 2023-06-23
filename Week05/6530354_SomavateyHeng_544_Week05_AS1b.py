for i in range(1, 10):
    for j in range(1, 10):
        if i == 1 or i == 9 or j == 1 or j == 9:
            print(f'{i*j:2d}', end = ' ')
        elif (i == 3 and 3 <=j <= 7) or (j == 3 and 3 <= i <= 7) or (i == 7 and 3 <=j <= 7) or (j == 7 and 3 <=i <= 7):
            print(f'{i*j:2d}', end = ' ')
        else:
            print("--", end=' ')
    print()
