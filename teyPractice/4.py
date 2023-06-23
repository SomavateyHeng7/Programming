ListA = [[4,6], [5,7,8], [1], [3,5,2]]
ListB = [[2,1], [4,2,0], [5], [2,8,4]]

summations = []

for sublist_a, sublist_b in zip(ListA, ListB):
    sublist_sum = []
    for a, b in zip(sublist_a, sublist_b):
        sublist_sum.append(a + b)
    summations.append(sublist_sum)

print("Summations:", summations)
