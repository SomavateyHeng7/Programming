for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        if all(int(d) % 2 == 0 for d in str(result)):
            print(result, end=' ')
        else:
            print('--', end=' ')
    print()
