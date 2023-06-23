for i in range(1, 10):
    for j in range(1, 10):
        num = i * j
        all_even = True
        for k in str(num):
            if int(k) % 2 != 0:
                all_even = False
                break
        if all_even:
            print(num, end=' ')
        else:
            print("--", end=' ')
    print()
