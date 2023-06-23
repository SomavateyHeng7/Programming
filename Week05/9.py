for i in range(1,10):
    for j in range(1,10):
        num = i * j
    if all(int(x) % 2 == 0 
    for x in str(num)):
        print(num, end=" ")
    else:
        print("--", end=" ")
print()