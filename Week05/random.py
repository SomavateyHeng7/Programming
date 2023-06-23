numA = int(input('Enter Num starting from A'))
numB = int(input('Enter Num starting from B'))
for num in range(numA, numB + 1):
    if num % 2 == 0:
        print(num, end=" ")
    else:
        print(f'Wrong')