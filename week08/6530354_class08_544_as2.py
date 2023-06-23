nList = [[2,5,99,99], [-3,8,1,2,10], [1, 7,100,10]]
evenList = []
oddList = []

for i in range(len(nList)):
    sepEven = []
    sepOdd = []
    for j in range(len(nList[i])):
        if nList[i][j] % 2 == 0:
            sepEven.append(nList[i][j])
        else:
            sepOdd.append(nList[i][j])
    evenList.append(sepEven)
    oddList.append(sepOdd)
print(f'Even List = {evenList}')
print(f'Odd List = {oddList}')