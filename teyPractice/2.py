ListA = [[4,6], [5,7,8], [1], [3,5,2]]
ListB = [[2,1], [4,2,0], [5], [2,8,4]]

summation = []

for i in range(len(ListA)):
    for j in range(len(ListB)):
        summation.append(ListA[i] + ListB[j])

print(summation)