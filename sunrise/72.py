ListA = [[4, 6], [5, 7, 8], [1], [3, 5, 2]]
ListB = [[2, 1], [4, 2, 1], [5], [2, 8, 4]]

result = []

for i in range(len(ListA)):
    subList = []
    for j in range(len(ListA[i])):
        summation = ListA[i][j] + ListB[i][j]
        subList.append(summation)
    result.append(subList)

print(f'Output: {result}')