numA = int(input("Enter numA: "))
numB = int(input("Enter numB: "))
sumoffivedivisible = 0

if numA < numB:
    while numA <= numB:
        if numA % 5 == 0:
            sumoffivedivisible += numA 
        else:
            sumoffivedivisible += numA
            if sumoffivedivisible > 4 * numB:
                break
            print(numA, end = ' ')
        numA += 1
else:
    while numB <= numA:
        if numB % 5 ==0:
            sumoffivedivisible += numB
        else:
            sumoffivedivisible += numB
            if sumoffivedivisible > 4 * numA:
                break
            print(numB, end = ' ')
        numB += 1
