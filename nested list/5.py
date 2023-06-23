nList = [[2,5,99],[-3,8,9,10],[1, 7,100]]

max_val = float('-inf')
min_val = float('inf')
for sub_lst in nList:
    max_val = max(max_val, *sub_lst)
    min_val = min(min_val, *sub_lst)

print(f"The max value is {max_val}.")
print(f"The min value is {min_val}.")
