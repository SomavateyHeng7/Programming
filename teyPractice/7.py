def sum_lists(ListA, ListB):
    result = []
    for i in range(len(ListA)):
        sublist_sum = [ListA[i][j] + ListB[i][j] for j in range(len(ListA[i]))]
        result.append(sublist_sum)
    return result
ListA = [[4, 6], [5, 7, 8], [1], [3, 5, 2]]
ListB = [[2, 1], [4, 2, 1], [5], [2, 8, 4]]

output = sum_lists(ListA, ListB)
print(output)