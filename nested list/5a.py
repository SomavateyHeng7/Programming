nList = [[2,5,99],[-3,8,9,10],[1, 7,100]]

max_val = float('-inf')
min_val = float('inf')
for sublist in nList:
    for num in sublist:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

print(f"The max value is {max_val}.")
print(f"The min value is {min_val}.")
