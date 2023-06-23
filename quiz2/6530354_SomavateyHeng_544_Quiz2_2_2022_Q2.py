nList = [[200,23], [-90,23,1], [15,6,2,100,8,9], [300,-9,3456], [84,23900], [3,7,9,2]]

max_val = float('-inf')
highest = []

for i in range(len(nList)):
    if len(nList[i]) > highest:
        highest = nList[i]
        

for sublist in nList:
    for num in sublist:
        if num > max_val:
            max_val = num
            
print(f' Sublist with the highest number of elements:' , highest)
print(f'The max value from this sublist is: {max_val}.')