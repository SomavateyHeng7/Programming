for i in range(1,10):
    for j in range(1,10):
        if i == 1 or i == 9 or j == 1 or j == 9:
            print(f'{i*j:2d}', end = ' ')
        else:
            print(f'--', end = ' ')
    print()
