exList = [] 
exList.append([2,4,6]) 
print(exList) 
exList.append([8,10,12]) 
print(exList) 
for i in range(len(exList)):
    for j in range(len(exList[i])):
        print(exList[i][j],end=' ')
    print()