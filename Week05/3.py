numA = int(input("Enter Num starting from A: "))
numB = int(input("Enter Num ending with B: "))

for i in range(numA, numB+1):
    if i >= 100:
        print("Wrong Input. Try again.")
    elif i >= 10:
        ones = i % 10
        tens = i // 10
        if (ones + tens) % 2 == 1:
            print("$$" , end = ' ')
        else:
            print(i, end = ' ')
    else:
        if i % 3 == 0:
            print("#" , end = ' ')
        else:
            print(i, end = ' ')
