ListA = [[4, 6], [5, 7, 8], [1], [3, 5, 2]]
ListB = [[2, 1], [4, 2, 1], [5], [2, 8, 4]]

result = []
i = 0

while i < len(ListA):
    j = 0
    inner = []
    while j < len(ListA[i]):
        summation = ListA[i][j] + ListB[i][j]
        inner.append(summation)
        j += 1
    result.append(inner)
    i+=1
    
print(f'Output: {result}')