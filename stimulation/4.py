# numList = [1,13,26,2,6,7,39,10,9]
# for i in numList:
#     if (i%13)!= 0 or i // 13 !=0:
#         print(i, end = ' ')
        
def SomeRecursive(nList):
    if len(nList) < 1:
        return 0
    else:
        return max(nList[0])+ SomeRecursive(nList[2:])
nList = [[1,2,3],[4,5,6],[7,8,9],[6,5,4]]
print(SomeRecursive(nList))