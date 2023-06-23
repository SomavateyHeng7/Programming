nList = [[2,5,99,99],[-3,8,1,2,10],[1, 7,100,10]]

for i in range(nList):
    sublist = []
    for j in range (1,4):
        sublist.append(j)
    nList.append(sublist)
print(nList)